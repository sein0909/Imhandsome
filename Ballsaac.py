import flet as ft
import random

def main(page: ft.Page):
    slider = ft.RangeSlider(
        min=0,
        max=100,
        start_value=0,  
        end_value=100,
        label="{value}"
    )
    text = ft.Text("")
    def randomassnum(e):
        jae = int(slider.start_value) 
        Zot = int(slider.end_value)
        if jae <= Zot:
            ran = random.randint(jae, Zot) 
            text.value = f"{ran}"
        page.update()

    button = ft.ElevatedButton(
        text="generate",
        on_click=randomassnum
    )

    page.add(
        ft.Column(
            controls=[
                ft.Text("Range"),
                slider,
                button,
                text
            ]
        )
    )
ft.app(target=main)