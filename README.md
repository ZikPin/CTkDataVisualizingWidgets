# Custom-widgets-for-CTk
Custom calendar, graph, chart, and scrollable frame widgets

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
