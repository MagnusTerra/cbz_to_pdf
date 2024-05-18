# CBZ to PDF Converter

This program converts CBZ (Comic Book Archive) files into PDF files. It uses Ghostscript to optimize the resulting PDF file size.

## Description

cbz_to_pdf Converter is script tool that simplifies the process of converting comic book archives (CBZ files) into easily shareable and readable PDF files. Ghostscript is used to ensure the PDF files are optimized for size without compromising quality.

## Prerequisites

- Python 3.x
- Ghostscript

## Installation
```shell
pip install -r requirements.txt
```

### Ghostscript Installation

#### Windows

1. **Download Ghostscript**:
   - Visit the [Ghostscript download page](https://www.ghostscript.com/download.html).
   - Download the appropriate installer for Windows (64-bit or 32-bit).

2. **Install Ghostscript**:
   - Run the downloaded installer and follow the installation instructions.

3. **Add Ghostscript to the System PATH**:
   - Open the Start Menu, search for "Environment Variables", and select "Edit the system environment variables".
   - In the System Properties window, click the "Environment Variables..." button.
   - In the Environment Variables window, find the "Path" variable in the "System variables" section and select it, then click "Edit...".
   - Click "New" and add the path to the Ghostscript `bin` directory (e.g., `C:\Program Files\gs\gs10.03.0\bin`).
   - Click "OK" to close all dialog boxes.

4. **Verify the Installation**:
   - Open a Command Prompt and type `gswin64c -v` (or `gswin32c -v` for the 32-bit version).
   - You should see output displaying the Ghostscript version.
   
5. **Create an Alias in PowerShell**:
   - Open a Command Prompt and type `gswin64c -v` (or `gswin32c -v` for the 32-bit version).
   - You should see output displaying the Ghostscript version.

Based on the output you provided, it seems that the Ghostscript path (`C:\Program Files\gs\gs10.03.0\bin`) is included in your PowerShell PATH. However, the `gs` command is still not recognized. Here are a few more steps to resolve this issue:

#### Create an Alias in PowerShell


1. Navigate to the Ghostscript `bin` directory:

   ```powershell
   cd "C:\Program Files\gs\gs10.03.0\bin"
   ```


2. List the files to confirm the executable name:
   ```powershell
   Get-ChildItem
   ```

**1. Create an Alias in PowerShell**.
			If the executable is not `gs.exe`, create an alias for convenience.

**2. If the executable is `gswin64c.exe`, create an alias in PowerShell**:
   ```powershell
   Set-Alias -Name gs -Value "C:\Program Files\gs\gs10.03.0\bin\gswin64c.exe"
   ```

**3. Test the alias:**
   ```powershell
   gs -v
   ```

**4. Add the Alias to Profile for Persistence:**
To make the alias persistent across PowerShell sessions, add it to your PowerShell profile.

1. Open the PowerShell profile script:
   ```powershell
   if (!(Test-Path -Path $PROFILE)) {
       New-Item -ItemType File -Path $PROFILE -Force
   }
   notepad $PROFILE
   ```

2. Add the alias command to the profile:
   ```powershell
   Set-Alias -Name gs -Value "C:\Program Files\gs\gs10.03.0\bin\gswin64c.exe"
   ```

3. Save and close the file.

4. Restart PowerShell and test the `gs` command:
   ```powershell
   gs -v
   ```

** 5. Verify Execution Policy**
Ensure the execution policy allows for the script in the profile to run:

1. Check the current execution policy:
   ```powershell
   Get-ExecutionPolicy
   ```

2. Set the execution policy to RemoteSigned if necessary:
   ```powershell
   Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
   ```


#### macOS

1. **Install Homebrew (if not already installed)**:
   ```bash
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   ```

2. **Update Homebrew**:
   ```bash
   brew update
   ```

3. **Install Ghostscript**:
   ```bash
   brew install ghostscript
   ```

4. **Verify the Installation**:
   ```bash
   gs --version
   ```

#### Linux

##### Ubuntu/Debian

1. **Update the package list**:
   ```bash
   sudo apt update
   ```

2. **Install Ghostscript**:
   ```bash
   sudo apt install ghostscript
   ```

3. **Verify the Installation**:
   ```bash
   gs --version
   ```

##### Fedora

1. **Update the package list**:
   ```bash
   sudo dnf check-update
   ```

2. **Install Ghostscript**:
   ```bash
   sudo dnf install ghostscript
   ```

3. **Verify the Installation**:
   ```bash
   gs --version
   ```

##### Arch Linux

1. **Update the package list** (if necessary):
   ```bash
   sudo pacman -Syu
   ```

2. **Install Ghostscript**:
   ```bash
   sudo pacman -S ghostscript
   ```

3. **Verify the Installation**:
   ```bash
   gs --version
   ```

### Example
```shell
python main.py 
```

```bash
Menu
1. Add the cbz file
2. Add the cbz file and the output directory
3. reduce pdf size
4. cbz to pdf and reduce its size
5. Exit
Enter your choice: 
```

