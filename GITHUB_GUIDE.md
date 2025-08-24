# 🧭 How to Upload Your Project to GitHub (Step-by-Step)

There are **three** easy methods. Choose **any one**.

---

## ✅ Method 1: Web Browser (Easiest – no Git needed)
1. Sign in to GitHub → click **New** repository.
2. Name it: `PhonePe-Transaction-Insights` → click **Create repository**.
3. On the new repo page, click **Add file** → **Upload files**.
4. Drag & drop these files/folders from your computer:
   - `app.py`
   - `README.md`
   - `requirements.txt`
   - `.gitignore`
   - (optional) `docs/`, `sql/`
5. Scroll down → **Commit changes**.

> Repeat the same to upload more files later.

---

## 💻 Method 2: GitHub Desktop (GUI app)
1. Install **GitHub Desktop** (Windows/Mac).
2. **File → New repository** → Name: `PhonePe-Transaction-Insights` → choose your local folder.
3. Copy your project files into that folder.
4. In GitHub Desktop: write a **summary** → click **Commit to main**.
5. Click **Publish repository** to push it to your GitHub account.

---

## 🧑‍💻 Method 3: Git (Command Line)
> Use this if you’re comfortable with terminal/PowerShell.

### One-time setup
```bash
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
```

### Initialize and push
From inside your project folder:
```bash
git init
git branch -M main
git add .
git commit -m "Initial commit: PhonePe Transaction Insights"
git remote add origin https://github.com/<your-username>/PhonePe-Transaction-Insights.git
git push -u origin main
```

### Common fixes
- **remote origin already exists**
  ```bash
  git remote remove origin
  git remote add origin https://github.com/<your-username>/PhonePe-Transaction-Insights.git
  ```
- **rejected: main protected / branch mismatch**
  ```bash
  git fetch origin
  git pull origin main --allow-unrelated-histories
  git push -u origin main
  ```
- **Large files (>100MB)**
  Install Git LFS and track the pattern:
  ```bash
  git lfs install
  git lfs track "*.csv"
  git add .gitattributes
  git add .
  git commit -m "Track large files with LFS"
  git push
  ```

### Update later
```bash
git add .
git commit -m "Update: new charts & queries"
git push
```

---

## 🔐 If asked for a token (2FA enabled)
Create a **Personal Access Token**:
1. GitHub → Settings → Developer settings → **Personal access tokens** → **Tokens (classic)** → **Generate new token**.
2. Scope: `repo` is enough.
3. Use this token **in place of your password** when pushing.

---

## 📦 Recommended project layout
```
PhonePe-Transaction-Insights/
│── app.py
│── requirements.txt
│── README.md
│── .gitignore
│── sql/
│── docs/
│── data/        # keep out of git if large
```

You’re all set! 🚀
