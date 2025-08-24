#!/usr/bin/env python3
"""
File Read & Write Challenge with Error Handling Lab
A comprehensive program demonstrating file operations and exception handling
"""

import os
import sys
from pathlib import Path
from datetime import datetime


class FileProcessor:
    """A robust file processor with comprehensive error handling"""
    
    def __init__(self):
        self.processed_files = []
        self.errors = []
    
    def read_file(self, filename):
        """
        Read a file with comprehensive error handling
        Returns: (success: bool, content: str, error_msg: str)
        """
        try:
            # Convert to Path object for better path handling
            file_path = Path(filename)
            
            # Check if file exists
            if not file_path.exists():
                error_msg = f"❌ File '{filename}' does not exist"
                self.errors.append(error_msg)
                return False, "", error_msg
            
            # Check if it's actually a file (not a directory)
            if not file_path.is_file():
                error_msg = f"❌ '{filename}' is not a file"
                self.errors.append(error_msg)
                return False, "", error_msg
            
            # Check file permissions
            if not os.access(file_path, os.R_OK):
                error_msg = f"❌ Permission denied: Cannot read '{filename}'"
                self.errors.append(error_msg)
                return False, "", error_msg
            
            # Try to read the file with different encodings
            encodings = ['utf-8', 'utf-16', 'latin-1', 'cp1252']
            
            for encoding in encodings:
                try:
                    with open(file_path, 'r', encoding=encoding) as file:
                        content = file.read()
                        print(f"✅ Successfully read '{filename}' using {encoding} encoding")
                        return True, content, ""
                except UnicodeDecodeError:
                    continue
            
            # If all encodings fail
            error_msg = f"❌ Could not decode '{filename}' with any supported encoding"
            self.errors.append(error_msg)
            return False, "", error_msg
            
        except PermissionError:
            error_msg = f"❌ Permission denied accessing '{filename}'"
            self.errors.append(error_msg)
            return False, "", error_msg
        except OSError as e:
            error_msg = f"❌ OS Error reading '{filename}': {e}"
            self.errors.append(error_msg)
            return False, "", error_msg
        except Exception as e:
            error_msg = f"❌ Unexpected error reading '{filename}': {e}"
            self.errors.append(error_msg)
            return False, "", error_msg
    
    def write_file(self, filename, content, backup=True):
        """
        Write content to a file with error handling and optional backup
        Returns: (success: bool, error_msg: str)
        """
        try:
            file_path = Path(filename)
            
            # Create backup if file exists and backup is requested
            if backup and file_path.exists():
                backup_path = file_path.with_suffix(f'{file_path.suffix}.backup')
                try:
                    backup_path.write_text(file_path.read_text(), encoding='utf-8')
                    print(f"📄 Created backup: {backup_path}")
                except Exception as e:
                    print(f"⚠️ Warning: Could not create backup: {e}")
            
            # Create directory if it doesn't exist
            file_path.parent.mkdir(parents=True, exist_ok=True)
            
            # Write the file
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(content)
            
            print(f"✅ Successfully wrote to '{filename}'")
            self.processed_files.append(filename)
            return True, ""
            
        except PermissionError:
            error_msg = f"❌ Permission denied writing to '{filename}'"
            self.errors.append(error_msg)
            return False, error_msg
        except OSError as e:
            error_msg = f"❌ OS Error writing to '{filename}': {e}"
            self.errors.append(error_msg)
            return False, error_msg
        except Exception as e:
            error_msg = f"❌ Unexpected error writing to '{filename}': {e}"
            self.errors.append(error_msg)
            return False, error_msg
    
    def process_text(self, content, operation="word_count"):
        """
        Process text content with various operations
        Available operations: word_count, line_numbers, reverse_lines, uppercase
        """
        try:
            lines = content.splitlines()
            
            if operation == "word_count":
                word_count = len(content.split())
                line_count = len(lines)
                char_count = len(content)
                
                stats = f"""=== FILE STATISTICS ===
Lines: {line_count}
Words: {word_count}
Characters: {char_count}
Characters (no spaces): {len(content.replace(' ', ''))}

=== ORIGINAL CONTENT ===
{content}
"""
                return stats
            
            elif operation == "line_numbers":
                numbered_lines = [f"{i+1:3d}: {line}" for i, line in enumerate(lines)]
                return "=== CONTENT WITH LINE NUMBERS ===\n" + "\n".join(numbered_lines)
            
            elif operation == "reverse_lines":
                reversed_lines = lines[::-1]
                return "=== CONTENT WITH REVERSED LINE ORDER ===\n" + "\n".join(reversed_lines)
            
            elif operation == "uppercase":
                return "=== CONTENT IN UPPERCASE ===\n" + content.upper()
            
            else:
                return f"=== PROCESSED CONTENT (unknown operation: {operation}) ===\n{content}"
                
        except Exception as e:
            return f"❌ Error processing content: {e}\n\nOriginal content:\n{content}"


