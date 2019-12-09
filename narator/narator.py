#! /usr/bin/env python3

import os
import re
import argparse
import requests

from urllib.parse import urlparse
from requests.auth import HTTPBasicAuth

from narator import get_template



def new_topic():
    return {
        'title': '',
        'done': [],
        'todo': []
    }


def aggregate(body):
    template = get_template()
    def topic_dict_factory():
        return {
            'title': '',
            'done': [],
            'todo': []
        }
    aggregation = []
    lines = body.splitlines()
    for line in lines:
        if not line:
            continue
        match = re.match('^(?P<status>todo|done) (?P<content>.*)$', line)
        if not match:
            aggregation.append(new_topic())
            aggregation[-1]['title'] = line.strip()
        else:
            status, content = match.groups()
            if not aggregation:
                aggregation.append(new_topic())
            aggregation[-1][status].append(content)
    rendered_aggregation = template.render(
        topics=aggregation,
    ).encode("utf-8").strip()
    return rendered_aggregation


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('url', type=str)
    args = parser.parse_args()
    url = args.url
    result = urlparse(url)
    session = requests.Session()
    headers={
        'User-Agent': 'narator-app',
        'Authorization': 'token {0}'.format(os.environ['GITHUB_TOKEN'])
    }
    request = requests.Request(
        'GET',
        'https://api.github.com/repos{0}'.format(result.path),
        headers=headers
    )
    prepped = request.prepare()
    response = session.send(prepped)
    response.raise_for_status()
    markdown = aggregate(response.json()['body']).decode('utf8')
    print(markdown)
    url = 'https://api.github.com/repos{0}/comments'.format(result.path)
    method = 'post'
    if response.json()['comments']:
        comments = requests.get(url, headers=headers)
        comments.raise_for_status()
        url = comments.json()[0]['url']
        method = 'patch'
    post_markdown_response = getattr(requests, method)(
        url,
        headers=headers,
        json={
            "body": markdown
        }
    )
    post_markdown_response.raise_for_status()


if __name__ == '__main__':
    main()
