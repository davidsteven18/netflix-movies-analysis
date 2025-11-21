# 🚀 Quick Start: GitHub Upload Commands

Copy and paste these commands in order in your VS Code terminal.

---

## ⚡ One-Time Setup (First time using Git)

```bash
# Configure your Git identity
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

---

## 📤 Upload Your Project to GitHub

### 1️⃣ Initialize Git Repository
```bash
git init
```

### 2️⃣ Add All Files
```bash
git add .
```

### 3️⃣ Make First Commit
```bash
git commit -m "Initial commit: Netflix movies analysis project"
```

### 4️⃣ Connect to GitHub
**⚠️ First, create a repository on GitHub.com, then:**

```bash
# Replace 'yourusername' and 'your-repo-name' with actual values
git remote add origin https://github.com/yourusername/your-repo-name.git
```

### 5️⃣ Rename Branch to Main
```bash
git branch -M main
```

### 6️⃣ Push to GitHub
```bash
git push -u origin main
```

---

## 🔄 Update Your Repository (After making changes)

```bash
# 1. Check what changed
git status

# 2. Add changes
git add .

# 3. Commit with message
git commit -m "Describe your changes here"

# 4. Push to GitHub
git push
```

---

## ✅ Verify Everything Worked

```bash
# Check current status
git status

# View commit history
git log --oneline

# Check remote connection
git remote -v
```

---

## 🆘 Common Issues & Fixes

### If you get: "remote origin already exists"
```bash
git remote remove origin
git remote add origin YOUR_URL_HERE
```

### If you need to undo last commit (before push)
```bash
git reset --soft HEAD~1
```

### If you accidentally committed large files
```bash
git rm --cached filename
git commit -m "Remove large file"
```

---

## 📝 Commit Message Tips

Good examples:
- ✅ "Add data visualization charts"
- ✅ "Fix bug in duration calculation"
- ✅ "Update README with new findings"
- ✅ "Refactor code for better readability"

Bad examples:
- ❌ "update"
- ❌ "fixes"
- ❌ "asdf"
- ❌ "changes"

---

**Need detailed instructions? → See `GITHUB_UPLOAD_GUIDE.md`**
