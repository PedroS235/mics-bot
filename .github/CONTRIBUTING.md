# Welcome to BICS-BOT contributing guide

Thank you for investing your time in contributing to our project! Any contribution you make will be reflected on [BICS-BOT](https://github.com/Luxembourg-Open-Source-Club/BICS-BOT) :sparkles:.

Read our [Code of Conduct](./CODE_OF_CONDUCT.md) to keep our community approachable and respectable.

In this guide you will get an overview of the contribution workflow from opening an issue, creating a PR, reviewing, and merging the PR.

## Technical Requirements Before Starting
- We expect you to develop on a UNIX-based operating system. If you are on Windows, follow [this tutorial](https://learn.microsoft.com/en-us/windows/wsl/install) on installing WSL.
- Use Python3.8 and above.

## New contributor guide

To get an overview of the project, read the [README](README.md). Here are some resources to help you get started with open source contributions:
- [Finding ways to contribute to open source on GitHub](https://docs.github.com/en/get-started/exploring-projects-on-github/finding-ways-to-contribute-to-open-source-on-github)
- [Set up Git](https://docs.github.com/en/get-started/quickstart/set-up-git)
- [GitHub flow](https://docs.github.com/en/get-started/quickstart/github-flow)
- [Collaborating with pull requests](https://docs.github.com/en/github/collaborating-with-pull-requests)

## Setting Up Development Environment
1. Create your own bot. You can follow [this tutorial](https://discord.com/developers/docs/getting-started), where you should do everything in step 1, and stop before step 2. Below are some answers to questions you might have about the setup process.

### Setup FAQ

#### What should the name of my testing bot be?
The name of your bot does not matter. The bot you are creating in this guide is your own, personal, testing bot. Completely disconnected from the production bot (the bot that students are using on the Discord server).

#### What priviliges should I give to my testing bot in the **Bot** section?
In the section **Priviliged Gateway Intents**, toggle all three options. When you scroll down, you will find a section called **Bot Permissions**. Check the **Administrator** box.

#### Where do I get the token for my testing bot?
Sometimes, Discord doesn't give the token at first. All you have to do is;
1. Navigate to the **Bot** page from the left sidebar.
2. Click **Reset Token**.
3. Write it down and do not lose it. DO NOT SHARE IT WITH ANYONE.
4. In case you lose it, repeat the steps above, and update your used token in the codebase.

#### What **Bot Permissions** should I choose in the **URL Generator** section?
After you choose `applications.command` and `bot` as your scopes, a new **Bot Permissions** section will be available below. Just as before, toggle the **Administrator** checkbox.

### Issues

#### Create a new issue

If you spot a problem with BICS-BOT, [search if an issue already exists](https://docs.github.com/en/github/searching-for-information-on-github/searching-on-github/searching-issues-and-pull-requests#search-by-the-title-body-or-comments). If a related issue doesn't exist, you can open a new issue using a relevant [issue form](https://github.com/Luxembourg-Open-Source-Club/BICS-BOT/issues/new/choose).

#### Solve an issue

Scan through our [existing issues](https://github.com/Luxembourg-Open-Source-Club/BICS-BOT/issues) to find one that interests you. You can narrow down the search using `labels` as filters. Once you spot an issue you are interested in solving, feel free to self-assign it and create a branch for it to start working. Pay attention to issues labeled **good first issue**

### Make Changes

#### Make changes locally

1. Clone the repo so that you can make your changes without affecting the original project until you're ready to merge them.

2. [Create a virtual environment](https://docs.python.org/3/library/venv.html#creating-virtual-environments) for Python, and [activate it](https://docs.python.org/3/library/venv.html#how-venvs-work). _**If you are on Linux**_, you must first install the package `python3-venv` using your distro's package manager.

3. Install requirements via `$ pip install -r requirements.txt`

4. Create a working branch and start with your changes!

### Commit your update

Commit the changes once you are happy with them.

### Pull Request

When you're finished with the changes, create a pull request, also known as a PR.
- Fill the "Ready for review" template so that we can review your PR. This template helps reviewers understand your changes as well as the purpose of your pull request.
- Don't forget to [link PR to issue](https://docs.github.com/en/issues/tracking-your-work-with-issues/linking-a-pull-request-to-an-issue) if you are solving one.
- Enable the checkbox to [allow maintainer edits](https://docs.github.com/en/github/collaborating-with-issues-and-pull-requests/allowing-changes-to-a-pull-request-branch-created-from-a-fork) so the branch can be updated for a merge.
Once you submit your PR, a BICS-BOT senior member will review your proposal. We may ask questions or request additional information.
- We may ask for changes to be made before a PR can be merged, either using [suggested changes](https://docs.github.com/en/github/collaborating-with-issues-and-pull-requests/incorporating-feedback-in-your-pull-request) or pull request comments. You can apply suggested changes directly through the UI. You can make any other changes in your fork, then commit them to your branch.
- As you update your PR and apply changes, mark each conversation as [resolved](https://docs.github.com/en/github/collaborating-with-issues-and-pull-requests/commenting-on-a-pull-request#resolving-conversations).
- If you run into any merge issues, checkout this [git tutorial](https://github.com/skills/resolve-merge-conflicts) to help you resolve merge conflicts and other issues.

### Your PR is merged!

Congratulations :tada::tada: The BICS-BOT team thanks you :sparkles:.

Once your PR is merged, your contributions will be publicly visible on the [BICS-BOT repo](https://github.com/Luxembourg-Open-Source-Club/BICS-BOT).