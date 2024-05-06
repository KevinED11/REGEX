import re


def find_all_numbers(pattern: str, text: str) -> list[str]:
    return re.findall(pattern, text)


def main() -> None:
    result = find_all_numbers(r"\d", "The password is 12345")
    print(result)


if __name__ == "__main__":
    main()
