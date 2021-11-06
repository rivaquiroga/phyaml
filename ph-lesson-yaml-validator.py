import yamale
import frontmatter

schema = yamale.make_schema('./original-lesson-schema.yaml')

lesson = frontmatter.load('./LESSON-FILE.md')

md_text = frontmatter.dumps(lesson)

lesson_metadata = md_text.split("---")[1].split("---")[0]

data = yamale.make_data(content=lesson_metadata)

yamale.validate(schema, data)

