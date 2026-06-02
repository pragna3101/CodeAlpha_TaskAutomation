# CodeAlpha Python Programming Internship - Task 3: Task Automation Script

## 📝 Project Overview
This repository contains a suite of three **Task Automation Scripts** developed in Python, designed to automate common real-world administrative and web tasks:
1. **File Organizer (`move_images.py`)**: Organizes image assets by moving all JPEG/JPG files from a source folder into an organized destination folder.
2. **Email Extractor (`email_extractor.py`)**: Uses robust regular expressions (`re`) to parse any text file, extract all valid email addresses, deduplicate them, and write a clean list to a file.
3. **Webpage Title Scraper (`webpage_title_scraper.py`)**: Crawls a target URL, scrapes its HTML content using `BeautifulSoup`, extracts the webpage's `<title>` tag, and exports it to a text file.

## 🎯 Objective
This project demonstrates standard task automation practices in Python using both built-in utilities (`os`, `shutil`, `re`) and highly popular open-source packages (`requests`, `beautifulsoup4`).

---

## ✨ Features

### Script 1: Image Organizer (`move_images.py`)
- Automatically filters out files with `.jpg` and `.jpeg` extensions case-insensitively.
- Safely moves files using `shutil.move` without deleting non-target files.
- Automatically handles directory creation for target folder if missing.

### Script 2: Regex Email Extractor (`email_extractor.py`)
- Employs a robust, industry-standard email matching regular expression pattern.
- Deduplicates matching emails automatically using set collections.
- Outputs extracted emails both to the command terminal and a sorted `.txt` report file.

### Script 3: Web Scraper (`webpage_title_scraper.py`)
- Performs network requests using the HTTP standard client (`requests`).
- Uses custom headers (User-Agent emulation) to prevent scraping-detection blocks.
- Employs `BeautifulSoup` parsing to extract HTML `<title>` tags cleanly.
- Implements comprehensive network exception handling for connection timeouts, DNS resolution issues, or HTTP failure codes.

---

## 🛠️ Technologies Used
- **Language**: Python 3
- **Core Modules**: `os`, `shutil`, `re`
- **External Dependencies**: `requests`, `beautifulsoup4`

---

## 📂 Folder Structure
```text
CodeAlpha_TaskAutomation/
│
├── move_images.py              # Script 1: Image Mover & Organizer
├── email_extractor.py          # Script 2: Regex Email Extractor
├── webpage_title_scraper.py    # Script 3: Web Scraper (Title Grabber)
├── requirements.txt            # Python External Dependencies
├── README.md                   # Project Documentation
├── screenshots/                # Directory containing sample run previews
│
└── sample_data/                # Out-of-the-box local testing dataset
    ├── input_emails.txt        # Sample text file with emails mixed in
    └── source_dir/             # Sample source directory with dummy files
        ├── image1.jpg
        ├── image2.jpg
        └── notes.txt
```

---

## 🚀 Installation & Getting Started

### Prerequisites
- **Python**: Make sure Python 3.x is installed.
- **Pip**: Verify pip (Python Package Installer) is ready.

### Installation Steps
1. Navigate to the automation repository:
   ```bash
   cd CodeAlpha_TaskAutomation
   ```
2. Install required third-party libraries for the web scraper using pip:
   ```bash
   pip install -r requirements.txt
   ```

---

## 🎮 How to Run

### 1. Run the Image Organizer
Move files from the included `sample_data/source_dir` to `sample_data/dest_dir`:
```bash
python move_images.py
```
*(Press Enter when prompted to use default settings)*

### 2. Run the Email Extractor
Extract sample emails from `sample_data/input_emails.txt`:
```bash
python email_extractor.py
```
*(Press Enter when prompted to use default settings)*

### 3. Run the Webpage Title Scraper
Scrape the default test webpage title (`https://example.com`):
```bash
python webpage_title_scraper.py
```
*(Press Enter when prompted to use default settings)*

---

## 📊 Sample Output Previews

### Image Organizer (`move_images.py`)
```text
==================================================
      IMAGE ORGANIZER AUTOMATION SCRIPT         
==================================================

[+] Active Source Directory:      D:\GITHUB\CODEALPHA\CodeAlpha_TaskAutomation\sample_data\source_dir
[+] Active Destination Directory: D:\GITHUB\CODEALPHA\CodeAlpha_TaskAutomation\sample_data\dest_dir

[✔] Moved: image1.jpg -> dest_dir
[✔] Moved: image2.jpg -> dest_dir
--------------------------------------------------
                 SUMMARY                       
--------------------------------------------------
Total JPG/JPEG files moved successfully: 2
Non-JPG files left untouched:             1
--------------------------------------------------
```

### Email Extractor (`email_extractor.py`)
```text
==================================================
        AUTOMATED EMAIL EXTRACTOR SCRIPT        
==================================================

[+] Reading Input File:  D:\GITHUB\CODEALPHA\CodeAlpha_TaskAutomation\sample_data\input_emails.txt
[+] Output Destination:  D:\GITHUB\CODEALPHA\CodeAlpha_TaskAutomation\extracted_emails.txt

[+] Found 5 email(s) total (5 unique).

Extracted Emails:
  - coordinators@codealpha.org
  - hr-department@codealpha.com
  - jobs.recruit@company-talent.co.uk
  - john.doe@sub.domain.com
  - support@codealpha.org

[✔] Success: Saved unique list to 'D:\GITHUB\CODEALPHA\CodeAlpha_TaskAutomation\extracted_emails.txt'
```

### Webpage Title Scraper (`webpage_title_scraper.py`)
```text
==================================================
       WEB SCRAPER: WEBPAGE TITLE EXTRACTOR     
==================================================

[+] Scrape Target URL:  https://example.com
[+] Output Destination: D:\GITHUB\CODEALPHA\CodeAlpha_TaskAutomation\scraped_title.txt
[~] Sending request, please wait...

[✔] Webpage Title Found: "Example Domain"
[✔] Success: Saved details to 'D:\GITHUB\CODEALPHA\CodeAlpha_TaskAutomation\scraped_title.txt'
```

---

## 📈 Future Improvements
- **Scheduler Integration**: Wrap the scripts in an automated scheduling loop (e.g. run every day at 12:00 PM) using built-in OS utilities like Windows Task Scheduler or Cron.
- **Support for More File Formats**: Expand `move_images.py` to organize multiple file categories (e.g., move `.pdf` to documents, `.mp4` to videos, `.zip` to compressed).
- **Deep Web Crawling**: Expand `webpage_title_scraper.py` into a spider scraper that crawls all anchors (`<a>` tags) on a website and indexes all sub-page titles recursively.
- **Log System**: Set up a persistent audit log file (`automation.log`) using Python's built-in `logging` module to track successes and errors over time.
