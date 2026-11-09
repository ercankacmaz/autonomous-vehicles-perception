# Autonomous Vehicles: Perception

## Project context

This repository contains Ercan Kaçmaz's coding exercises for the Autonomous
Vehicles: Perception lectures. The first planned exercise is Week 02: calibration.
Read `README.md` for repository setup, naming conventions, and the weekly workflow.

## Learning and collaboration

- Prioritize understanding the theory, implementation, and results.
- When asked to explain an exercise, explain the mathematical model, assumptions,
  relevant file paths, code structure, and a small number of meaningful steps.
- When the user intends to implement the solution, provide guidance and review
  without filling in the entire exercise. Implement code when the user asks for it.
- Preserve the user's work and approach. Explain a proposed correction before
  making a substantial change to an existing solution.
- Read the assignment and supplied starter documentation before choosing an
  algorithm, dependency, or expected result. Do not invent assignment requirements.
- Keep communication, documentation, code identifiers, and commit messages in
  English unless the user requests another language.

## Repository organization

- Use one repository for the course and one directory per exercise week:
  `weeks/week02_calibration/`, followed by `weeks/weekNN_topic/`.
- Preserve the supplied starter structure inside the week's directory, including
  filenames, function signatures, notebook cells, relative paths, and TODOs.
- If the course tooling requires a different layout, follow its requirements and
  document the adjustment instead of forcing this suggested structure.
- Keep week-specific code, notes, small required input fixtures, and dependencies
  with that exercise. Introduce shared utilities only when actual reuse warrants it.
- Do not initialize nested Git repositories when importing exercise material.
- Do not add frameworks, package managers, CI, or dependency files before the
  supplied code establishes a need for them.

## Git workflow

- `main` holds repository setup and completed exercises.
- Use one working branch per week, named `weekNN/topic`; the first is
  `week02/calibration`.
- Create each weekly branch from an up-to-date `main`. If weeks must overlap,
  keep their changes separate and reconcile shared changes before merging.
- Before modifying files, inspect the current branch, working-tree status, and
  applicable instructions. Do not overwrite, discard, or commit unrelated changes.
- For a new week, the first exercise commit must contain the original, unsolved
  starter code. Do not combine the import with fixes, formatting, dependency
  changes, completed TODOs, or solution documentation.
- Review which supplied assets belong in Git before the starter commit. Preserve
  required source and small fixtures; document separately downloaded datasets.
  Check ignored paths if a required starter file is missing from the staged set.
- Use subsequent commits on the same branch for meaningful implementation,
  validation, and documentation steps. Intermediate work is allowed on the branch;
  do not describe incomplete work as finished.
- Prefer focused messages such as:
  - `chore(week02): add original calibration starter code`
  - `feat(week02): implement camera calibration`
  - `fix(week02): correct point ordering`
  - `docs(week02): explain validation results`
- Review the staged diff and run relevant checks before committing. Stage explicit
  paths so unrelated work is not included accidentally.
- Push the branch after its starter commit and useful progress checkpoints when
  the user has requested those Git operations.
- Merge a completed week through a pull request using **Create a merge commit**,
  or use `git merge --no-ff` locally. Preserve the individual starter and solution
  commits; do not squash or rewrite published history unless the user requests it.
- After a GitHub merge, update local `main` before starting the next week.
  Branch deletion is optional; deleting a merged branch does not remove its
  commits from `main`.
- A request for explanations or file preparation is not a request to initialize,
  commit, push, or merge. When the user authorizes a Git workflow, complete its
  authorized steps without repeatedly asking for the same permission.
- Do not force-push, reset away changes, amend published commits, or change global
  Git settings without a specific user instruction.

## Implementation and perception conventions

- Follow the assignment's language, libraries, APIs, and conventions. The starter
  code has not yet been supplied; do not assume Python, C++, ROS, or OpenCV.
- Prefer readable, direct solutions that match the lecture material.
- For mathematical code, state array shapes, coordinate frames, units, indexing,
  angle units, and transformation direction where relevant.
- For calibration, make 2D/3D point correspondence, image dimensions, calibration
  target geometry, and any distortion model explicit when they apply.
- Keep units consistent and preserve the assignment's expected output format.
- Use relative paths or configurable inputs instead of machine-specific absolute
  paths in exercise code. Document the working directory for run commands.
- Record package/runtime versions that affect reproducibility. Seed randomized
  procedures when appropriate and explain any remaining nondeterminism.

## Validation and completion

- Run supplied checks and the actual exercise entry point where practical.
- Use small, meaningful numerical checks for changed mathematical behavior.
  Avoid tests that merely duplicate the implementation.
- For calibration, validate relevant outputs and reprojection behavior if required
  by the assignment. Do not invent acceptable error thresholds or claim success
  solely because the program runs.
- Record the exact commands, observed results, and limitations. If dependencies,
  data, display access, or hardware prevent execution, say so explicitly.
- Before marking a week complete, update its documentation with setup, inputs,
  execution instructions, approach, and results. Preserve supplied README content;
  extend it or add a separate notes file when appropriate.
- Mark the root exercise table complete only after the solution and its validation
  are ready. Do not claim that a branch has merged until the merge is verified.

## Data and generated files

- Use the root `.gitignore`; extend it only for concrete project needs.
- Keep credentials, virtual environments, caches, build outputs, and bulk datasets
  out of Git. Store large downloaded inputs in `data/raw/` or `data/downloads/`
  under the relevant week, and document how to obtain them.
- Generated `outputs/` directories are ignored. Put deliberately selected, small
  report figures or result summaries in a tracked location such as `report/`.
- Do not ignore all images, notebooks, numerical arrays, or calibration files:
  small reproducible fixtures and requested deliverables may need to be tracked.
- Retain supplied attribution and license notices. Keep repository visibility and
  distribution of course material consistent with the user's course permissions.
