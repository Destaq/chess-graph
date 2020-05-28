![Python application](https://github.com/Destaq/chess_graph/workflows/Python%20application/badge.svg)
[![PyPI version](https://badge.fury.io/py/chess-graph.svg)](https://badge.fury.io/py/chess-graph)
![PyPI - Downloads](https://img.shields.io/pypi/dm/chess-graph)
# The Chess Opening Analyzer
**Available on PyPI with `pip install chess-graph`!**

<p align="center">
  <img width = "574" height = "400" src = "https://github.com/Destaq/opening_analysis/raw/master/images/main_image.png">
 </p>

## About
A program that will produce a graphical sunburst chart of chess openings from the PGN that is provided to it.

You can upload your own PGN files and then create a multi-level piechart to your inputted depth that will show each move by its relative popularity.

The `chart.py` python file will then create a vividly colored graphical chart using Plot.ly with each segment shaded based on how often white/black win.

The pie chart sizes will be divided based on how frequent the move is compared to its parent. You can hover on the 'slice' of the piechart to see the exact number of games in which that position was reached; clicking is also possible to expand that segment to 100%.

### Features
- Make graph of games to **any depth**
- Upload a **custom database** and see how *your* chart looks like
- **Hover** to see metadata such as **game count and percentage of parent**
- Easily **find openings** with simple hover tooltip identification
- **Click to zoom** in on a slice and expand it, making it easy to magnify any slice of the pie chart
- **Downloadable files**: you can download the chart as an interactive HTML, or as a static PNG/JPEG/SVG/WEBP image with just a few clicks
- **Win Ratio Shading** means that you will never be in doubt as to what next move is statistically best
- **Run easily** with the PyPI module, `chess-graph`
- **Hide small slices** and prevent them from showing up in the graph!
- **Custom player and color** by choosing games from a certain player where they played as a certain color

### Prerequisites
- Runs in Python 3, must have Python 3 installed
- Requires Plotly and pgnparser
- To run as PyPI module, have this projects PyPI package installed

You can install Plotly and pgnparser using PyPi, as long as you are an admin user on your device. To do so, simply type `pip install plotly` and `pip install pgnparser` into your terminal.

If you would like to simply run this code from Python IDE, then type `pip install chess-graph` (make sure you have the other modules installed as well).

### How to Use

#### Using directly from the Github Repo
1. Download the repo (make sure you have fulfilled the prerequisites)
2. Download the PGN game you want to analyze (or use one of the examples). Make sure it is downloaded in the same folder as the repo.
3. Import `chart.py`
4. Run the function `chess_graph.graph(*path to file*, depth=5, shade = True, fragmentation_percentage=0.0032, should_defragment=False, custom_branching=False, should_download = False, download_format = 'png', download_name = 'fig1')`
- Note that the path to the pgn file must be relative to the current directory python is running in. For example, if you have the pgn downloaded on your Desktop, you could easily solve this issue by navigating to Desktop within terminal (cd Desktop). From there, you can run *path to file* simply by typing in the filename (assuming it is in Desktop). If this is confusing, just type in the full path.
- The arguments with an equal sign means that they are set to that as default, but you can change them by typing in e.g. depth = 7.

#### Using via pip install
1. `pip install chess-graph`
2. Open terminal/interpreter.
3. `import chess_graph`
4. `chess_graph.graph(database, depth=5, shade = True, fragmentation_percentage=0.0032, should_defragment=False, custom_branching=False, should_download = False, download_format = 'png', download_name = 'fig1')`
  - Note that the path to the pgn file (the database) must be relative to the current directory python is running in. For example, if you have the pgn downloaded on your Desktop, you could easily solve this issue by navigating to Desktop within terminal (cd Desktop). From there, you can replace the database argument with the simple filename (assuming it is in Desktop). If this is confusing, just type in the full path.
  
 *Special note: there can be some issues if the file you are trying to open is saved in icloud. In that case, you will see a small cloud next to the file with a downwards-pointing arrow. Click on it to download the file - otherwise it will be stored on the cloud and won't register as on your device, and thus cannot be read by the python program.*

### A Deeper Look at the Function
  The `graph()` function takes 9 arguments, and 8 of them are default-set. We'll explore each of them so that you know how to properly use this package to its full potential.

  You can run this function either by importing it through `pip install chess_graph` and then running `chess_graph.graph(...)` which will be how this documentation is laid out. You can also run it from the downloaded GitHub repo by navigating to the repository, typing `import chart` OR by modifying the `chart.py` file at the bottom and calling the function there.

  - The `database` argument: This argument must *always* be inputted. It is the path to the file. Let's look at two examples.

    1. `chess_graph.graph('Users/student/Desktop/pgns/mir_khan.pgn')`. Here, we are running the chess_graph on a pgn from Mir Sultan Khan. We are showing the program what file to read this by providing the full path to the file.

    2. In the example above, you can see that the file is in the `pgns` folder in Desktop. So, we can open our terminal, and then type `cd Desktop`, `cd pgns` to go the folder that has this file. Because we are now in that directory, we can type: `chess_graph.graph('mir_khan.pgn')` as it is in the current directory. If you are unsure, stick with the full file path.

  - The `depth` argument. This is set to 5 by default, and shows the number of rings that the pie chart will have. You can change this by typing `chess_graph.graph(*path to file*, depth = 7)`. Make sure that you type `depth = `, and not just the integer depth.

  - The `shade` argument. This is set to True by default. It is whether you should shade the segments or not based on W/B win percentage. If you set it to False, (`chess_graph.graph(*path to file*, shade = False)`), then a vividly colored chart will be produced instead.

  - The `fragmentation_percentage` argument. Set to 0.0032 by default. You can 'defragment' the graph by hiding very small slices. This argument shows how small the slices have to be (relative to the total number of games, e.g. 2 games/100 games total = 2%) to be deleted. In this example, the percentage is 100*0.0032 = 0.32%. Example: `chess_graph.graph(*path to file*, fragmentation_percentage = 0.05)` - 5% or smaller will be deleted.

  - The `should_defragment` argument. Set to False by default. Setting it to True will allow the graph to hide the slices, keeping it False will show all slices. Even if you change fragmentation_percentage, if this isn't set to True, nothing will change. Example: `chess_graph.graph(*path to file*, fragmentation_percentage = 0.05, should_defragment = True)`

  - The `custom branching` argument. Set to False by default. You can analyze a database from any position if set to True. Example: `chess_graph.graph(*path to file*, custom_branching = True)`. You will be asked for an input for the custom branching. For the sake of this example, let's say you want to analyze only positions from e4 e5. So, type e4 e5. The graph will then show positions only from e4 e5.

  - The `should_download` argument. Set to False be default. You can download the figures in five different formats (see more below). Make sure you have the packages installed before downloading. You can set this to True if you would like to download the figure.

  - The `download_format` argument. Set to the string 'png' by default. Change it to the string of the file type you want the download to be in. `chess_graph.graph(..., download_format = 'jpeg')`

  - The `download_name` argument. The name of the figure that will be downloaded. Set to be fig1 by default, meaning that files downloaded will be downloaded as fig1.png. See above.

  - The `color` argument. This is set to both by default. Valid inputs are 'both', 'white', 'w', 'black' and 'b'. If you change the `color` argument from both, then the program will only read games that are from the `color` you chose. Note that you need to also change the player name with the name argument if you do so. See below.

  - The `name` argument. This argument will allow the program to pick games from the file it is given, but only games from a certain player. There is an example below: Set the color to 'black' or 'white' to pick only games where the player (the name) played as black or white. (i.e. chess_graph.graph('pgns/Carlsen.pgn', color = 'white', name = 'Magnus Carlsen') will pick all the games where Carlsen played as white.)

**Remember to include all variations and parts of a player's name! For example, the player Viktor Korchnoi has his last name spelled as Kortschnoj as well. In that case, for the 'name' field, type: Viktor Korchnoi Kortschnoj**

### Downloading
Downloading *is* an option, although to download in some formats you need to install extra libraries.

Currently, you can download as an interactive HTML file without any extra dependencies. If you do so, an HTML file of the graph will be saved to your device, which you can open with your browser.

You can also download the file as: SVG, PDF, JPEG, PNG, and WebP.

However, if you want to download in *these* formats you need the following installed.

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
