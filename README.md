# The Chess Opening Analyzer
## About
A program that will produce a graphical sunburst chart of chess openings from the PGN that is provided to it.

You can upload your own PGN files and then create a multi-level piechart to your inputted depth that will show each move by its relative popularity.

The vivid_burst python file will then create a vividly colored graphical chart using PyGal with each opening move (e.g. e4, d4, c4) having their own color. Their children will follow the same color.

The pie chart sizes will be divided based on how frequent the move is compared to its parent. You can hover on the 'slice' of the piechart to see the exact number of games in which that position was reached.

### How to Use
1. Download the repo (make sure you have fulfilled the prerequisites)
2. Download the PGN game you want to analyze (or use one of the examples). Make sure it is downloaded in the same folder as the repo.
3. Run vivid_chart.py.
- You will be asked for the path to the file. Do so by typing in the path to your pgn game relative to vivid_chart. E.g. if you downloaded your file and dragged it into the pgns subfolder, you would type `pgns/my_file.pgn`
- You will then be asked to what *depth* the chart should be made. **This is ply depth!**. I suggest starting around 4-7 (I haven't tested to see how long it takes to go to depths beyond that. A depth of 6 takes 30 seconds)
4. Enjoy!

### Prerequisites
- Runs in Python 3, must have Python 3 installed
- Requires PyGal
You can install PyGal using PyPi, as long as you are an admin user on your device. To do so, simply type `pip install pygal` into your terminal.

### Downloading
Downloading *is* an option, although to do so you will need to go to vivd_chart.py and scroll to the bottom of the fie. There, several lines will be commented out.

Currently, you can uncomment the download interactive HTML file without anything else to download. If you do so, an HTML file of the graph will be saved to your device, which you can open with your browser.

You can also download the file as: SVG, PDF, JPEG, PNG, and WebP. Just uncomment those lines in the file as well, instructions are there. However, if you want to download in *these* formats you need the following installed.

`npm install -g electron@1.8.4 orca`

`pip install psutil requests`

`pip install psutil`

## Examples
*All examples were that of Magnus Carlsen's OTB tournament games*
### Simple Pie Chart
<p align="center">
  <img width="700" height="450" src="https://github.com/Destaq/opening_analysis/raw/master/images/carlsen_5.png">
</p>

### Hover Functionality
<p align="center">
  <img width = "197" height = "172" src = "https://github.com/Destaq/opening_analysis/raw/master/images/hover_Example.png">
 </p>

### Click to Zoom
<p align="center">
  <img width = "700" height = "450" src = "https://github.com/Destaq/opening_analysis/raw/master/images/carlsen_Nf3_4.png">
 </p>

## Extra Info
I based this project off of a post that I read on ebemunk's blog - you can find the link here: https://blog.ebemunk.com/a-visual-look-at-2-million-chess-games/. However, that project was written in Java and it didn't have everything that I wanted, such as showing all the games, zooming in, etc.
