# 🖋️ File Read & Write Challenge with Error Handling Lab

A comprehensive Python program demonstrating robust file operations, text processing, and bulletproof error handling. This application showcases production-level file management techniques with graceful error recovery.

## 📋 Table of Contents
- [Features](#-features)
- [Installation](#-installation)
- [Usage](#-usage)
- [File Operations](#-file-operations)
- [Error Handling](#-error-handling)
- [Examples](#-examples)
- [Technical Details](#-technical-details)
- [Contributing](#-contributing)

## ✨ Features

### 🖋️ File Operations
- **Smart File Reading**: Multi-encoding support (UTF-8, UTF-16, Latin-1, CP1252)
- **Safe File Writing**: Automatic backups and directory creation
- **Text Processing**: Word counting, line numbering, content transformation
- **Cross-Platform**: Works on Windows, macOS, and Linux

### 🛡️ Error Handling
- **Comprehensive Exception Management**: Handles all common file system errors
- **Graceful Degradation**: Program continues after errors
- **Detailed Error Reporting**: Clear, actionable error messages
- **User Input Validation**: Prevents crashes from invalid input

### 🎯 Text Processing Operations
- **Statistics Generation**: Word, line, and character counts
- **Line Numbering**: Add numbered lines to content
- **Content Reversal**: Reverse line order for analysis
- **Text Transformation**: Uppercase conversion and more

## 🚀 Installation

### Prerequisites
- Python 3.6+ (uses pathlib and modern f-strings)
- No external dependencies required (uses only standard library)

### Setup
1. **Clone or Download**:
   ```bash
   # Download the file_handler.py script
   wget https://your-repo/file_handler.py
   # Or save the code to a local file
   ```

2. **Make Executable** (Unix/macOS):
   ```bash
   chmod +x file_handler.py
   ```

3. **Run**:
   ```bash
   python file_handler.py
   # Or on Unix/macOS:
   ./file_handler.py
   ```

## 📖 Usage

### Interactive Menu
The program provides a user-friendly menu interface:

```
🖋️  FILE READ & WRITE CHALLENGE WITH ERROR HANDLING LAB
============================================================

📋 MENU:
1. Read and process a file
2. Create a sample file for testing
3. View processing summary
4. Exit
```

### Quick Start Example
1. **Create Sample File**: Choose option 2 to generate a test file
2. **Process File**: Choose option 1 to read and transform the file
3. **View Results**: Check the generated output file

## 🔧 File Operations

### Reading Files
```python
# The program handles multiple scenarios:
✅ File exists and readable
❌ File doesn't exist
❌ Permission denied
❌ Encoding issues
❌ Directory instead of file
```

### Processing Operations
| Operation | Description | Output Example |
|-----------|-------------|----------------|
| **Word Count** | Statistics + original content | Lines: 10, Words: 45, Characters: 234 |
| **Line Numbers** | Add numbered lines | `001: First line content` |
| **Reverse Lines** | Reverse line order | Last line becomes first |
| **Uppercase** | Convert to uppercase | `HELLO WORLD` |

### Writing Files
- **Automatic Backups**: Creates `.backup` files before overwriting
- **Directory Creation**: Creates missing directories automatically
- **Safe Encoding**: Uses UTF-8 with proper error handling

## 🛠️ Error Handling

### File System Errors
```python
# Handled Error Types:
FileNotFoundError    # File doesn't exist
PermissionError      # No read/write access
UnicodeDecodeError   # Encoding issues
OSError             # General OS-level errors
IsADirectoryError   # Path is directory, not file
```

### Error Recovery Strategies
- **Multiple Encoding Attempts**: Tries UTF-8, UTF-16, Latin-1, CP1252
- **Graceful Fallbacks**: Program continues after individual failures
- **Detailed Logging**: All errors tracked for review
- **User-Friendly Messages**: Clear explanations, not technical jargon

## 💡 Examples

### Example 1: Processing a Text File
```bash
$ python file_handler.py

📋 MENU:
1. Read and process a file
> 1

📁 Enter filename to read: my_document.txt
✅ Successfully read 'my_document.txt' using utf-8 encoding

📊 Choose processing operation:
1. Word/Line/Character count
> 1

💾 Output filename (default: processed_my_document.txt): 
✅ Successfully wrote to 'processed_my_document.txt'
🎉 File processing completed successfully!
```

### Example 2: Handling Missing File
```bash
📁 Enter filename to read: nonexistent.txt
❌ File 'nonexistent.txt' does not exist
```

### Example 3: Permission Error
```bash
📁 Enter filename to read: /root/protected.txt
❌ Permission denied: Cannot read '/root/protected.txt'
```

## 🔍 Technical Details

### Architecture
```
FileProcessor Class
├── read_file()      # Multi-encoding file reading
├── write_file()     # Safe file writing with backups
└── process_text()   # Text transformation operations

Main Program
├── get_user_input() # Input validation and error handling
└── main()          # Interactive menu system
```

### Key Technologies
- **pathlib.Path**: Modern, cross-platform path handling
- **Multiple Encoding Support**: Handles various text formats
- **Context Managers**: Proper file handle management
- **Exception Chaining**: Preserves original error context

### Performance Considerations
- **Memory Efficient**: Reads files in single operation for small-to-medium files
- **Encoding Detection**: Tries common encodings before failing
- **Backup Strategy**: Only creates backups when necessary

## 🧪 Testing Scenarios

### Create Test Cases
The program includes a sample file generator that creates files with:
- Multiple lines of text
- Special characters
- Timestamps
- Various content types for testing

### Error Testing
Test these scenarios to see robust error handling:
```bash
# Test non-existent file
Enter filename: fake_file.txt

# Test directory instead of file
Enter filename: /home/user/Documents/

# Test permission denied
Enter filename: /etc/passwd

# Test binary file (will try multiple encodings)
Enter filename: image.jpg
```

## 🚀 Advanced Usage

### Batch Processing (Future Enhancement)
```python
# Example of how to extend for batch processing:
files = ["doc1.txt", "doc2.txt", "doc3.txt"]
for file in files:
    success, content, error = processor.read_file(file)
    if success:
        processed = processor.process_text(content, "word_count")
        processor.write_file(f"processed_{file}", processed)
```

### Custom Operations
```python
# Add custom text processing operations:
def process_text(self, content, operation="custom"):
    if operation == "custom":
        # Your custom processing logic here
        return modified_content
```

## 🤝 Contributing

### Code Style
- **PEP 8 Compliance**: Follow Python style guidelines
- **Type Hints**: Add type annotations for clarity
- **Docstrings**: Document all functions and classes
- **Error Messages**: Use emoji and clear language

### Enhancement Ideas
- [ ] Support for binary file detection
- [ ] Configuration file for custom operations
- [ ] GUI interface using tkinter
- [ ] Batch processing capabilities
- [ ] Plugin system for custom transformations
- [ ] Progress bars for large files
- [ ] File format detection and conversion

### Reporting Issues
1. **Error Context**: Include full error messages
2. **Environment**: Python version, OS, file types
3. **Reproduction Steps**: Exact steps to reproduce
4. **Expected Behavior**: What should happen instead

## 📚 Learning Objectives

This program demonstrates mastery of:

### File I/O Concepts
- Opening, reading, and writing files safely
- Handling different text encodings
- Managing file permissions and paths
- Creating backups and handling overwrites

### Error Handling Patterns
- Try-except blocks with specific exceptions
- Error recovery and graceful degradation
- User-friendly error messaging
- Logging and error tracking

### Python Best Practices
- Context managers (`with` statements)
- Modern path handling with `pathlib`
- Input validation and sanitization
- Clean code organization and documentation

## 🎉 Outcomes

By studying and running this program, you'll master:

✅ **Robust File Operations**: Handle any file system scenario
✅ **Professional Error Handling**: Build bulletproof applications  
✅ **User Experience Design**: Create friendly, informative interfaces
✅ **Production Code Quality**: Write maintainable, documented code

## 📄 License

This project is provided for educational purposes. Feel free to use, modify, and distribute for learning and teaching Python file operations and error handling.

---

**Happy Coding! 🐍**

*Remember: Great programs don't just work when everything goes right – they shine when things go wrong!*
