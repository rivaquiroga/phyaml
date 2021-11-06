![status](https://img.shields.io/badge/status-WIP-lightgrey)

# phyaml

A very first draft of a YAML validator for Programming Historian lessons.

While we work on developing the script, you can use the code on `ph-lesson-yaml-validator.py` editing two lines of code:

1. If the lesson you are editing is a translation, change the schema file to  `translated-lesson-schema.yaml` in this line:

```python
schema = yamale.make_schema('./original-lesson-schema.yaml')
```
If your are editing an original lesson, you don't need to make any changes.

2. Add the path to the .md file of the lesson you are editing here:

```python
lesson = frontmatter.load('PATH-TO/LESSON-FILE.md')
```
That's all.
If you run the script and something is missing, you will see a message similar to this one:

```
abstract: Required field missing
doi: Required field missing
```
