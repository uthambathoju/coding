```mermaid
%%{
  "theme": "base",
  "themeVariables": {
    "primaryColor": "#f3f4f6",
    "primaryTextColor": "#111827",
    "primaryBorderColor": "#6b7280",
    "lineColor": "#6b7280",
    "secondaryColor": "#dbeafe",
    "tertiaryColor": "#bfdbfe",
    "git0": "#2563eb",
    "git1": "#4f46e5",
    "git2": "#db2777",
    "git3": "#f59e0b",
    "git4": "#16a34a",
    "git5": "#ef4444",
    "commitLabelColor": "#111827",
    "commitLabelBackground": "#ffffff",
    "commitLabelFontSize": "12px",
    "tagLabelFontSize": "12px",
    "tagLabelColor": "#ffffff"
  }
}%%
gitGraph
    %% --- Initial Setup: Define the main 'prod' and 'develop' branches ---
    commit id: "v1.0.0" type: HIGHLIGHT
    branch develop
    checkout develop
    commit id: "Initial Develop"

    %% --- SCENARIO 1: A new feature is developed ---
    %% Rule: New branches are created from develop.
    branch feature/user-login
    checkout feature/user-login
    commit id: "feat: Add login UI"
    commit id: "feat: Implement auth logic"
    
    %% Rule: Raise a PR from the working branch to develop.
    checkout develop
    merge feature/user-login id: "PR #1" tag: "Feature Complete"
    
    %% Rule: Conduct integration testing using develop.
    commit id: "test: Pass integration tests"
    
    %% --- SCENARIO 2: A bugfix is developed in parallel ---
    branch bugfix/css-issue
    checkout bugfix/css-issue
    commit id: "fix: Correct button alignment"
    checkout develop
    merge bugfix/css-issue id: "PR #2" tag: "Bugfix Merged"
    
    %% --- SCENARIO 3: Promotion to Production ---
    %% Rule: After successful testing, raise a PR from develop to prod.
    checkout main
    %% Renaming the default 'main' branch to 'prod' for clarity
    branch prod
    checkout prod
    merge develop id: "PR #3 (Release)" tag: "v1.1.0" type: HIGHLIGHT
    
    %% --- SCENARIO 4: Sanity Check / Hotfix Sync ---
    %% This scenario shows a commit on prod that is not in develop, triggering the sanity check rule.
    %% This typically happens after a hotfix.
    commit id: "hotfix: Critical security patch" type: REVERSE
    tag "v1.1.1"
    
    %% Rule: If there are commit differences, raise a PR from prod to develop.
    checkout develop
    merge prod id: "PR #4 (Sync Hotfix)"
```
