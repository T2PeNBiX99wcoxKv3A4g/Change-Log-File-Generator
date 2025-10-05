# coding: utf-8
import os

import typer
from icecream import ic

change_log_path: str = "./CHANGELOG.md"
change_log_keyword: str = "Changelog"
title_keyword: str = "##"
url_keyword: str = "["
change_log_title: str = "# Changelog"


def main(new_change_log: str, debug: bool = False) -> None:
    if debug:
        ic.enable()
    else:
        ic.disable()

    ic(new_change_log)

    new_change_logs = new_change_log.split("\n")
    change_log_lines: list[str] = []

    for log in new_change_logs:
        new_log = log.strip().replace("\n", "")
        if new_log == "":
            continue
        change_log_lines.append(new_log)

    ic(change_log_lines)

    if os.path.isfile(change_log_path):
        with open(change_log_path, "r+") as file:
            count = 0

            for line in file.readlines():
                line = line.strip().replace("\n", "")
                start = line.find(change_log_keyword)

                ic(line, count)

                if count == 0 and start > -1:
                    count += 1
                    continue
                elif line == "\n" or line == "":
                    count += 1
                    continue

                count += 1
                change_log_lines.append(line)

    ic(change_log_lines)

    for line in change_log_lines:
        find_start = line.find(title_keyword)
        url_start = line.find(url_keyword)

        ic(line, find_start)
        ic(line, url_start)

        if find_start > -1 and url_start > -1:
            new_line = f"## {line[url_start::]}"
            change_log_lines[change_log_lines.index(line)] = new_line
            ic(new_line)

    ic(change_log_lines)

    change_log_content = "\n\n".join(change_log_lines)
    new_text = f"{change_log_title}\n\n{change_log_content}"
    ic(new_text, change_log_content)

    typer.echo(f"Changelog file generated: {new_text}")

    with open(change_log_path, "w+") as file:
        file.seek(0)
        file.truncate(0)
        file.write(new_text)
        file.close()


if __name__ == "__main__":
    typer.run(main)
