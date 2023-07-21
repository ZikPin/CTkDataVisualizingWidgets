import customtkinter as ctk
import calendar
from datetime import datetime
import tkinter as tk


class CTkCalendar(ctk.CTkFrame):
    """
    Calendar widget to display certain month, each day is rendered as Label.

    If you do not define today_fg_color and today_text_color it will be rendered as other days
    """
    def __init__(self, master,
                 today_fg_color=None,
                 today_text_color=None,
                 width=250,
                 height=250,
                 fg_color=None,
                 corner_radius=8,
                 border_width=None,
                 border_color=None,
                 bg_color="transparent",
                 background_corner_colors=None,
                 title_bar_fg_color=None,
                 title_bar_border_width=None,
                 title_bar_border_color=None,
                 title_bar_corner_radius=None,
                 title_bar_text_color=None,
                 title_bar_button_fg_color=None,
                 title_bar_button_hover_color=None,
                 title_bar_button_text_color=None,
                 title_bar_button_border_width=None,
                 title_bar_button_border_color=None,
                 calendar_fg_color=None,
                 calendar_border_width=None,
                 calendar_border_color=None,
                 calendar_corner_radius=None,
                 calendar_text_color=None,
                 calendar_text_fg_color=None,
                 calendar_label_pad=1):

        super().__init__(master=master,
                         width=width,
                         height=height,
                         fg_color=fg_color,
                         corner_radius=corner_radius,
                         border_width=border_width,
                         border_color=border_color,
                         bg_color=bg_color,
                         background_corner_colors=background_corner_colors)

        # data
        self.today_text_color = today_text_color
        self.today_fg_color = today_fg_color
        self.today = self.current_date()
        self.day, self.month, self.year = self.today[:]
        self.labels_by_date = dict()
        self.month_label = ctk.StringVar(value=calendar.month_name[self.month])
        self.year_label = ctk.IntVar(value=self.year)

        # data for title bar
        self.title_bar_fg_color = title_bar_fg_color
        self.title_bar_border_width = title_bar_border_width
        self.title_bar_border_color = title_bar_border_color
        self.title_bar_text_color = title_bar_text_color
        self.title_bar_button_fg_color = title_bar_button_fg_color
        self.title_bar_button_hover_color = title_bar_button_hover_color
        self.title_bar_button_text_color = title_bar_button_text_color
        self.title_bar_button_border_width = title_bar_button_border_width
        self.title_bar_button_border_color = title_bar_button_border_color
        self.title_bar_corner_radius = title_bar_corner_radius

        # data for calendar frame
        self.calendar_fg_color = calendar_fg_color
        self.calendar_border_width = calendar_border_width
        self.calendar_border_color = calendar_border_color
        self.calendar_corner_radius = calendar_corner_radius
        self.calendar_text_fg_color = calendar_text_fg_color
        self.calendar_text_color = calendar_text_color
        self.calendar_label_pad = calendar_label_pad

        # creating header and calendar frames
        self.content_frame = ctk.CTkFrame(self, fg_color="transparent", width=width, height=height)
        self.content_frame.pack(expand=True, fill="both", padx=corner_radius/3, pady=corner_radius/3)
        self.setup_header_frame()
        self.create_calendar_frame()

    # setting up the header frame
    def setup_header_frame(self):
        header_frame = ctk.CTkFrame(self.content_frame, fg_color=self.title_bar_fg_color,
                                    corner_radius=self.title_bar_corner_radius,
                                    border_color=self.title_bar_border_color, border_width=self.title_bar_border_width)

        ctk.CTkButton(header_frame, text="<", width=25, fg_color=self.title_bar_button_fg_color,
                      hover_color=self.title_bar_button_hover_color, border_color=self.title_bar_button_border_color,
                      border_width=self.title_bar_button_border_width, font=ctk.CTkFont("Arial", 11, "bold"),
                      command=lambda: self.change_month(-1)).pack(side="left", padx=10)
        ctk.CTkLabel(header_frame, textvariable=self.month_label, font=ctk.CTkFont("Arial", 16, "bold"),
                     fg_color="transparent").pack(side="left", fill="x", expand=True)
        ctk.CTkLabel(header_frame, textvariable=self.year_label, font=ctk.CTkFont("Arial", 16, "bold"),
                     fg_color="transparent").pack(side="left", fill="x")
        ctk.CTkButton(header_frame, text=">", width=25, fg_color=self.title_bar_button_fg_color,
                      hover_color=self.title_bar_button_hover_color, border_color=self.title_bar_button_border_color,
                      border_width=self.title_bar_button_border_width, font=ctk.CTkFont("Arial", 11, "bold"),
                      command=lambda: self.change_month(1)).pack(side="right", padx=10)

        header_frame.place(relx=0.5, rely=0.02, anchor="n", relheight=0.18, relwidth=0.95)

    def create_calendar_frame(self):
        # "updating" frames
        calendar_frame = ctk.CTkFrame(self.content_frame, fg_color=self.calendar_fg_color,
                                      corner_radius=self.calendar_corner_radius,
                                      border_width=self.calendar_border_width, border_color=self.calendar_border_color)
        current_month = calendar.monthcalendar(self.year, self.month)

        # grid
        calendar_frame.columnconfigure((0, 1, 2, 3, 4, 5, 6), weight=1, uniform="b")
        rows = tuple([i for i in range(len(current_month))])
        calendar_frame.rowconfigure(rows, weight=1, uniform="b")

        # labels for days
        for row in range(len(current_month)):
            for column in range(7):
                if current_month[row][column] != 0:
                    if self.today_fg_color is not None and self.year == self.today[2] and self.month == self.today[1] \
                            and current_month[row][column] == self.today[0]:
                        label = ctk.CTkLabel(calendar_frame, text=str(current_month[row][column]), corner_radius=5,
                                             fg_color=self.today_fg_color, font=ctk.CTkFont("Arial", 11),
                                             text_color=self.today_text_color)
                    else:
                        label = ctk.CTkLabel(calendar_frame, text=str(current_month[row][column]), corner_radius=5,
                                             fg_color=self.calendar_text_fg_color, font=ctk.CTkFont("Arial", 11),
                                             text_color=self.calendar_text_color)

                    self.labels_by_date[(current_month[row][column], self.month, self.year)] = label

                    label.grid(row=row, column=column, sticky="nsew", padx=self.calendar_label_pad,
                               pady=self.calendar_label_pad)

        calendar_frame.place(relx=0.5, rely=0.97, anchor="s", relheight=0.75, relwidth=0.95)

    def change_month(self, amount):
        self.month += amount
        if self.month < 1:
            self.year -= 1
            self.month = 12
            self.day = 1
        elif self.month > 12:
            self.year += 1
            self.month = 1
            self.day = 1

        self.month_label.set(calendar.month_name[self.month])
        self.year_label.set(self.year)

        self.create_calendar_frame()

    def current_date(self) -> tuple[int, int, int]:
        date = str(datetime.now()).split()
        year, month, day = date[0].split("-")
        return int(day), int(month), int(year)


class CTkGraph(ctk.CTkFrame):
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


# test window
if __name__ == '__main__':
    window = ctk.CTk()
    window.title("Calendar Widget")
    ctk.set_appearance_mode("dark")

    values = [49, 76, 61, 65, 51, 24, 9, 29, 53, 24]

    CTkGraph(window, values).pack(side="left", padx=20, pady=20)

    CTkGraph(window, values, width=250, height=200, fg_color="#FF7761", graph_color="#FF7761",
             graph_fg_color="#FF5330", title="Screentime", title_font_size=30, corner_radius=20).pack(side="left", padx=20, pady=20)

    window.mainloop()
