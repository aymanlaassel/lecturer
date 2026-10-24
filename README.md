# Lecturer 🎓

**Your personal AI tutor, built on Claude Code.**

Give it your professor's slides, PDFs and readings, and it will teach you each topic, quiz you
in the style of your real exam, and write you a cheat sheet, all based on **your** course
materials, with a note on which slide or page each fact came from.

No coding needed. If you can copy-paste a command and drag files into a folder, you can use it.

---

## Part 1: One-time setup (about 10 minutes)

### Step 1: Install Claude Code

Claude Code is the app Lecturer runs inside. It runs in your computer's terminal.

1. **Open the terminal.**
   - **Mac:** press `Cmd + Space`, type `Terminal`, press Enter.
   - **Windows:** open the Start menu, type `PowerShell`, press Enter.
2. **Paste this and press Enter:**

   **Mac / Linux:**
   ```bash
   curl -fsSL https://claude.ai/install.sh | bash
   ```
   **Windows (PowerShell):**
   ```powershell
   irm https://claude.ai/install.ps1 | iex
   ```
3. Close the terminal and open it again, then type `claude` and press Enter. The first time, it
   opens a browser window to sign in with your Claude account. (Claude Code needs a Claude Pro,
   Max, or API plan. See https://claude.com/pricing.)
4. Type `/exit` and press Enter to leave Claude for now.

### Step 2: Install Python (skip if you already have it)

Lecturer uses Python to read PDF, PowerPoint and Word files.

- **Mac:** Python usually comes installed. Check by typing `python3 --version`. If you see a
  version number, you're fine. If not, download it from https://www.python.org/downloads/.
- **Windows:** download it from https://www.python.org/downloads/. During install, **tick the box
  "Add Python to PATH"**.

### Step 3: Install Lecturer

Paste these two commands into the terminal, one at a time, pressing Enter after each:

```bash
claude plugin install lecturer --marketplace aymanlaassel/lecturer
```

```bash
pip3 install pymupdf python-docx python-pptx openpyxl
```

(On Windows, if `pip3` isn't recognized, use `pip` instead.)

You should see `✔ Successfully installed plugin: lecturer@lecturer`. Setup is done.

---

## Part 2: Set up a course (2 minutes per course)

### Step 4: Make a study folder

This is where your courses, notes and quizzes will live. Paste:

```bash
mkdir -p ~/Study && cd ~/Study && claude
```

This creates a folder called `Study` in your home folder and opens Claude inside it.
**Every time you want to study later, run this same line.**

### Step 5: Tell Lecturer about your exam

Inside Claude, type `/lecturer:setup`, then a short name for the course (letters and dashes
only), then paste anything you have about the exam: the professor's email, the syllabus, the
Canvas exam page. For example:

```
/lecturer:setup logic-cs
Hello everyone, our midterm is Monday October 26 in room 114, 45 minutes,
18 multiple choice questions covering Modules 1-9: ...
```

Lecturer creates `Study/courses/logic-cs/` with a `COURSE.md` file holding the exam date,
format and topic list, plus an empty `inbox` folder.

### Step 6: Put your course files in the inbox

Drag and drop your files into `Study/courses/logic-cs/inbox/`. To open that folder:

- **Mac:** in Claude type `! open courses/logic-cs/inbox` and press Enter. Finder opens.
- **Windows:** in Claude type `! explorer courses\logic-cs\inbox` and press Enter.

Good things to put in:
- All the lecture slides (`.pptx` or `.pdf`)
- Practice / mock exams **with answers** (the most useful file of all)
- Old quizzes (print them to PDF from Canvas)
- Textbook chapters or zyBooks sections (print to PDF, or paste the text into a `.txt` file)
- Homework or project handouts

Supported: PDF, PowerPoint, Word, Excel, `.txt`, `.md`, `.csv`.

### Step 7: Load the files

Back in Claude, type:

```
/lecturer:ingest
```

It reads every file and tells you which topics are now covered and which are still missing.

---

## Part 3: Study

Type any of these inside Claude:

| Type this | What you get |
|---|---|
| `/lecturer:exam-info` | When and where the exam is, the format, days left, and a study plan |
| `/lecturer:teach 5` | A full lesson on Module 5: definitions, worked examples, exam traps, quick quiz |
| `/lecturer:teach all` | A lesson for every module, saved as files you can reread |
| `/lecturer:explain converse vs contrapositive` | A short, focused explanation of one thing |
| `/lecturer:quiz 3 4 10` | 10 practice questions on Modules 3 and 4, then grading with explanations |
| `/lecturer:quiz all 18` | A full mock exam in the real format |
| `/lecturer:cheatsheet` | A two-page summary of everything, for the night before |

You don't have to use commands. Just talk to it:

> teach me everything I need to remember from module 7

> I got this practice question wrong, explain why: *(paste the question)*

> what are the most common mistakes on resolution?

Lessons are saved in `Study/courses/<course>/notes/`, quizzes in `quizzes/`, and your quiz
scores are logged so it can focus on your weak spots over time.

---

## Everyday use, in short

```bash
cd ~/Study && claude          # open your study folder
```
```
/lecturer:ingest              # after adding new files
/lecturer:teach 3             # learn
/lecturer:quiz 3              # test yourself
```

---

## FAQ

**Can I have more than one course?**
Yes. Run `/lecturer:setup <another-name>` with that exam's info. When you have several, add the
course name to commands: `/lecturer:teach calc2 3`, `/lecturer:quiz calc2 all`.

**Where do my files go? Is anything uploaded?**
Your files stay on your computer. Only the text Claude needs to answer you is sent to Claude,
the same as if you pasted it into a chat.

**It says `ModuleNotFoundError` or can't read my PDF.**
The Python libraries from Step 3 aren't installed. Run the `pip3 install …` command again, or
just ask Claude: "install the lecturer requirements".

**A PDF came out empty.**
It's probably a scanned image with no real text. Ask Claude to "read this PDF page by page as
images" and it will.

**How do I update Lecturer?**
```bash
claude plugin update lecturer@lecturer
```

**How do I uninstall?**
```bash
claude plugin uninstall lecturer@lecturer
```
Your `Study` folder is untouched.

---

## For developers

```bash
git clone https://github.com/aymanlaassel/lecturer.git
cd lecturer
claude plugin validate --strict .
claude --plugin-dir .          # load this checkout for one session
```

- `skills/*/SKILL.md`: the slash commands
- `rules/TUTOR.md`: the tutor persona and rules every skill follows
- `scripts/ingest.py`: PDF / PPTX / DOCX / XLSX to markdown extraction
- `templates/COURSE.md`: blank course file; `examples/COURSE.logic-cs.md`: a filled one

Bump `version` in `.claude-plugin/plugin.json` before pushing a release, or installed users
won't receive the update.

## License

MIT
