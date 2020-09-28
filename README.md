# TyPy

TyPy is a RESTful application that leverages Python Flask and PostgreSQL to allow the user to create, store, view, edit, and delete notes for themselves. Each new note is created as its own table within the database, and each line within the note is a row within the table. The user is given access to a set of commands that can be entered in the browser console to perform actions related to the notes, as follows:

## Pages

The TyPy application makes use of two webages.

## The Contents Page

This page shows a list of all notes in the database, along with associated metadata including author and date created. This is also the landing page for the application. The contents page has several commands that can be entered into the browser console. Content commands essentially deal with file manipulation.

### \create

Creates a new note. Propmpts the user to enter, in order, the name, author, and date for that note. The command adds a row to the "notes" table, and assigns it a unique id value, and creates a new table to hold that note's contents.

### \open

Opens a specific note. The user can specify a note name or id, and the app will redirect to the Display page, and display the contents of the specified note. If no note is specified, the user will be prompted to specify one or cancel the command.

### \rename

Changes the name of a note. The user must specify the note to be renamed, and the new name. The corresponding entry in the notes table, and the corresponding table, will be updated accordingly.

#### Stretch Goal: More Metadata

Add methods to edit all metadata values for a note. Also, implement timestamping instead of manual date entry.

### \trash

Deletes a note. The user is prompted to confirm before this command is executed.

## The Display Page

This page displays the contents of a single note, and gives the user access to several commands for managing the contents of the note.

### \new

This command adds a new line to the end of the note. The user is prompted to enter the text to be added for that line.

### \edit

This command alters the contents of an existing line. The user must specify the line to be edited by line number, and is then prompted to enter text similarly to the "\new" command.

### \delete

This command removes a specified line, shifting the rest of the contents upward accordingly.The user can also specify a number of lines to be deleted, beginning with the specified line.

#### Stretch Goal: Multi-Delete

Specifying "ALL" instead of a line number will delete all lines.
Specifying "ALL" instead of a quantity of lines will delete the first specified and all after it.

### \close

This command returns the user to the Contents page. All changes are automatically saved as soon as they are made (assuming the database server doesn't crash).
