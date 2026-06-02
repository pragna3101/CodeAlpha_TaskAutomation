#!/usr/bin/env python3
"""
CodeAlpha Python Internship
Task 3: Task Automation - Script 1: Image Mover & Organizer

Automates moving all JPG and JPEG images from a source directory to a 
designated destination directory. Useful for decluttering folders.
"""

import os
import shutil


def move_jpg_files(source_dir, dest_dir):
    """
    Finds and moves all files with .jpg or .jpeg extensions from source_dir
    to dest_dir. Creates dest_dir if it doesn't already exist.
    """
    # Normalize paths
    source_dir = os.path.abspath(source_dir)
    dest_dir = os.path.abspath(dest_dir)

    print(f"\n[+] Active Source Directory:      {source_dir}")
    print(f"[+] Active Destination Directory: {dest_dir}\n")

    # Verify that source directory exists
    if not os.path.exists(source_dir):
        print(f"[-] Error: Source directory '{source_dir}' does not exist.")
        return

    # Verify that source is indeed a directory
    if not os.path.isdir(source_dir):
        print(f"[-] Error: Path '{source_dir}' is a file, not a directory.")
        return

    # Create destination directory if it doesn't exist
    if not os.path.exists(dest_dir):
        try:
            os.makedirs(dest_dir)
            print(f"[+] Created destination directory: {dest_dir}")
        except Exception as e:
            print(f"[-] Error creating destination directory: {e}")
            return

    # Scan the source directory
    try:
        files = os.listdir(source_dir)
    except Exception as e:
        print(f"[-] Error listing source files: {e}")
        return

    moved_count = 0
    skipped_count = 0

    # Iterate through files and filter JPG/JPEGs
    for filename in files:
        source_filepath = os.path.join(source_dir, filename)
        
        # Skip directories
        if os.path.isdir(source_filepath):
            continue

        # Extract file extension (case-insensitive)
        file_ext = os.path.splitext(filename)[1].lower()

        if file_ext in ['.jpg', '.jpeg']:
            dest_filepath = os.path.join(dest_dir, filename)
            
            try:
                # Move the file
                shutil.move(source_filepath, dest_filepath)
                print(f"[+] Moved: {filename} -> {os.path.basename(dest_dir)}")
                moved_count += 1
            except Exception as e:
                print(f"[-] Failed to move {filename}: {e}")
        else:
            skipped_count += 1

    # Print summary
    print("-" * 50)
    print("                 SUMMARY                       ")
    print("-" * 50)
    print(f"Total JPG/JPEG files moved successfully: {moved_count}")
    print(f"Non-JPG files left untouched:             {skipped_count}")
    print("-" * 50 + "\n")


def main():
    """
    Main controller. Uses default relative folders or prompts user for custom inputs.
    """
    print("=" * 50)
    print("      IMAGE ORGANIZER AUTOMATION SCRIPT         ")
    print("=" * 50)
    
    # Pre-configured default paths for instant out-of-the-box running
    default_source = os.path.join("sample_data", "source_dir")
    default_dest = os.path.join("sample_data", "dest_dir")

    print(f"\nDefault configuration:")
    print(f"  Source:      {default_source}")
    print(f"  Destination: {default_dest}")
    
    choice = input("\nUse default settings? (yes/no) [Default: yes]: ").strip().lower()
    
    if choice in ['n', 'no']:
        # Prompt user for their own custom paths
        source_input = input("Enter path to source directory: ").strip()
        dest_input = input("Enter path to destination directory: ").strip()
        
        if not source_input or not dest_input:
            print("[-] Paths cannot be empty! Reverting to defaults.")
            move_jpg_files(default_source, default_dest)
        else:
            move_jpg_files(source_input, dest_input)
    else:
        move_jpg_files(default_source, default_dest)


if __name__ == "__main__":
    main()
