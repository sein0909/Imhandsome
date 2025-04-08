import flet as ft

def main(page: ft.Page):
    quotes = {
        'Korean': '부엉이 바위로 가자. ',
        'English': 'Lets go to the owl rock.',
        'Spanish': 'Vamos a Owl Rock.'
    }
    og = ft.Text(quotes['Korean'])
    tq = ft.Text("",)
    lr = ft.RadioGroup(
    content=ft.Column([ft.Radio(value="English", label="English"),
            ft.Radio(value="Spanish", label="Spanish"),
            ft.Radio(value="Korean", label="Original:korean"),]))
    
    def trans(e):
        sl = lr.value
        tq.value = quotes[sl]
        page.update()
    
    lr.on_change = trans
    page.add(
        ft.Column([ft.Divider(),ft.Text("Original"),og,ft.Divider(),lr,ft.Divider(),ft.Text("Translated"),tq],))


ft.app(target=main)