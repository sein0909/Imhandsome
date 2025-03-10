import flet as ft

def main(page: ft.Page):
    아 = ft.TextField(label="name of the item")
    쇼핑 = ft.Column()

    def add(e):
        if 아.value:
            쇼핑.controls.append(ft.Text(아.value))
            아.value = ""
        page.update()

    def remove(e):
        if 쇼핑.controls:
            빼기 = 쇼핑.controls[0].value
            쇼핑.controls.pop(0) 
        page.update()

    def clear(e):
        쇼핑.controls.clear()
        page.update()

    page.add(
        ft.Row([아, ft.ElevatedButton("add", on_click=add)]),
        쇼핑, ft.Row([ft.ElevatedButton("remove it", on_click=remove),ft.ElevatedButton("clear it", on_click=clear)])
    )

ft.app(target=main)
