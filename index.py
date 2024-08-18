import flet as ft
def summit(e):
    command = userinput.value
    userinput.value = ""

userinput = ft.TextField(width=720,height=200,on_submit=summit)

def main(page: ft.page):
    page.add(userinput)






ft.app(target=main)