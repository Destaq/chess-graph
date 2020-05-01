![Python application](https://github.com/Destaq/chess_opening_graph/workflows/Python%20application/badge.svg)
# The Chess Opening Analyzer

<p align="center">
  <img width = "498" height = "383" src = "https://github.com/Destaq/opening_analysis/raw/master/images/main_image.png">
 </p>

## About
A program that will produce a graphical sunburst chart of chess openings from the PGN that is provided to it.

You can upload your own PGN files and then create a multi-level piechart to your inputted depth that will show each move by its relative popularity.

The `chart` python file will then create a vividly colored graphical chart using Plot.ly with each segment shaded based on how often white/black win.

The pie chart sizes will be divided based on how frequent the move is compared to its parent. You can hover on the 'slice' of the piechart to see the exact number of games in which that position was reached; clicking is also possible to expand that segment to 100%.

### Features
- Make graph of games to **any depth**
- Upload a **custom database** and see how *your* chart looks like
- **Hover** to see metadata such as **game count and percentage of parent**
- Easily **find openings** with simple hover tooltip identification
- **Click to zoom** in on a slice and expand it, making it easy to magnify any slice of the pie chart
- **Downloadable files**: you can download the chart as an interactive HTML, or as a static PNG/JPEG/SVG/WEBP image with just a few clicks
- **Win Ratio Shading** means that you will never be in doubt as to what next move is statistically best

### How to Use
1. Download the repo (make sure you have fulfilled the prerequisites)
2. Download the PGN game you want to analyze (or use one of the examples). Make sure it is downloaded in the same folder as the repo.
3. Run chart.py.
- You will be asked for the path to the file. Do so by typing in the path to your pgn game relative to vivid_chart. E.g. if you downloaded your file and dragged it into the pgns subfolder, you would type `pgns/my_file.pgn`
- You will then be asked to what *depth* the chart should be made. **This is ply depth!**. Keep in mind: ply depth of 5 takes 30 seconds for a database with a few thousand games, and it takes 2 minutes to go to a depth of 8 for a few thousand games as well.

### Prerequisites
- Runs in Python 3, must have Python 3 installed
- Requires Plotly and Python-Chess

You can install Plotly and Python-Chess using PyPi, as long as you are an admin user on your device. To do so, simply type `pip install plotly` and `pip install python-chess` into your terminal.

### Downloading
Downloading *is* an option, although to do so you will need to go to chart.py and scroll to the bottom of the fie. There, several lines will be commented out.

Currently, you can uncomment the download interactive HTML file without anything else to download. If you do so, an HTML file of the graph will be saved to your device, which you can open with your browser.

You can also download the file as: SVG, PDF, JPEG, PNG, and WebP. Just uncomment those lines in the file as well, instructions are there. However, if you want to download in *these* formats you need the following installed.

`npm install -g electron@1.8.4 orca`

`pip install psutil requests`

`pip install psutil`

## Examples
*All examples are those of Magnus Carlsen's OTB tournament games*
### Simple Pie Chart
<p align="center">
  <img width="700" height="450" src="https://github.com/Destaq/opening_analysis/raw/master/images/random.png">
</p>

### Hover Functionality | Show Percentage of Parent + Game Count
<p align="center">
  <img width = "522" height = "117" src = "https://github.com/Destaq/opening_analysis/raw/master/images/hovering.png">
 </p>

### Click to Zoom
<p align="center">
  <img width = "528" height = "457" src = "https://github.com/Destaq/opening_analysis/raw/master/images/zoom.png">
 </p>

## Extra Info
I based this chart loosely off of a post that I read on ebemunk's blog - you can find the link here: https://blog.ebemunk.com/a-visual-look-at-2-million-chess-games/. However, that project was written in Java and it didn't have everything that I wanted, such as showing all the games, zooming in, etc.
