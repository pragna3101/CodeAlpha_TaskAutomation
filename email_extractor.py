#!/usr/bin/env python3
"""
CodeAlpha Python Internship
Task 3: Task Automation - Script 2: Email Extractor

Automates searching for all valid email addresses inside a raw text file
using regular expressions, removing duplicates, and saving them to an output file.
"""

import os
import re

# Standard robust regular expression for matching valid email addresses
EMAIL_REGEX = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'


def extract_emails_from_file(input_filepath, output_filepath):
    """
    Reads content from input_filepath, extracts all valid unique emails
    using regex, and writes the sorted unique results to output_filepath.
    """
    input_filepath = os.path.abspath(input_filepath)
    output_filepath = os.path.abspath(output_filepath)

    print(f"\n[+] Reading Input File:  {input_filepath}")
    print(f"[+] Output Destination:  {output_filepath}\n")

    # Verify input file exists
    if not os.path.exists(input_filepath):
        print(f"[-] Error: Input file '{input_filepath}' does not exist.")
        return

    # Verify input is indeed a file
    if not os.path.isfile(input_filepath):
        print(f"[-] Error: Path '{input_filepath}' is a directory, not a file.")
        return

    # Read content from the input file
    try:
        with open(input_filepath, 'r', encoding='utf-8') as file:
            content = file.read()
    except Exception as e:
        print(f"[-] Error reading file: {e}")
        return

    # Apply regex to find all emails
    found_emails = re.findall(EMAIL_REGEX, content)

    if not found_emails:
        print("[-] No email addresses found in the input file.")
        return

    # Deduplicate by converting to set and sorting alphabetically
    unique_emails = sorted(list(set(found_emails)))

    print(f"[+] Found {len(found_emails)} email(s) total ({len(unique_emails)} unique).")

    # Print matching list to console
    print("\nExtracted Emails:")
    for email in unique_emails:
        print(f"  - {email}")

    # Write unique emails to output file
    try:
        with open(output_filepath, 'w', encoding='utf-8') as output_file:
            for email in unique_emails:
                output_file.write(email + '\n')
        print(f"\n[+] Success: Saved unique list to '{output_filepath}'\n")
    except Exception as e:
        print(f"[-] Error writing to output file: {e}")


def main():
    """
    Main controller. Uses default relative folders or prompts user for custom inputs.
    """
    print("=" * 50)
    print("        AUTOMATED EMAIL EXTRACTOR SCRIPT        ")
    print("=" * 50)

    # Pre-configured default paths
    default_input = os.path.join("sample_data", "input_emails.txt")
    default_output = "extracted_emails.txt"

    print(f"\nDefault configuration:")
    print(f"  Input File:  {default_input}")
    print(f"  Output File: {default_output}")

    choice = input("\nUse default settings? (yes/no) [Default: yes]: ").strip().lower()

    if choice in ['n', 'no']:
        input_input = input("Enter path to input text file: ").strip()
        output_input = input("Enter path to save output emails: ").strip()

        if not input_input or not output_input:
            print("[-] Paths cannot be empty! Reverting to defaults.")
            extract_emails_from_file(default_input, default_output)
        else:
            extract_emails_from_file(input_input, output_input)
    else:
        extract_emails_from_file(default_input, default_output)


if __name__ == "__main__":
    main()
