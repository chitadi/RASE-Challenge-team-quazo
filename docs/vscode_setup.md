# 🖥️ VS Code Setup Guide

This guide will help participants with **zero prior experience** install and configure Visual Studio Code (VS Code) for editing and running the challenge code.

---

## 1. Install VS Code
Download and install VS Code for your platform:

- **Windows / macOS / Linux** → [https://code.visualstudio.com/download](https://code.visualstudio.com/download)

---

## 2. Install Recommended Extensions
Open VS Code,
Press `Ctrl+Shift+X` (Windows/Linux) or `Cmd+Shift+X` (Mac), search for the extension name listed below then click **Install**.


- 🐍 **Python** (Microsoft) – Python syntax highlighting, linting, debugging.  
- 📦 **Pylance** – Fast IntelliSense and type checking.  
- 🐳 **Docker** – Manage Docker containers and images directly from VS Code. 
- **Dev Containers** - Open any folder or repository inside a Docker container and take advantage of Visual Studio Code's full feature set.
- **Remote Development**
An extension pack that lets you open any folder in a container, on a remote machine, or in WSL and take advantage of VS Code's full feature set.
- **Remote Explorer**
View remote machines for SSH
- **Jupyter** - Jupyter notebook support
- 📝 **Markdown All in One** – Preview and edit Markdown (`README.md`) files easily.  


---

## 3. Open the Docker container Project Folder 
1. In VS Code, open the Command Palette (`Ctrl+Shift+P` or `Cmd+Shift+P`).

2. Search for "Attach to Running Container".

3. Select our container (e.g., rase2026-baseline).

4. VS Code will reload, and you’ll now be working inside the container.


5. Once connected to the container, go to File → Open Folder→ /src

6. The Explorer panel will now show the container’s project files.


Before proceeding, press ```Ctrl+ ` ``` to activate the terminal within VS code before continuing with the [training code](../README.md#4-run-the-training-code-in-the-container).


