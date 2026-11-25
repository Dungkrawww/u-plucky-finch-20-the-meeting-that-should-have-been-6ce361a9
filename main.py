# u-plucky-finch-20-the-meeting-that-should-have-been-6ce361a9: The Meeting That Should Have Been an Email
# A single funny line of text, at most 200 characters.
# The program writes the line to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR).
import os

OUT = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
LINE = "We spent an hour in a meeting deciding what the email should say, then scheduled another meeting to approve sending it."


def validate_line(text):
    assert 1 <= len(text) <= 200, "line must be 1-200 characters"
    assert text.strip(), "line must not be only whitespace"
    assert "\n" not in text, "line must be a single line"


def main():
    validate_line(LINE)
    os.makedirs(OUT, exist_ok=True)
    with open(os.path.join(OUT, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
