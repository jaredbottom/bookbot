from pathlib import Path


def main():
    file_contents = Path('books/frankenstein.txt').read_text().lower()

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{len(file_contents.split())} words found in the document\n")

    letters = dict.fromkeys([x for x in 'abcdefghijklmnopqrstuvwxyz'], 0)

    for x in file_contents:
        try:
            letters[x] += 1
        except:
            pass

    for x in letters:
        print(f"the '{x}' character was found {letters[x]} times")

    print("--- End report ---")


main()
