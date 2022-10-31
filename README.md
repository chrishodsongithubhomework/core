# core account.
This account hold the central code that oversees all repos

## EnsureSecurity App
This app runs on a server and listens for incoming events.  presently, it only listens for the creation of new repos and takes actions to ensure they are secure.

The code is in two parts
### The listener
This is in webhook.py and listens for incoming events.  If the event is a repo create, it will call the actions

### Actions
This is set of files (curently 1) that take action on a newly created repo, ensuring it is secure.
Actions taken:
- Set the repository to private
- Ensure Issues is turned on the the new repo
- Add branch protection to the "main" branch
- Add an Issue to the core repo to log that a new repository has been created

## To run as a container:
1. > docker build -t github-webhook .
2. > docker run -ditp 5000:5000 --name github-webhook \\
   > --restart=unless-stopped \\
   > github-webhook

Or run the container in something like [AWS Fargate](https://aws.amazon.com/fargate/).

#### TODO
- Add error checking
- Add secret to app
- Move from PAT to PEM key
- Add more suggestions
