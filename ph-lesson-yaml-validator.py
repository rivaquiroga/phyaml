#!/usr/bin/env python3
""" Validates a Programming Historian lesson file (.md)
    against a YAML schema.
    Created by Riva Quiroga (riva.quiroga@uc.cl) and
    Nicolas Vaughan (nivaca@fastmail.com), 2021. """

import os
import re
import sys
from typing import Type
import click
from yamale import YamaleError, make_data, make_schema, validate, schema

VERSION = "0.1 (2021-11-06)"
TRANS_SCHEMA = "translated-lesson-schema.yaml"
ORIG_SCHEMA = "original-lesson-schema.yaml"


def get_metadata(fulltext: str) -> list:
    """ Given a text, extract the metadata section (between '---' and '---')
    and return a yamale meta_data object. """
    pattern = r'--- ?\n(.+?)--- ?\n'
    match = re.search(pattern, fulltext, re.DOTALL)
    if not match:
        click.secho('Error! No metadata found in file.', fg='red')
        sys.exit(1)
    metadata = match.group(1)
    return make_data(content=metadata)


def select_schema(data: list) -> schema.Schema:
    datadict = data[0][0]
    if "translator" in datadict.keys():
        schema = make_schema(TRANS_SCHEMA)
        schemafname = TRANS_SCHEMA
        lessontype = 'translation'
    else:
        schema = make_schema(ORIG_SCHEMA)
        schemafname = ORIG_SCHEMA
        lessontype = 'original lesson'
    click.secho(f"Lesson type: {lessontype}", fg='blue')
    click.secho(f"Using schema file: {schemafname}", fg='blue')
    return schema


def validate_data(schema: schema.Schema, data: str, inputfile: str):
    try:
        validate(schema, data)
        click.secho('Validation successful!', fg='green')
        sys.exit(0)
    except YamaleError as e:
        click.secho('Validation failed!', fg='red')
        for result in e.results:
            click.secho(f"Error validating ‘{inputfile}’ with schema ‘{result.schema}’:", fg='red')
            for error in result.errors:
                click.secho(f'  - {error}', fg='red')
        sys.exit(1)


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# +                               main()                               +
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

@click.command()
@click.option('--schemafile', help='YAML schema file (if not using the default ones)')
@click.argument('inputfile', default='')
def main(inputfile: str, schemafile: str):
    scriptname = "ph-lesson-yaml-validator.py"

    if not inputfile:
        click.secho(f"Usage: {scriptname} [OPTIONS] INPUTFILE\n"
                    f"Try '{scriptname} --help' for help.", fg='blue')
        click.secho(f"Error: Missing argument 'INPUTFILE'.", fg='red')
        sys.exit(1)

    mdfn, mdfn_ext = os.path.splitext(inputfile)
    if mdfn_ext.lower() != '.md':
        click.secho(f'Error: input file (‘{inputfile}’) must have ‘.md’ extension.', fg='red')
        sys.exit(1)

    if not os.path.exists(inputfile):
        click.secho(f"Error: {inputfile} not found.", fg='red')
        sys.exit(1)

    with open(inputfile, encoding="utf-8") as file:
        fulltext = file.read()

    data = get_metadata(fulltext)

    if schemafile:
        click.secho(f"Using schema file: {schemafile}", fg='blue')
        schema = make_schema(schemafile)
    else:
        schema = select_schema(data)

    validate_data(schema, data, inputfile)


if __name__ == "__main__":
    main()
