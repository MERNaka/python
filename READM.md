python 

programming language
guido rossum 1991
server side web application

GIT NOTES
git --version

Step 2: Create a New GitHub Repo
Go to https://github.com

Click on “New Repository”
Name it something like python-practice
Leave other options as default (don’t check README or .gitignore)
Click Create Repository

git init
git remote add origin https://github.com/yourusername/python-practice.git
git add .
git commit -m "Initial commit"
git branch -M main
git push -u origin main

On future pushes, you’ll just need:
git add .
git commit -m "your message"
git push

Personal Access Token (PAT).

Go to: https://github.com/settings/tokens
Click "Generate new token" (→ Classic)
Select scopes:
repo (all checkboxes under it)
Set expiry (e.g., 30 or 90 days)
Click Generate Token
Copy the token and save it (you won’t see it again!)

git push --set-upstream origin master
git branch -M main
git push -u origin main
