# Autonomous Vehicles: Perception

Coding exercises and learning notes by Ercan Kaçmaz for the Autonomous Vehicles:
Perception lectures.

The first planned exercise is **Week 02: calibration**. Starter code has not yet
been imported. The programming language, dependencies, and execution commands
will be documented after inspecting that code.

## Working approach

Use one repository for the course, one directory per week, and one working branch
per week. Keep completed exercises on `main`.

1. Create the week's branch from the latest `main`.
2. Copy the original exercise into its directory.
3. Commit and push the unsolved starter code before editing it.
4. Implement and validate the solution in meaningful commits on that same branch.
5. Document how to run it and what the results mean.
6. Merge the completed week into `main`, preserving the individual commits.

A separate `develop` branch is unnecessary for this individual coursework project.
The Git history preserves the unsolved version, so there is no need to maintain
duplicate `starter/` and `solution/` source trees.

### Exercise index

| Week | Topic | Planned directory | Working branch | Status |
| --- | --- | --- | --- | --- |
| 02 | Calibration | `weeks/week02_calibration/` | `week02/calibration` | Awaiting starter code |

Add later weeks when their assignments are available. Directory and branch names
use zero-padded week numbers, for example `week03`.

### Repository organization

| Path | Purpose |
| --- | --- |
| `README.md` | Course overview, Git setup, and weekly workflow |
| `AGENTS.md` | Instructions for coding assistants working on this repository |
| `.gitignore` | Local environments, caches, bulk inputs, and generated outputs |
| `weeks/week02_calibration/` | Planned location of the first exercise |
| `weeks/weekNN_topic/` | Naming pattern for future weeks |

Create each weekly directory when importing its assignment. Preserve the provided
internal folder structure. If course scripts require a particular repository
layout, adapt this suggestion to those requirements.

## Git concepts used here

| Term | Meaning in this project |
| --- | --- |
| Local repository | Files and Git history on your computer |
| Remote repository | The copy hosted on GitHub |
| `origin` | The conventional local nickname for the GitHub remote |
| `main` | The branch with setup files and completed exercises |
| Weekly branch | A separate line of work for one week's assignment |
| Staging / `git add` | Selecting the current changes for the next commit |
| Commit | A saved local snapshot of the staged changes |
| Push | Sending local commits to GitHub |
| Pull | Bringing remote changes into the current local branch |
| Pull request (PR) | A GitHub page to review and merge a branch |
| Merge | Integrating one branch's work into another |

Commits are local until pushed. A branch is a line of history, not a second folder:
switching branches changes the tracked files in the same working directory.
Commit intended work or deliberately stash it before switching branches.

## First-time setup on Ubuntu/Linux

The commands below are instructions to run yourself; preparing these files does
not initialize a repository or contact your GitHub account. Replace uppercase
placeholders such as `YOUR_GITHUB_USERNAME` and `YOUR_GITHUB_EMAIL` before running
the relevant command. Run each step only after the previous step succeeds.

### 1. Create an empty repository on GitHub

