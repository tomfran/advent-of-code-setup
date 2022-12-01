import os

base_link = "https://github.com/<USERNAME>/<REPOSITORY_NAME>/blob/main/src/"


def parse(e):
    name = e.replace(".py", "")
    # name = " ".join(name.split("_")[1:])
    return f"[{name}]({base_link}{e})"


solutions = filter(lambda x: ".py" in x and "init" not in x, os.listdir("src"))

readme_content = "# Advent of code\nProblems list:\n"
tmp = [f"{i+1}. {parse(e)}" for i, e in enumerate(sorted(solutions))]
readme_content += "\n".join(tmp)

with open("README.md", "w") as f:
    f.write(
        readme_content
        + "\n\nCreated via: [advent-of-code-setup](https://github.com/tomfran/advent-of-code-setup)"
    )
