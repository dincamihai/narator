import re
import requests
from requests.auth import HTTPBasicAuth
import argparse
import config
from urllib.parse import urlparse
from jinja2 import Environment, PackageLoader, select_autoescape


def get_auth():
    return HTTPBasicAuth(config.github['user'], config.github['token'])


def authenticate(fun):
    def wrapper(*args, **kwargs):
        return fun(get_auth(), *args, **kwargs)
    return wrapper


def get_template():
    env = Environment(
        loader=PackageLoader('narator', 'templates'),
        autoescape=select_autoescape(['txt'])
    )

    return env.get_template('template.txt')


def aggregate(comments):
    template = get_template()
    def topic_dict_factory():
        return {
            'title': '',
            'done': [],
            'todo': []
        }
    aggregation = []
    for comment in comments:
        lines = comment.splitlines()
        topic = {
            'title': lines[0],
            'done': [],
            'todo': []
        }
        for line in lines[1:]:
            if not line:
                continue
            status, content = re.match('^(?P<status>todo|done) (?P<content>.*)$', line).groups()
            topic[status].append(content)
        aggregation.append(topic)
    rendered_aggregation = template.render(
        topics=aggregation,
    ).encode("utf-8").strip()
    return rendered_aggregation


@authenticate
def main(auth, url):
    result = urlparse(url)
    session = requests.Session()
    request = requests.Request(
        'GET',
        'https://api.github.com/repos{0}/comments'.format(result.path),
        headers={
            'User-Agent': 'narator-app'
        },
        auth=auth
    )
    prepped = request.prepare()
    response = session.send(prepped)
    response.raise_for_status()
    bodies = []
    for comment in response.json():
        bodies.append(comment['body'])
    print(aggregate(bodies).decode('utf8'))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('url', type=str)
    args = parser.parse_args()
    main(args.url)
