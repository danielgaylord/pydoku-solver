# Python Sudoku Solver
 A sudoku solving program I started making in Python to practice the language and solve a 'problem' all at once. Pretty basic so far.

 By [@danielgaylord](https://github.com/danielgaylord)

## Table of Contents

Every good README has a table of contents, right?

- [TO DO](https://github.com/danielgaylord/pydoku-solver#to-do)
- [File Structure](https://github.com/danielgaylord/pydoku-solver#file-structure)
- [Changelog](https://github.com/danielgaylord/pydoku-solver#changelog)

## TO DO

- [x] Create the basic algorithm that looks through rows, columns, and diagonals
- [x] Modularize functions to be useful outside of this program
- [x] Modularize Cell object
- [x] Add ability to solve naked pairs
- [x] Add ability to add additional sudoku types (diagonals, strange-sized regions)
- [ ] Add a UI (using django?) to make it easier to use
- [ ] Add additional solving techniques (naked triples+, hidden pairs+, interactions)
 
## File Structure

- _cell.py_
  - Represents one cell in a sudoku puzzle
- _region.py_
  - Represents one region in a sudoku puzzle (i.e. row, column, box, etc)
- _sudoku.py_
  - Represents a sudoku puzzle, this is the brains
- _main.py_
  - Current location for running the program

## Changelog

### 11/09/21

From [Dan](https://github.com/danielgaylord)

- Added React for frontend
- Added Heroku for deployment

### 11/02/21

From [Dan](https://github.com/danielgaylord)

- Initializing Flask and starting template

### 10/10/21

From [Dan](https://github.com/danielgaylord)

- Delayed commit (this work occured among 3 days)
- Seperated program into cell, region, and sudoku classes
- Created helper functions and move pre existing functions around to make program more 'modular' and easy to read
- Added ability to solve non-normal sudoku puzzle types
- Added ability to use the nake pair solving technique

### 10/7/21

From [Dan](https://github.com/danielgaylord)

- Added README

### 8/2/17

From [Dan](https://github.com/danielgaylord)

- Created basic brains to solve all non-'naked pair' puzzles
