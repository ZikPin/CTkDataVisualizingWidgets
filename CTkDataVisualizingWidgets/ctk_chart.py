import customtkinter as ctk
import tkinter as tk

class CTkChart(ctk.CTkFrame):
    """
    This is widget to create a chart representation of a dict[str, int]. It takes str of the dict as a key and a title
    for certain stat and int or float for that matter as the value and draws it on the canvas. There are also
    indicators like average and max value.

    You can also set title, if you do not define it, it wont be rendered.

    There are two values with tuple[bool, bool] format:
    * stat_info_show: first bool is responsible for drawing the value in the stat, second for drawing title
    * show_indicators: first bool is responsible for max value, second for average.
    """
    def __init__(self, master,
                 data: dict,
                 width=350,
                 height=250,
                 fg_color="gray17",
                 corner_radius=5,
                 border_width=None,
                 border_color=None,
                 chart_fg_color="gray17",
                 title=None,
                 title_font_family="Arial",
                 title_text_color="white",
                 title_font_size=16,
                 chart_axis_width=4,
                 chart_axis_color="white",
                 chart_arrow="last",
                 show_indicators: tuple[bool, bool] = (True, True),
                 indicator_line_color="white",
                 indicator_text_color="white",
                 stat_color="white",
                 stat_width=30,
                 stat_info_show: tuple[bool, bool] = (True, True),
                 stat_text_color="gray17",
                 stat_title_color="white"):
        super().__init__(master=master, fg_color=fg_color, corner_radius=corner_radius, border_color=border_color,
                         border_width=border_width, width=width, height=height)

        # data
        self.data = data
        self.data_avg, self.data_max = self.format_data()

        # data about chart axis
        self.chart_axis_width = chart_axis_width
        self.chart_axis_color = chart_axis_color
        self.chart_arrow = chart_arrow

        # data about indicators
        self.show_indicators: tuple[bool, bool] = show_indicators
        self.indicator_line_color = indicator_line_color
        self.indicator_text_color = indicator_text_color

        # data about stats
        self.stat_color = stat_color
        self.stat_width = stat_width
        self.stat_info_show = stat_info_show
        self.stat_text_color = stat_text_color
        self.stat_title_color = stat_title_color

        self.main_canvas = ctk.CTkCanvas(self, background=chart_fg_color, bd=0, highlightthickness=0, relief="ridge",
                                         width=width, height=height)

        if title is not None:
            ctk.CTkLabel(self, text=title, font=ctk.CTkFont(title_font_family, title_font_size, "bold"),
                         text_color=title_text_color).pack(fill="x", expand=True)

        self.main_canvas.pack(expand=True, fill="both", padx=corner_radius//1.5, pady=corner_radius//1.5)
        self.main_canvas.bind("<Configure>", lambda event: self.draw_stats())

    def format_data(self) -> tuple[float, int]:
        m = 0.01
        s, count = 0, 0.01

        for value in self.data.values():
            s += value
            count += 1
            m = max(m, value)

        return s/count, m

    def draw_stats(self):
        # updating canvas and canvas info
        self.main_canvas.delete("all")
        canvas_height = self.main_canvas.winfo_height()
        canvas_width = self.main_canvas.winfo_width()

        # drawing graph axis
        self.main_canvas.create_line(0+self.chart_axis_width, canvas_height-self.chart_axis_width-canvas_height*0.15,
                                     canvas_width, canvas_height-self.chart_axis_width-canvas_height*0.15,
                                     capstyle="round", width=self.chart_axis_width, fill=self.chart_axis_color,
                                     arrow=self.chart_arrow)
        self.main_canvas.create_line(0 + self.chart_axis_width, canvas_height-self.chart_axis_width-canvas_height*0.15,
                                     0 + self.chart_axis_width, 0, arrow=self.chart_arrow,
                                     capstyle="round", width=self.chart_axis_width, fill=self.chart_axis_color)

        for index, key in enumerate(self.data.keys()):
            self.draw_stat_day(canvas_width*0.01, canvas_height * 0.2, canvas_width * 0.9, canvas_height * 0.55,
                               index, key)

        # drawing indicator lines
        if self.show_indicators[0]:
            self.draw_stat_indicator(canvas_width * 0.9, canvas_height * 0.2 - 15, "max")
        if self.show_indicators[1]:
            avg_height = canvas_height * 0.55 - canvas_height * 0.55 * (self.data_avg / self.data_max)
            self.draw_stat_indicator(canvas_width * 0.9, avg_height + canvas_height * 0.2, "avg")

    def draw_stat_day(self, graph_x_offset, graph_y_offset, graph_width, graph_height, index, key):
        day_width = graph_width//len(self.data.keys())
        day_offset = day_width*0.6

        value = self.data[key]
        day_stat_height = value / self.data_max * graph_height

        self.main_canvas.create_line(graph_x_offset + day_width * index + day_offset,
                                     graph_y_offset + graph_height,
                                     graph_x_offset + day_width * index + day_offset,
                                     graph_y_offset + graph_height - day_stat_height,
                                     capstyle="round", fill=self.stat_color, width=self.stat_width)

        if self.stat_info_show[0]:
            self.main_canvas.create_text(graph_x_offset + day_width * index + day_offset,
                                         graph_y_offset + graph_height,
                                         text=value, fill=self.stat_text_color,
                                         font=ctk.CTkFont("Arial", 13, "bold"))

        if self.stat_info_show[1]:
            self.main_canvas.create_text(graph_x_offset + day_width * index + day_offset,
                                         graph_y_offset + graph_height + 40,
                                         text=key, fill=self.stat_title_color,
                                         font=ctk.CTkFont("Arial", 13, "bold"))

    def draw_stat_indicator(self, x2, y, title):
        self.main_canvas.create_line(10, y, x2, y,
                                     dash=[20], fill=self.indicator_line_color, capstyle="round", width=3)
        self.main_canvas.create_text(x2+5, y, anchor="w", text=title, fill=self.indicator_text_color,
                                     font=ctk.CTkFont("Arial", 15, "bold"))

