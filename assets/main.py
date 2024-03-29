from pdf_to_text import *
from text_to_sections import *


def read_convert_write(source, dest):
    text = pdf_to_text(source)
    sections, contents = text_to_section_contents(text)
    section_contents_to_dir(sections, contents, dest)

    for key, section in sections:
        print(key, section)


if __name__ == "__main__":
    if len(argv) < 3:
        print("args: <source> <dest>")
        exit(1)
    source = argv[1]
    dest = argv[2]
    read_convert_write(source, dest)
