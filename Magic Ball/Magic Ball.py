import flet as ft
import random

def main(page: ft.Page ):

    def changeImage(e):
        imageList = ["Yes.png",
                     "No.png",
                     "AI exists.png",
                     "DONT CRY.png",
                     "It is certain.png",
                     "Next Friday.png",
                     "Without Doubt.png",
                     "DREAMS.png",
                     "NAH.png",
                     "Tough Luck.png"
                     ]
        
        chosenImage = random.choice(imageList)
        rdm_text.src = chosenImage
        ask.value = ""

        page.update()

    page.theme_mode = "LIGHT"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    rdm_text = ft.Image(height=400, width=600, src="200w.gif")
    ask = ft.TextField(label="Ask and then press ENTER", on_submit=changeImage)
    page.add(rdm_text, ask)

ft.run(main=main, assets_dir="MagicBall_Assets")