# About
A program that will produce a graphical sunburst chart of chess openings from the PGN that is provided to it.

You can upload your own PGN files and then create a multi-level piechart to your inputted depth that will show each move by its relative popularity.

The vivid_burst python file will then create a vividly colored graphical chart using PyGal with each opening move (e.g. e4, d4, c4) having their own color. Their children will follow the same color.

The pie chart sizes will be divided based on how frequent the move is compared to its parent. You can hover on the 'slice' of the piechart to see the exact number of games in which that position was reached.

# Prerequisites
- Runs in Python 3, must have Python 3 installed
- Requires PyGal
You can install PyGal using PyPi, as long as you are an admin user on your device. To do so, simply type `pip install pygal` into your terminal.

# Examples
## Simple Pie Chart
<p align="center">
  <img width="700" height="450" src="https://github.com/Destaq/opening_analysis/raw/master/images/carlsen_5.png">
</p>

## Hover Functionality
<p align="center">
  <img width = "197" height = "172" src = "https://github.com/Destaq/opening_analysis/raw/master/images/hover_Example.png">
 </p>
