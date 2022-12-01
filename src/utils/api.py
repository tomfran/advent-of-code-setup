import requests
from os.path import exists


def get_session_id(filename):
    with open(filename) as f:
        return f.read().strip()


def get_url(year, day):
    return f"https://adventofcode.com/{year}/day/{day}/input"


YEAR = 2022
SESSION_ID_FILE = "session.cookie"
SESSION = get_session_id(SESSION_ID_FILE)


def get_input(day):
    path = f"inputs/{day:02d}"

    if not exists(path):
        url = get_url(YEAR, day)
        headers = requests.utils.default_headers()
        headers.update(
            {"User-Agent": "github.com/tomfran/advent-of-code-setup reddit:fran-sch"}
        )
        response = requests.get(url, headers=headers, cookies={"session": SESSION})
        if not response.ok:
            raise RuntimeError(
                f"Request failed\n\tstatus code: {response.status_code}\n\tmessage: {response.content}"
            )
        with open(path, "w") as f:
            f.write(response.text[:-1])

    with open(path, "r") as f:
        return f.read()