Open [github.com/new](https://github.com/new) while signed in.

- Owner: your personal GitHub account.
- Repository name: `autonomous-vehicles-perception`.
- Description: `Coding exercises for Autonomous Vehicles: Perception.`
- Visibility: private is a sensible starting point for course assignments. Make
  it public later if sharing the starter code and solutions is permitted.
- Leave automatic README creation off.
- Do not select a `.gitignore` template or a license at this step.
- Click **Create repository**.

The remote should be empty because the first commit will come from this local
folder. Creating files on GitHub now would produce a separate initial history.
The local folder may use underscores while the GitHub name uses hyphens; they do
not have to match.

### 2. Set up GitHub authentication using SSH

If SSH access to GitHub already works, reuse it and skip key generation. Test it:

```bash
ssh -T git@github.com
```

On the first connection, verify the displayed host fingerprint against
[GitHub's published fingerprints](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/githubs-ssh-key-fingerprints)
before accepting it. A successful response says that you authenticated and that
GitHub does not provide shell access. That response is expected; this test can
exit with status 1 even when authentication succeeds.

If authentication is not configured, first check for an existing public key:

```bash
ls ~/.ssh/*.pub
```

If you already have an appropriate key, reuse it. If you have none, create one:

```bash
ssh-keygen -t ed25519 -C "YOUR_GITHUB_EMAIL"
```

Accept the default location if it is unused, and choose a passphrase. Do not
overwrite an existing key. The following commands assume the default name
`id_ed25519`; substitute your actual key filename when using another name.

```bash
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519
cat ~/.ssh/id_ed25519.pub
```

Copy the complete public-key line printed by the last command. In GitHub account
**Settings → SSH and GPG keys → New SSH key**, give it a title such as
`Ubuntu laptop`, select **Authentication Key**, paste it, and save. Copy only the
`.pub` file's contents; the file without `.pub` is your private key.

Repeat `ssh -T git@github.com` and check that it identifies the intended account.
If authentication still fails, resolve that before attempting a push.

### 3. Initialize the existing local folder

This folder already exists; you do not need to create another folder inside it.
Check that Git is available, then initialize it:

```bash
cd /home/ercankacmaz/Documents/lectures/autonomous_vehicles_perception
git --version
git init -b main
```

`git init` creates the local Git metadata, and `-b main` names the initial branch.
It does not create a GitHub repository or upload anything.

Configure the author identity for this repository:

```bash
git config --local user.name "Ercan Kaçmaz"
git config --local user.email "YOUR_GITHUB_EMAIL"
```

Use an email associated with your GitHub account, or copy your GitHub-provided
no-reply address from [email settings](https://github.com/settings/emails).
`--local` affects this repository only. These values identify commit authors;
SSH handles authentication separately.

### 4. Commit the repository setup

```bash
git status
git add README.md AGENTS.md .gitignore
git diff --cached --stat
git diff --cached
git commit -m "chore: initialize perception coursework repository"
```

Review the staged changes before committing. If Git opens a pager for a diff,
press `q` to return to the terminal. Only the three setup files belong in this
first commit; import the calibration exercise on its own branch later.

### 5. Connect to GitHub and push `main`

Use the SSH URL shown on the empty GitHub repository page:

```bash
git remote add origin git@github.com:YOUR_GITHUB_USERNAME/autonomous-vehicles-perception.git
git remote -v
git push -u origin main
```

`origin` stores the remote URL. `-u` sets `origin/main` as the upstream of local
`main`, so subsequent pushes from this branch can use `git push` alone.

Refresh the GitHub repository page: the setup files should now appear on `main`.
You initialize this existing folder once. `git clone` is for downloading an
existing remote repository into another folder or onto another computer; do not
clone another copy inside this project.

## Week 02: import the unsolved calibration exercise

Run from the repository root after the initial setup has been pushed. First make
sure `git status` reports no pending changes that need to be kept:

```bash
git status
git switch main
git pull --ff-only
git switch -c week02/calibration
mkdir -p weeks/week02_calibration
```

`git switch -c` creates the branch and switches to it. `--ff-only` updates `main`
only when Git can do so without creating a merge commit; if it refuses, inspect
the histories before proceeding.

Copy the supplied exercise contents into `weeks/week02_calibration/`, preserving
the supplied paths and TODOs. Do not copy another repository's `.git` metadata.
If there are large datasets, follow the data guidance below and document their
location separately. Do not solve, reformat, or repair the source before this
first exercise commit.

```bash
git status --short
git add weeks/week02_calibration/
git diff --cached --stat
git diff --cached
git commit -m "chore(week02): add original calibration starter code"
git push -u origin week02/calibration
```

Check that the staged set includes every required source file and small input
asset. If something is absent, inspect ignored files with
`git status --short --ignored weeks/week02_calibration/` before committing.

The original exercise is now saved both locally and on GitHub. Next, update the
exercise index to `In progress` in a separate documentation commit. Add environment
instructions or notes after the untouched starter import has been committed.

## Implement and save progress

Stay on `week02/calibration`. Read the assignment, identify meaningful subtasks,
and solve them one by one. Run the actual checks appropriate to the supplied code.
The commands below are an example checkpoint after implementing calibration:

```bash
git branch --show-current
git diff
git add weeks/week02_calibration/
git diff --cached
git commit -m "feat(week02): implement camera calibration"
git push
```

Use a commit message that describes the work actually completed. You can make
multiple solution commits; there is no need to wait until the whole week is done.
If you also changed the root exercise index, stage `README.md` explicitly.

Before merging, record these items in the week's README or a separate notes file:

- Assignment goal and the relevant mathematical model.
- Runtime and dependencies, including installation instructions.
- Required data and where it belongs.
- Exact execution and validation commands, including the working directory.
- Results, interpretation, and any known limitations.

Update the root table to `Completed` in the final documentation commit when the
exercise and its validation are ready. Record any execution you could not perform
honestly instead of presenting an untested result as verified.

## Merge a completed week

### Recommended: a GitHub pull request

1. Push all completed work on `week02/calibration`.
2. On GitHub, open **Pull requests → New pull request**.
3. Select **base: `main`** and **compare: `week02/calibration`**.
4. Use a title such as `Week 02: Camera calibration` and summarize the approach,
   checks run, results, and remaining limitations.
5. Inspect the changed files and commits. Resolve any conflicts before merging.
6. Select **Create a merge commit**, then confirm the merge.

This merge method preserves both the starter commit and the solution commits on
`main`, with an explicit completion point. Squash merging would combine those
commits into one on `main`, which is less useful for this learning history.
If the option is absent, enable **Allow merge commits** in the repository's
settings under **Pull Requests**.

After merging on GitHub, update the local repository:

```bash
git switch main
git pull --ff-only
```

Optional cleanup after confirming that the merge is present:

```bash
git branch -d week02/calibration
```

You may also use GitHub's **Delete branch** button for the remote branch. Keeping
merged branches is fine too. Removing a merged branch removes its name, not the
commits now reachable through `main`. Use `-d`, not forced deletion with `-D`.

### Alternative: merge locally

Use this instead of the GitHub merge step, with a clean working directory and all
intended Week 02 changes already committed:

```bash
git switch main
git pull --ff-only
git merge --no-ff week02/calibration -m "Merge week02/calibration: complete calibration exercise"
git push origin main
```

`--no-ff` preserves a visible merge point even when a fast-forward is possible.
If conflicts occur, resolve and validate them before completing the merge and
pushing. Do not run both merge procedures as separate ways to finish the same week.

## Begin the next week

After the previous week has merged and local `main` is updated:

```bash
git switch main
git pull --ff-only
git switch -c week03/topic
```

Replace `topic` with the actual assignment topic. Create its directory, import and
commit the untouched starter code, then repeat the same workflow. Each new branch
includes the exercises already merged into `main`; work for the new week belongs
in its own directory. Avoid beginning a new week from the previous week's
unfinished branch unless that dependency is intentional.

## Inspect the original exercise and your changes

These commands inspect history without changing your current files:

```bash
git log --oneline --graph --all
git log --oneline -- weeks/week02_calibration/
```

Find the hash of `chore(week02): add original calibration starter code`. Substitute
that hash for `STARTER_COMMIT` below:

```bash
git show --stat STARTER_COMMIT
git diff STARTER_COMMIT HEAD -- weeks/week02_calibration/
```

The diff compares the original starter snapshot with your current committed
version. GitHub's commit pages also let you browse files at an earlier snapshot.
There is no need to reset or overwrite your working files to view the unsolved code.

## Data, environments, and results

The root `.gitignore` covers common local environments, caches, notebook
checkpoints, build directories, credentials, and generated outputs. It does not
ignore all images, notebooks, or calibration parameters.

| Content | Suggested handling |
| --- | --- |
| Exercise source, notebooks, dependency manifests | Commit |
| Small required calibration images or fixtures, when shareable | Commit in the supplied layout or a documented fixture directory |
| Large downloaded inputs | Keep under the week's `data/raw/` or `data/downloads/`; document acquisition and expected paths |
| Regenerable outputs | Write under the week's `outputs/`; ignored by default |
| Selected small figures and result summaries | Commit deliberately under a tracked path such as `report/` |
| Virtual environments, caches, credentials | Keep local and untracked |

If the starter uses an ignored directory name for required source or deliverables,
adjust the ignore rules deliberately before committing. Do not force-add an
entire ignored directory without reviewing its contents. Preserve attribution and
license notices in supplied material.

## Common setup problems

| Message or situation | What to check |
| --- | --- |
| `remote origin already exists` | Inspect `git remote -v`. Keep the correct existing URL, or deliberately correct it with `git remote set-url origin YOUR_REMOTE_URL`. |
| `Permission denied (publickey)` | Confirm the public key is registered with the intended GitHub account, load its private key with `ssh-add`, and retry `ssh -T git@github.com`. |
| `Repository not found` | Check the owner, repository name, remote URL, and the authenticated account's access. |
| Push rejected because GitHub already has commits | Fetch and inspect the histories; do not force-push. The setup above expects an empty remote. |
| `src refspec main does not match any` | Confirm the initial commit succeeded and that the current branch is named `main`. |
| `git pull --ff-only` refuses | Local and remote history may have diverged. Inspect `git log --oneline --graph --all` before deciding how to reconcile them. |

## Official references

- [Create a GitHub repository](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-new-repository)
- [Add locally hosted code to GitHub](https://docs.github.com/en/migrations/importing-source-code/using-the-command-line-to-import-source-code/adding-locally-hosted-code-to-github)
- [Generate an SSH key on Linux](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent?platform=linux)
- [Add an SSH key to GitHub](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account?platform=linux)
- [Test the SSH connection](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/testing-your-ssh-connection?platform=linux)
- [GitHub merge methods](https://docs.github.com/en/pull-requests/reference/pull-request-merges)
