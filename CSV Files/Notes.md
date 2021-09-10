# Reading and Writing CSV Files
**CSV (Comma Separated Values)** is a simple file format used to store tabular data, such as a spreadsheet or database. A CSV file stores tabular data (numbers and text) in plain text. Each line of the file is a data record. Each record consists of one or more fields, separated by commas. The use of the comma as a field separator is the source of the name for this file format.

## Module Contents
The csv module defines the following functions:
* **csv.writer(csvfile, dialect='excel', **fmtparams)**
Return a writer object responsible for converting the user’s data into delimited strings on the given file-like object. csvfile can be any object with a write() method. If csvfile is a file object, it should be opened with newline='' 1. An optional dialect parameter can be given which is used to define a set of parameters specific to a particular CSV dialect. It may be an instance of a subclass of the Dialect class or one of the strings returned by the list_dialects() function. The other optional fmtparams keyword arguments can be given to override individual formatting parameters in the current dialect. For full details about dialects and formatting parameters, see the Dialects and Formatting Parameters section. To make it as easy as possible to interface with modules which implement the DB API, the value None is written as the empty string. While this isn’t a reversible transformation, it makes it easier to dump SQL NULL data values to CSV files without preprocessing the data returned from a cursor.fetch* call. All other non-string data are stringified with str() before being written.

## Reader Objects
* **csvreader.next()**
Return the next row of the reader’s iterable object as a list (if the object was returned from reader()) or a dict (if it is a DictReader instance), parsed according to the current Dialect. Usually you should call this as next(reader).
* **csvreader.line_num**
The number of lines read from the source iterator. This is not the same as the number of records returned, as records can span multiple lines.