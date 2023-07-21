# Custom-widgets-for-CTk
Custom calendar, graph and chart widgets

## Calendar widget
A calendar widget consists of two parts title_bar and calendar frame. You can customize virtually everything in the widget. There is 
also an option to define the current day, if you define today_fg_color

Basic view on the left and with little customization on the right:

![image](https://github.com/ZikPin/Custom-widgets-for-CTk/assets/65452275/b27c41e8-c5bb-4788-92ad-f1e39bc6ab49)

To use just init the class and pass the `parent` (the only required argument). The parameters starting with title_bar are responsible for 
widgets inside the title bar and the ones starting with the calendar are responsible for the frame where the calendar is displayed

Creating the customized widget on the preview:
```
window = ctk.CTk()
window.title("Calendar Widget")
ctk.set_appearance_mode("dark")

# init calendar
calendar_widget = CTkCalendar(window, width=300, height=210, border_width=3, border_color="white",
                              fg_color="#020317", title_bar_border_width=3, title_bar_border_color="white",
                              title_bar_fg_color="#020F43", calendar_fg_color="#020F43", corner_radius=30,
                              title_bar_corner_radius=10, calendar_corner_radius=10, calendar_border_color="white",
                              calendar_border_width=3, calendar_label_pad=5,
                              today_fg_color="white", today_text_color="black")
calendar_widget.pack(side="left", padx=20)

window.mainloop()
```

## CTkGraph
The graph widgets lets you visualize the list of integer values as a graph. You can customize almost every part, except for corner radius of canvas (where the graph is drawn). You can also set a custom title and define its family, size and color. If you do not define a title
the widget will display only the graph

Default view on left and with customization on the right:

![image](https://github.com/ZikPin/Custom-widgets-for-CTk/assets/65452275/17b46820-d881-4f27-8ea9-7dd572d9d704)

To use just define parent and supply with list of integers. Example code:
```
window = ctk.CTk()
window.title("Calendar Widget")
ctk.set_appearance_mode("dark")

values = [49, 76, 61, 65, 51, 24, 9, 29, 53, 24]

CTkGraph(window, values, width=250, height=200, fg_color="#FF7761", graph_color="#FF7761",
         graph_fg_color="#FF5330", title="Screentime", title_font_size=30, corner_radius=20).pack(side="left", padx=20, pady=20)
```
## CTkChart
This is widget to create a chart representation of a dict[str, int]. It takes str of the dict as a key and a title
for certain stat and int or float for that matter as the value and draws it on the canvas. There are also
indicators like average and max value.

You can also set title, if you do not define it, it wont be rendered.

There are two values with tuple[bool, bool] format:
- stat_info_show: first bool is responsible for drawing the value in the stat, second for drawing title
- show_indicators: first bool is responsible for max value, second for average.

Default view on the left and with customization on the right:

![image](https://github.com/ZikPin/Custom-widgets-for-CTk/assets/65452275/e40ea973-77d0-42c4-b740-535c15ad5748)

Example code to create the widget:

```
window = ctk.CTk()
window.title("Calendar Widget")
ctk.set_appearance_mode("dark")

value = {'JJ': 5, 'OO': 0, 'WW': 7, 'TT': 3, 'GG': 15, 'FF': 10, 'HH': 1, 'PP': 12, "AA": 4}
CTkChart(window, value, corner_radius=20, fg_color="#032680", stat_color="#1D6FFF", chart_fg_color="#032680",
         show_indicators=(False, True), stat_info_show=(False, True), chart_arrow="none", border_width=2,
         border_color="white", indicator_line_color="#1942AC", indicator_text_color="#020F43", stat_width=15,
         stat_title_color="#1D6FFF", chart_axis_width=3, width=300, height=200).pack(side="left", pady=20, padx=20)
```
