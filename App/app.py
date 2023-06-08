from datetime import datetime
import csv
import time
from time import sleep
import math
import keyboard
import numpy as np
import asciichartpy

from rich import print
from rich import box
from rich.tree import Tree
from rich.text import Text
from rich.align import Align
from rich.panel import Panel
from rich.layout import Layout 
from rich.table import Table

from rich.live import Live
from rich.prompt import Prompt
from rich.progress import track
from rich.progress import BarColumn, Progress, SpinnerColumn, TextColumn

from rich.traceback import install
install(show_locals=True)

layout = Layout()

layout.split_column(
    Layout(name = "Header", size=3),
    Layout(name = "Body"),
    Layout(name = "Footer", size=3)
)

layout["Body"].split_column(
    Layout(name = "Upper_Body", ratio=2),
    Layout(name = "Lower_Body")
)

layout["Upper_Body"].split_row(
    Layout(name="Channels"),
    Layout(name="Chat", ratio=4)    
)

layout["Chat"].split_column(
    Layout(name = "messages"),
    Layout(name = "type bar", size=4)
)

layout["Lower_Body"].split_row(
    Layout(name = "LB_1"),
    Layout(name = "LB_2")
)

class Header:

    def __rich__(self) -> Panel:
        grid = Table.grid(expand=True)
        grid.add_column(justify="left")
        grid.add_column(justify="center", ratio=1)
        grid.add_column(justify="right")
        grid.add_row(
            "👔", "[b]ConnectWave[/]", datetime.now().ctime().replace(":", "[blink]:[/]"),
        )
        return Panel(grid, style="bold white")
    
class Footer:

    def __rich__(self) -> Panel:
        grid = Table.grid(expand=True)
        grid.add_column(justify="left")
        grid.add_column(justify="center", ratio=1)
        grid.add_column(justify="right")
        grid.add_row(
            "💻", "[b]Simplifying Collaboration. Empowering Success.[/]", "📊")
        return Panel(grid, style="blue on black")
    
def Channels():
    tree = Tree("Rich Tree")
    tree.add("foo")
    tree.add("bar")
    
    baz_tree = tree.add("Business")
    baz_tree.add("[red]Document Channel")
    baz_tree = tree.add("Finances")
    baz_tree.add("General")
    baz_tree.add("Documents")
    
    channels_panel = Panel(baz_tree, title = "Channels", border_style="Bold white", box = box.SQUARE)
    
    return channels_panel

def Chat():
    ...

layout["Header"].update(Header())
layout["Footer"].update(Footer())
layout["Channels"].update(Channels())

print(layout)