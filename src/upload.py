from github import Github
from github import Auth

# create md file
import createmd

auth = Auth.Token("<your access token>")

# First create a Github instance:
g = Github(auth=auth)

repo = g.get_user().get_repo("<repo name>")
all_files = []
contents = repo.get_contents("")
while contents:
    file_content = contents.pop(0)
    if file_content.type == "dir":
        contents.extend(repo.get_contents(file_content.path))
    else:
        file = file_content
        all_files.append(str(file).replace('ContentFile(path="','').replace('")',''))

with open('Readme.md', 'r') as file:
    content = file.read()

# Upload to github
git_prefix = ''
git_file = git_prefix + 'README.md'
if git_file in all_files:
    contents = repo.get_contents(git_file)
    repo.update_file(contents.path, "committing files", content, contents.sha, branch="main")
    print(git_file + ' UPDATED')
else:
    repo.create_file(git_file, "committing files", content, branch="main")
    print(git_file + ' CREATED')