# Notes

Here are all the topics under File Handling in Python:
1. Fundamentals

1.1 What is File Handling & Why It's Needed
1.2 File Types (Text Files vs Binary Files)
1.3 File Paths (Absolute vs Relative)
1.4 File Objects (Concept)

2. Opening & Closing Files

2.1 open() Function
2.2 File Open Modes (r, w, a, x, r+, w+, a+, rb, wb, ab, rb+, wb+)
2.2.1 Read Mode (r)
2.2.2 Write Mode (w) — Overwrites File
2.2.3 Append Mode (a)
2.2.4 Exclusive Creation Mode (x)
2.2.5 Read/Write Mode (r+, w+, a+)
2.2.6 Binary Modes (rb, wb, ab, etc.)
2.3 close() Method
2.4 Why Closing Files Matters (Resource Leaks)
2.5 file.closed Attribute (Checking if File is Closed)

3. Context Managers for Files

3.1 with Statement (Automatic File Closing)
3.2 Why with is Preferred Over Manual open()/close()
3.3 Multiple Files in a Single with Statement

4. Reading Files

4.1 read() Method (Read Entire File)
4.2 read(size) (Read Specific Number of Characters/Bytes)
4.3 readline() Method (Read One Line)
4.4 readlines() Method (Read All Lines into a List)
4.5 Iterating Over a File Object Line by Line (Most Memory-Efficient)
4.6 Reading Large Files in Chunks

5. Writing Files

5.1 write() Method
5.2 writelines() Method
5.3 Writing Multiple Lines
5.4 Appending vs Overwriting Data
5.5 Adding Newlines (\n) Manually

6. File Pointer / Cursor Handling

6.1 tell() Method (Current Cursor Position)
6.2 seek() Method (Moving Cursor to a Specific Position)
6.3 seek() with Whence Parameter (0 = start, 1 = current, 2 = end)
6.4 Practical Use of Cursor Control

7. Working with File Paths — os Module

7.1 os.getcwd() (Current Working Directory)
7.2 os.chdir() (Change Directory)
7.3 os.listdir() (List Files in a Directory)
7.4 os.mkdir() / os.makedirs() (Create Directories)
7.5 os.remove() (Delete a File)
7.6 os.rmdir() / os.removedirs() (Delete Directories)
7.7 os.rename() (Rename a File/Directory)
7.8 os.path.exists() (Check if File/Path Exists)
7.9 os.path.isfile() / os.path.isdir()
7.10 os.path.join() (Cross-Platform Path Building)
7.11 os.path.split() / os.path.splitext()
7.12 os.path.abspath() / os.path.basename() / os.path.dirname()
7.13 os.path.getsize() (File Size)
7.14 os.walk() (Traverse Directory Tree)

8. Working with File Paths — pathlib Module (Modern Approach)

8.1 Path Object (Introduction)
8.2 Creating Paths (Path("folder/file.txt"))
8.3 Path.exists(), Path.is_file(), Path.is_dir()
8.4 Path.mkdir()
8.5 Path.iterdir() (List Directory Contents)
8.6 Path.glob() / Path.rglob() (Pattern Matching Files)
8.7 Path.read_text() / Path.write_text()
8.8 Path.read_bytes() / Path.write_bytes()
8.9 Path Properties (.name, .suffix, .stem, .parent)
8.10 pathlib vs os.path (Why pathlib is Preferred Today)

9. Working with Binary Files

9.1 Reading Binary Files (Images, PDFs, etc.)
9.2 Writing Binary Files
9.3 Use Cases (copying images, downloading files)

10. Working with CSV Files

10.1 csv Module Introduction
10.2 Reading CSV with csv.reader()
10.3 Reading CSV with csv.DictReader()
10.4 Writing CSV with csv.writer()
10.5 Writing CSV with csv.DictWriter()
10.6 Handling Delimiters & Quoting
10.7 Reading/Writing CSV with Pandas (pd.read_csv(), to_csv()) — cross-reference

11. Working with JSON Files

11.1 json Module Introduction
11.2 json.load() (Read JSON from File)
11.3 json.loads() (Parse JSON from String)
11.4 json.dump() (Write JSON to File)
11.5 json.dumps() (Convert Object to JSON String)
11.6 Pretty-Printing JSON (indent parameter)
11.7 Handling Nested JSON Structures
11.8 JSON Serialization of Custom Objects

12. Working with XML Files

12.1 xml.etree.ElementTree Module
12.2 Parsing XML Files
12.3 Navigating XML Tree (elements, attributes)
12.4 Creating/Writing XML Files

13. Working with Other File Formats (Overview)

13.1 YAML Files (PyYAML library)
13.2 Excel Files (openpyxl, pandas) — cross-reference
13.3 Parquet/Avro Files (Data Engineering context) — cross-reference to Spark/Data Lake sections

14. File Handling Exceptions

14.1 FileNotFoundError
14.2 PermissionError
14.3 IsADirectoryError
14.4 FileExistsError
14.5 Handling File Errors with try-except-finally
14.6 Combining with + try-except for Safe File Operations

15. Temporary Files

15.1 tempfile Module
15.2 tempfile.TemporaryFile()
15.3 tempfile.NamedTemporaryFile()
15.4 tempfile.TemporaryDirectory()
15.5 Use Cases (staging data before upload, testing)

16. File Compression & Archiving

16.1 zipfile Module (Reading/Writing ZIP Files)
16.2 tarfile Module (Reading/Writing TAR Files)
16.3 gzip Module
16.4 shutil Module (copy(), move(), make_archive())

17. File Encoding

17.1 Understanding Encoding (utf-8, ascii, etc.)
17.2 Specifying Encoding in open()
17.3 UnicodeDecodeError Handling
17.4 encode() / decode() Methods

18. File Locking & Concurrency (Advanced)

18.1 Why File Locking Matters (Concurrent Access Issues)
18.2 filelock Library (Overview)
18.3 Race Conditions in File I/O

19. Best Practices

19.1 Always Use with Statement
19.2 Handle Large Files Efficiently (Streaming, Chunking, Avoid Loading Entirely into Memory)
19.3 Always Specify Encoding Explicitly
19.4 Validate File Existence Before Operations
19.5 Use pathlib Over os.path for New Code
19.6 Clean Up Temporary Files

20. Real-World / Applied Topics (Data Engineering Focus)

20.1 Reading/Writing Files from Local to Cloud (S3) — cross-reference to AWS section
20.2 Processing Large Log Files Line by Line
20.3 File-Based ETL Patterns (staging files, archiving processed files)
20.4 Watching a Directory for New Files (polling pattern)