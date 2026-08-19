# Moduler-Packager

<div align="center">

# 🧰 Multi-Utility Toolkit

**A single command-line hub for everyday date-time, math, random-data, UUID, and file-handling tasks — built entirely with Python's standard library.**

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)
![No Dependencies](https://img.shields.io/badge/dependencies-none-brightgreen)
![License](https://img.shields.io/badge/license-MIT-lightgrey)
![Platform](https://img.shields.io/badge/platform-CLI-orange)

</div>

---

## 📖 Table of Contents

- [Overview](#-overview)
- [Features](#-features)
- [Project Structure](#-project-structure)
- [Requirements](#-requirements)
- [Getting Started](#-getting-started)
- [Usage Walkthrough](#-usage-walkthrough)
- [Notes & Tips](#-notes--tips)
- [Contributing](#-contributing)
- [License](#-license)

---

## 🔎 Overview

**Multi-Utility Toolkit** is a lightweight, menu-driven CLI application designed to bundle several everyday utilities into one place — no need to jump between scripts. Whether you need to check the difference between two dates, calculate compound interest, generate a secure password, or quickly read/write a file, this toolkit has you covered.

It's built entirely on Python's **built-in modules** (`datetime`, `time`, `math`, `random`, `uuid`), so there's zero setup — just clone and run.

---

## ✨ Features

| Category | What You Can Do |
|---|---|
| 🕒 **Datetime & Time** | View current date/time • Find difference between two dates • Format dates • Stopwatch • Countdown timer |
| ➗ **Mathematical Operations** | Factorial • Compound interest • Trigonometric calculations • Area of geometric shapes |
| 🎲 **Random Data Generation** | Random number • Random number list • Secure random password • Random OTP |
| 🆔 **UUID Generator** | Generate a universally unique identifier |
| 📁 **File Operations** | Create • Write • Read • Append files |
| 🔍 **Module Explorer** | Inspect available attributes/functions of `math`, `random`, `datetime`, `time`, `uuid` via `dir()` |

---

## 📁 Project Structure

```
multi-utility-toolkit/
├── main.py                   # Entry point — drives all menus and navigation
└── utilities/
    ├── file_operations.py    # create_file, write_file, read_file, append_file
    └── math_operations.py    # factorial, compound_interest, trigonometric_calculations, area_of_shapes
```

---

## 🛠️ Requirements

- **Python 3.x**
- No external/third-party packages — only Python's standard library is used

---

## 🚀 Getting Started

**1. Clone the repository**
```bash
git clone https://github.com/<your-username>/multi-utility-toolkit.git
cd multi-utility-toolkit
```

**2. Run the toolkit**
```bash
python main.py
```

That's it — no `pip install`, no configuration. You're ready to go. ✅

---

## 🧭 Usage Walkthrough

When you launch the app, you'll see the main menu:

```
============================
 Welcome to Multi-Utility Toolkit
============================
1. Datetime and Time Operations
2. Mathematical Operations
3. Random Data Generation
4. Generate Unique Identifiers (UUID)
5. File Operations (Custom Module)
6. Explore Module Attributes (dir())
7. Exit
```

- Type the **number** of the option you want and press **Enter**.
- Each category (Datetime, Math, Random, File) opens its **own sub-menu** — select the last option there to go **"Back to Main Menu"**.
- Choose **7** anytime from the main menu to exit the program.

---

## 📝 Notes & Tips

- 📅 Always enter dates in **`YYYY-MM-DD`** format to avoid errors.
- ⏱️ The countdown timer and stopwatch run in **real time** — expect live terminal updates.
- 📂 Make sure the `utilities/` folder (with `file_operations.py` and `math_operations.py`) stays alongside `main.py`, or you'll hit an import error.
- 🔐 Generated passwords/OTPs are for casual use — not intended for production-grade security systems.

---

## 🤝 Contributing

Contributions are welcome! To contribute:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/your-feature`)
3. Commit your changes (`git commit -m "Add: your feature"`)
4. Push to your branch and open a Pull Request

Ideas like new math operations, additional random generators, better error handling, or UI/UX polish are all appreciated.

---

## 📄 License

This project is open-source and free to use, modify, and distribute under the **MIT License**.

---

<div align="center">
Made with 🐍 Python — no dependencies, no hassle.
</div>