def get_user_input(prompt, required=True):
    """Get user input with error handling"""
    while True:
        try:
            user_input = input(prompt).strip()
            if required and not user_input:
                print("❌ Input cannot be empty. Please try again.")
                continue
            return user_input
        except KeyboardInterrupt:
            print("\n👋 Program interrupted by user.")
            sys.exit(0)
        except EOFError:
            print("\n❌ Input error occurred.")
            sys.exit(1)


def main():
    """Main program demonstrating file operations and error handling"""
    print("🖋️  FILE READ & WRITE CHALLENGE WITH ERROR HANDLING LAB")
    print("=" * 60)
    
    processor = FileProcessor()
    
    while True:
        try:
            print("\n📋 MENU:")
            print("1. Read and process a file")
            print("2. Create a sample file for testing")
            print("3. View processing summary")
            print("4. Exit")
            
            choice = get_user_input("\nEnter your choice (1-4): ")
            
            if choice == "1":
                # File reading and processing
                filename = get_user_input("📁 Enter filename to read: ")
                
                print(f"\n🔄 Attempting to read '{filename}'...")
                success, content, error_msg = processor.read_file(filename)
                
                if not success:
                    print(error_msg)
                    continue
                
                print("\n📊 Choose processing operation:")
                print("1. Word/Line/Character count")
                print("2. Add line numbers")
                print("3. Reverse line order")
                print("4. Convert to uppercase")
                
                op_choice = get_user_input("Enter operation (1-4): ")
                
                operations = {
                    "1": "word_count",
                    "2": "line_numbers", 
                    "3": "reverse_lines",
                    "4": "uppercase"
                }
                
                operation = operations.get(op_choice, "word_count")
                processed_content = processor.process_text(content, operation)
                
                # Ask for output filename
                default_output = f"processed_{Path(filename).stem}.txt"
                output_filename = get_user_input(f"💾 Output filename (default: {default_output}): ", required=False)
                
                if not output_filename:
                    output_filename = default_output
                
                # Write processed content
                print(f"\n🔄 Writing processed content to '{output_filename}'...")
                success, error_msg = processor.write_file(output_filename, processed_content)
                
                if success:
                    print(f"🎉 File processing completed successfully!")
                else:
                    print(error_msg)
            
            elif choice == "2":
                # Create sample file
                print("\n📝 Creating a sample file for testing...")
                
                sample_content = f"""Welcome to the File Processing Lab!
This is a sample text file created on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}.

This file contains multiple lines for testing:
- Line processing
- Word counting
- Character analysis
- Error handling

Python makes file handling easy and robust!
Remember to always handle exceptions gracefully.

Happy coding! 🐍
"""
                
                sample_filename = get_user_input("📁 Enter filename for sample file (default: sample.txt): ", required=False)
                if not sample_filename:
                    sample_filename = "sample.txt"
                
                success, error_msg = processor.write_file(sample_filename, sample_content, backup=False)
                
                if success:
                    print(f"✅ Sample file '{sample_filename}' created successfully!")
                else:
                    print(error_msg)
            
            elif choice == "3":
                # Show summary
                print("\n📈 PROCESSING SUMMARY:")
                print("=" * 40)
                
                if processor.processed_files:
                    print("✅ Successfully processed files:")
                    for filename in processor.processed_files:
                        print(f"   • {filename}")
                else:
                    print("No files processed yet.")
                
                if processor.errors:
                    print("\n❌ Errors encountered:")
                    for error in processor.errors:
                        print(f"   • {error}")
                else:
                    print("\n✅ No errors encountered!")
            
            elif choice == "4":
                print("\n👋 Thank you for using the File Processing Lab!")
                print("🎉 You've mastered file operations and error handling!")
                break
            
            else:
                print("❌ Invalid choice. Please enter 1-4.")
        
        except KeyboardInterrupt:
            print("\n👋 Program interrupted by user. Goodbye!")
            break
        except Exception as e:
            print(f"\n❌ Unexpected error in main program: {e}")
            print("🔄 Returning to main menu...")


if __name__ == "__main__":
    main()