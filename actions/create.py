from github import Github # https://github.com/PyGithub/PyGithub

with open("client_secret") as f:
  token = f.readline().strip()
g = Github(token)

def secure(data):
  core = g.get_repo("chrishodsongithubhomework/core")
  core.create_issue(title=f"New repo created: {repo_name}")
  try:
    repo_name = data["repository"]["name"]
    print(f"repo name {repo_name} created")
    repo = g.get_repo(repo_name)
    repo.edit(private=True, has_issues=True)
    branch = repo.get_branch("main")
    branch.edit_protection(dismiss_stale_reviews=True,
        require_code_owner_reviews=True,
        required_approving_review_count=1)
    core.create_issue(title=f"Security settings updated for {repo_name}", body="Branch protections enabled")
  except:
    print("unable to complete all security steps")
    return False
  return True

def suggestions(data):
  repo_name = data["repository"]["name"]
  repo = g.get_repo(repo_name)
  if repo.description = "":
    repo.create_issue(title=f"Suggestion - update description", body="Consider adding a description to your new repo")
