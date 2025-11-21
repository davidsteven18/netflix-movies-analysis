# 📤 Step-by-Step Guide: Uploading Your Project to GitHub

## Prerequisites Checklist ✅

Before starting, make sure you have:
- [ ] Git installed on your computer ([Download here](https://git-scm.com/downloads))
- [ ] A GitHub account ([Sign up here](https://github.com/join))
- [ ] Visual Studio Code installed

---

## Part 1: Prepare Your Project 📋

### Step 1: Review Your Files
Your project should now contain:
- ✅ `README.md` - Project documentation
- ✅ `Investigating_Netflix_movies.py` - Main analysis script
- ✅ `netflix_data.csv` - Dataset
- ✅ `requirements.txt` - Python dependencies
- ✅ `.gitignore` - Files to exclude from Git
- ✅ `notebook.ipynb` - Jupyter notebook (optional)

### Step 2: Customize the README
1. Open `README.md`
2. Replace placeholders:
   - `yourusername` → Your GitHub username
   - `Your Name` → Your actual name
   - Add your LinkedIn profile link
3. Save the file (Ctrl+S)

---

## Part 2: Initialize Git Repository 🔧

### Step 3: Open Terminal in VS Code
1. In VS Code, click **Terminal** → **New Terminal**
2. Make sure you're in your project folder:
   ```bash
   pwd
   ```
   Should show: `C:/Users/steve/Documents/David Steven H/DataScienceProjects/NetflixProject`

### Step 4: Configure Git (First-time setup only)
If you haven't used Git before, configure your identity:
```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

### Step 5: Initialize Git Repository
```bash
git init
```
Expected output: `Initialized empty Git repository in ...`

### Step 6: Add Files to Staging Area
```bash
git add .
```
This adds all files (respecting `.gitignore`)

### Step 7: Check Status (Optional)
```bash
git status
```
You should see all your files listed in green (ready to commit)

### Step 8: Make Your First Commit
```bash
git commit -m "Initial commit: Netflix movies analysis project"
```

---

## Part 3: Create GitHub Repository 🌐

### Step 9: Go to GitHub
1. Open your browser and go to [github.com](https://github.com)
2. Log in to your account

### Step 10: Create New Repository
1. Click the **+** icon (top-right) → **New repository**
2. Fill in the details:
   - **Repository name**: `netflix-movies-analysis` (or your preferred name)
   - **Description**: "Data analysis project investigating Netflix movie trends from the 1990s"
   - **Visibility**: Choose **Public** (for portfolio)
   - ❌ **DO NOT** initialize with README (you already have one)
   - ❌ **DO NOT** add .gitignore or license yet
3. Click **Create repository**

### Step 11: Copy Repository URL
GitHub will show you a page with setup instructions. Copy the repository URL:
```
https://github.com/yourusername/netflix-movies-analysis.git
```

---

## Part 4: Push to GitHub 🚀

### Step 12: Connect Local Repository to GitHub
Back in VS Code terminal, run:
```bash
git remote add origin https://github.com/yourusername/netflix-movies-analysis.git
```
Replace `yourusername` and repository name with yours.

### Step 13: Rename Branch to 'main' (if needed)
```bash
git branch -M main
```

### Step 14: Push Your Code
```bash
git push -u origin main
```

You may be prompted to log in:
- Enter your GitHub username
- For password, use a **Personal Access Token** (not your account password)

**How to create a Personal Access Token:**
1. Go to GitHub → Settings → Developer settings → Personal access tokens → Tokens (classic)
2. Generate new token
3. Select scope: `repo` (full control of private repositories)
4. Copy the token and use it as your password

### Step 15: Verify Upload
1. Go back to your GitHub repository page
2. Refresh the page
3. You should see all your files! 🎉

---

## Part 5: Making Updates Later 🔄

When you make changes to your project:

### 1. Check what changed
```bash
git status
```

### 2. Add changed files
```bash
git add .
```
Or add specific files:
```bash
git add filename.py
```

### 3. Commit changes
```bash
git commit -m "Description of what you changed"
```

### 4. Push to GitHub
```bash
git push
```

---

## Part 6: Using VS Code Git Interface (Alternative) 🖱️

VS Code has a built-in Git interface:

### Visual Method:
1. Click the **Source Control** icon (left sidebar, looks like a branch)
2. Review changes in the list
3. Click **+** next to files to stage them (or "Stage All Changes")
4. Type a commit message in the text box
5. Click the **✓ Commit** button
6. Click **•••** → **Push** to send to GitHub

---

## Troubleshooting 🔧

### Problem: "fatal: not a git repository"
**Solution**: Make sure you ran `git init` in the correct folder

### Problem: "remote origin already exists"
**Solution**: Remove and re-add:
```bash
git remote remove origin
git remote add origin YOUR_GITHUB_URL
```

### Problem: Authentication failed
**Solution**: Use a Personal Access Token instead of your password

### Problem: ".venv folder being committed"
**Solution**: The `.gitignore` file should prevent this. If not:
```bash
git rm -r --cached .venv
git commit -m "Remove .venv from repository"
git push
```

---

## Best Practices 💡

1. **Commit often** - Make small, focused commits
2. **Write clear commit messages** - Describe what and why
3. **Update README** - Keep documentation current
4. **Don't commit sensitive data** - Check `.gitignore` works
5. **Test before pushing** - Make sure your code runs

---

## Next Steps 🎯

After uploading:
1. ⭐ Add a LICENSE file (MIT is common for open source)
2. 📊 Add visualization images to your README
3. 🔗 Add the GitHub link to your resume/LinkedIn
4. 📝 Write a blog post about your analysis
5. 🎨 Create a GitHub profile README to showcase your work

---

## Useful Git Commands Reference 📚

```bash
# Check status
git status

# View commit history
git log --oneline

# View remote URL
git remote -v

# Pull latest changes from GitHub
git pull

# Create and switch to new branch
git checkout -b feature-branch-name

# Switch back to main branch
git checkout main

# View differences
git diff
```

---

## Resources 📖

- [Git Documentation](https://git-scm.com/doc)
- [GitHub Guides](https://guides.github.com/)
- [Git Cheat Sheet](https://education.github.com/git-cheat-sheet-education.pdf)
- [Markdown Guide](https://www.markdownguide.org/)

---

**Good luck with your portfolio project! 🚀**

If you encounter any issues, check the Troubleshooting section or search for error messages on Google/Stack Overflow.
