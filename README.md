#### Usage

  - virtualenv --python=python3 sandbox
  - . sandbox/bin/activate
  - pip install -r requirements.txt
  - GITHUB_TOKEN=\<auth-token-here> python narator.py \<url-to-work-report-issue>


#### Example

Issue description:

```
Title 1

todo create PR
done investigate
done discuss with team#1
```

Output:

```markdown
#### Title 1
  - DONE:
    - investigate
    - discuss with team#1
  - TODO
    - create PR
```
