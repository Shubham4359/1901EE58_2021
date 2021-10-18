import os
import re

movie_re = r"(?P<movie>[\w\s]+\-?\s)"

se_re1 = r"s(?P<season>\d+)e(?P<episode>\d+)\s"
se_re2 = r"(?P<season>\d+)x(?P<episode>\d+)\s\-\s"

title_re = r"(?P<title>[\w\s']+)"
extension_re = r"(?P<extension>\.(mp4|srt))"

body_re1 = fr".+\.{title_re}{extension_re}"
body_re2 = fr"{title_re}.+{extension_re}"


def regex_renamer():

    # Taking input from the user

    choices = ["Breaking Bad", "Game of Thrones", "Lucifer"]

    for idx, choice in enumerate(choices):
        print(f"{idx + 1}. {choice}")

    webseries_num = int(input("Enter the number of the web series that you wish to rename. 1/2/3: "))
    season_padding = int(input("Enter the Season Number Padding: "))
    episode_padding = int(input("Enter the Episode Number Padding: "))

    regex = None
    if webseries_num == 1:
        regex = fr"{movie_re}{se_re1}{body_re1}"
    elif webseries_num == 2 or webseries_num == 3:
        regex = fr"{movie_re}{se_re2}{body_re2}"
    else:
        raise ValueError("webseries_num must be within 1-3")

    relative_path = "srt"
    path = os.path.join(relative_path, choices[webseries_num - 1])

    pattern = re.compile(regex)

    files = os.listdir(path)

    def get_number(num, pad_by):
        num = str(int(num))
        while len(num) < pad_by:
            num = "0" + num
        return num

    for file in files:
        print(file)
        m = pattern.search(file)
        season = get_number(m.group("season"), season_padding)
        episode = get_number(m.group("episode"), episode_padding)
        hyphen = "- " if webseries_num != 1 else ""
        new_file_name = f"{m.group('movie')}Season {season} Episode {episode} {hyphen}{m.group('title')}{m.group('extension')}"
        os.rename(os.path.join(path, file), os.path.join(path, new_file_name))


regex_renamer()
