import requests
from pprint import pprint
import argparse
import os

#YOU HAVE TO ADD THE FOLDER DIST TO YOUR SYSTEM VARIABLES PATH

parser = argparse.ArgumentParser()
parser.add_argument("--name","-n",type=str,dest="name",required=True)
parser.add_argument("--private","-p",dest="is_private",action="store_true")
args = parser.parse_args()
print(args)
repo_name = args.name
is_private = args.is_private

api_url = "https://api.github.com" 

if is_private:
  payload = '{"name":"' + repo_name + '", "private": true }' 
else:
  payload = '{"name":"' + repo_name + '", "private": false }' 

print(payload)

github_token = "YOUR-PERSONAL-TOKEN-FROM-API-OF-GITHUB"
headers = {
  "Authorization": "token " + github_token,
  "Accept": "application/vnd.github.v3+json"
}

try:
  r = requests.post(api_url+"/user/repos", data=payload, headers=headers)
  r.raise_for_status()
except requests.exceptions.RequestException as err:
  raise SystemExit(err)

try:
  repo_path = "/Users/57304/Documents/Repositories/"
  os.chdir(repo_path)
  os.system("mkdir " + repo_name)
  os.chdir(repo_path + repo_name)
  os.system("git init")
  os.system("git remote add origin https://github.com/Ivan-Sanchez-Diaz/" + repo_name + ".git")
  os.system("echo # " + repo_name + " >> README.md")
  os.system("git add . && git commit -m 'initial' && git push origin master")
except FileExistsError as err:
  raise SystemExit(err)

