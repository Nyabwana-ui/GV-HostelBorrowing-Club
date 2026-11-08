# Green View Borrowing Club

A responsive web application built around the hostel borrowing OOP system in `inclass.py`.

## Run

From the project folder, using Node.js/npm:

```powershell
npm install
npm run dev
```

`npm install` installs the Python backend dependencies into `.venv`. Open http://127.0.0.1:5000 in the browser.

To create or repair the virtual environment manually:

```powershell
py -m venv .venv
``` 

## Project structure

```text
backend/   Flask API and OOP domain model
frontend/  HTML, CSS, and JavaScript
run.py     Application launcher
```

## Demo accounts

| Role | Username | Password |
|---|---|---|
| Administrator | `admin` | `admin123` |
| Member | `brian` | `pass1` |
| Member | `grace` | `pass2` |
| Member | `simon` | `pass3` |

Demo data resets whenever the server restarts.
