import customtkinter as ctk
from datetime import datetime
import tkinter as tk

class CTkGraph(ctk.CTkFrame):
    """
    Widget to display list of integers as a graph. You can customize almost everything, except for the corner radius
    of the canvas that draws the graph.

    You can also set a custom title, if you don't do is the Labeled won't be rendered.

    Graph axis vars are responsible for the arrows of the graph, graph line is responsible for the outline of the
    graph polygon (the graph is represented with a polygon)
    """
    def __init__(self, master,
                 data_values: list,
                 fg_color="gray17",
                 graph_fg_color="gray17",
                 width=200,
                 height=200,
                 border_width=None,
                 border_color=None,
                 corner_radius=None,
                 graph_color="gray20",
                 graph_axis_width=3,
                 graph_line_width=2,
                 graph_axis_color="white",
                 graph_line_color="white",
                 graph_axis_arrow="last",
                 title_font_family="Arial",
                 title_font_size=16,
                 title_text_color=None,
                 title=None):

        super().__init__(master=master, fg_color=fg_color, width=width, height=height, corner_radius=corner_radius,
                         border_color=border_color, border_width=border_width)

        # data
        self.data_values = data_values
        self.date = self.current_date()
        self.date_display = self.date[:]
        self.graph_fg_color = graph_fg_color
        self.graph_color = graph_color
        self.main_canvas = None

        # graph data
        self.width = width
        self.height = height
        self.graph_axis_width = graph_axis_width
        self.graph_line_width = graph_line_width
        self.graph_axis_color = graph_axis_color
        self.graph_line_color = graph_line_color
        self.graph_axis_arrow = graph_axis_arrow

        # title data
        self.title_font_family = title_font_family
        self.title_font_size = title_font_size
        self.title_text_color = title_text_color
        self.title = title

        # setting up
        self.setup_stat()

    def setup_stat(self):
        if self.title is not None:
            ctk.CTkLabel(self, text=self.title, text_color=self.title_text_color,
                         font=ctk.CTkFont(self.title_font_family, self.title_font_size)).pack(fill="x", padx=10, pady=10)

        self.main_canvas = ctk.CTkCanvas(self, background=self.graph_fg_color, bd=0, highlightthickness=0,
                                         relief="ridge", width=self.width, height=self.height)

        self.main_canvas.pack(expand=True, fill="both", padx=self._corner_radius//2, pady=self._corner_radius//2)

        self.main_canvas.bind("<Configure>", lambda event: self.draw_stats(event.width, event.height))

    def draw_stats(self, width, height):
        # drawing graph lines
        self.main_canvas.delete("all")

        # axis for the graph
        self.main_canvas.create_line(width * 0.05, height * 0.95, width * 0.05, height * 0.05, fill=self.graph_axis_color,
                                     width=self.graph_axis_width, arrow=self.graph_axis_arrow)
        self.main_canvas.create_line(width * 0.05, height * 0.95, width * 0.95, height * 0.95, fill=self.graph_axis_color,
                                     width=self.graph_axis_width, arrow=self.graph_axis_arrow)

        data_len = len(self.data_values)
        max_value = max(self.data_values)
        gap = (width - 15) // data_len
        coordinates = [(width * 0.05, height * 0.95)]

        for i in range(data_len):
            h = height * 0.8 * self.data_values[i] / max_value
            coordinates.append((width * 0.05 + gap * i, height * 0.95 - h))

        else:
            coordinates.append((width * 0.05 + gap * data_len - gap, height * 0.95))

        self.main_canvas.create_polygon(coordinates, width=self.graph_line_width, fill=self.graph_color,
                                        outline=self.graph_line_color)

    def current_date(self) -> tuple[int, int, int]:
        date = str(datetime.now()).split()
        year, month, day = date[0].split("-")
        return int(day), int(month), int(year)
