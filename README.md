![status](https://img.shields.io/badge/status-WIP-lightgrey)

# phyaml

## A very first draft of a YAML validator for Programming Historian lessons.

## USAGE:

```sh
python3 ph-lesson-yaml-validator.py lesson.md
```

The script automatically detects the lesson type (either an original lesson or a translation) and selects the schema file accordingly:

- `original-lesson-schema.yaml`
- `translated-lesson-schema.yaml`

If the user prefers so, they can also specify another schema file with the argument `--schemafile`, followed by the file name, e.g.:

```sh
python3 ph-lesson-yaml-validator.py lesson.md --schemafile anotherschema.yaml
```

That's all.
If you run the script and something is missing, you will see a message similar to this one:

```
abstract: Required field missing
doi: Required field missing
```
