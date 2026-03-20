import flet as ft
import random
from playsound3 import playsound
import time
 
def main(page: ft.Page):
    page.title = "Trivia Quiz App"
    page.window_width = 600
    page.window_height = 500
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
 
    ranStuff_category = [
        {
            "question": "In basketball, a free throw is worth?",
            "choices": ["1 point", "0 points", "2 points", "3 points"],
            "answer": "1 point",
            "image": "Image/Basket.png"
        },
        {
            "question": "Mount Everest lies on the border of which two countries?",
            "choices": ["India and Pakistan", "Nepal and China", "Tibet and Vietnam", "China and Pakistan"],
            "answer": "Nepal and China",
            "image": "Image/Everest.png"
        },
        {
            "question": "Which African country was formerly known as Abyssinia?",
            "choices": ["Somalia", "Rwanda", "Tanzania", "Djibouti", "Ethiopia"],
            "answer": "Ethiopia",
            "image": "Image/africa.png"
        },
        {
            "question": "Octopuses have how many arms?",
            "choices": ["7 arms", "8 arms", "9 arms","76","67"],
            "answer": "8 arms",
            "image": "Image/Octo.png"
        },
        {
            "question": "Which country won the first FIFA World Cup (1930)?",
            "choices": ["Brazil", "Uruguay", "Italy", "Argentina", "Germany!!!"],
            "answer": "Uruguay",
            "image": "Image/WC.png"
        },
        {
            "question": "Which predator is nicknamed the 'King of the Savannah'?",
            "choices": ["Lion", "Ostrich", "Tiger", "Elephant", "F2 Stealth Bomber"],
            "answer": "Lion",
            "image": "Image/animals.png"
        },
        {
            "question": "Which bird, native to the African savannah, is the largest flightless bird?",
            "choices": ["Penguin", "Hen", "Eagle", "Ostrich","IDK","My S24 Samsung Galaxy Ultra"],
            "answer": "Ostrich",
            "image": "Image/bird.png"
        },
        {
            "question": "What is the name of the galaxy that contains our solar system?",
            "choices": ["Supernova", "Chiron", "Milky Way", "Twix", "M&MS","Kitkat","Hollow Purple"],
            "answer": "Milky Way",
            "image": "Image/gala.png"
        },
        {
            "question": "Which planet has the fastest orbit around the Sun?",
            "choices": ["Earth", "Mercury", "Saturn", "None of the ones listed"],
            "answer": "Mercury",
            "image": "Image/solar.png"
        },
        {
            "question": "What country is the largest producer of coffee in the world?",
            "choices": ["Ethiopia", "India", "Brazil"],
            "answer": "Brazil",
            "image": "Image/coffe.png"
        }
    ]
 
    cars_category = [
        {
            "question": "Which is the faster car?",
            "choices": ["Chevy SS", "mk5 BMW"],
            "answer": "Chevy SS",
            "image": "Image/mk5.png"
        },
        {
            "question": "Which company made this engine?",
            "choices": ["Pagani", "Koenigsegg", "Ferrari", "Bugatti", "Mazda", "Bently", "Fiat", "Citroen", "Temu"],
            "answer": "Mazda",
            "image": "Image/brap.png"
        },
        {
            "question": "What is this car known for?",
            "choices": ["For being the mk5 supra", "For being a BMW car", "It's an Ferrari car"],
            "answer": "For being a BMW car",
            "image": "Image/mk5.png"
        },
        {
            "question": "What happened on November 30th, 2013?",
            "choices": ["When Paul Walker crashed his Porsche Carrera GT", "Someone's Birthday", "Inpedependence day of USA!!!"],
            "answer": "When Paul Walker crashed his Porsche Carrera GT",
            "image": "Image/fah.png"
        },
        {
            "question": "Which movie featured the Toyota Trueno car?",
            "choices": ["2 Fast 2 Furious", "Initial D", "Gran Turismo", "Tokyo DRIFT!!!"],
            "answer": "Initial D",
            "image": "Image/trueno.png"
        },
        {
            "question": "What car is this? (It's obv a mustang chat...)",
            "choices": ["Jeep", "Mustang", "Chevrolet", "Dodge"],
            "answer": "Mustang",
            "image": "Image/cobra.png"
        },
        {
            "question": "Which is the faster car?",
            "choices": ["Jesko", "Chiron", "Ford Raptor", "A15"],
            "answer": "Jesko",
            "image": "Image/jesko.png"
        },
        {
            "question": "Which is better overall?",
            "choices": ["The C8 ZR1", "Dodge Viper", "Toyota Corrola", "Honda Civic"],
            "answer": "The C8 ZR1",
            "image": "Image/c8.png"
        },
        {
            "question": "Name the soccer player who is from Georgia and his car that he drives",
            "choices": ["Kvaratskhelia who drives an AMG GTR", "Hakimi who drives an GTR-35", "Maradona who drives an Jesko", "Buffon who drives an Honda NSX", "Maldini who drives an Huracan"],
            "answer": "Kvaratskhelia who drives an AMG GTR",
            "image": "Image/georgia.png"
        },
        {
            "question": "Which car does Erling Haaland use as his daily?",
            "choices": ["Audi RS6 Avant", "Jesko", "Chiron", "LFA"],
            "answer": "Audi RS6 Avant",
            "image": "Image/haaland.png"
        }
    ]
 
    ranStufftwo_category = [
        {
            "question": "What gas do plants absorb from the atmosphere for photosynthesis?",
            "choices": ["Oxygen", "Nitrogen", "Carbon dioxide", "Hydrogen"],
            "answer": "Carbon dioxide",
            "image": "Image/co2.png"
        },
        {
            "question": "What is the longest bone in the human body?",
            "choices": ["Humerus", "Femur", "Tibia", "Radius"],
            "answer": "Femur",
            "image": "Image/femur.png"
        },
        {
            "question": "Who was the first person to walk on the Moon?",
            "choices": ["Michel Collins ", "Neil Armstrong", "Yuri Gagarin"],
            "answer": "Neil Armstrong",
            "image": "Image/moon.png"
        },
        {
            "question": "What is the currency used in the United Kingdom?",
            "choices": ["Euro", "Dollar", "Pound"],
            "answer": "Pound",
            "image": "Image/england.png"
        },
        {
            "question": "What is H2O commonly known as?",
            "choices": ["Salt", "Water", "Oxygen", "Hydrogen"],
            "answer": "Water",
            "image": "Image/h20.png"
        },
        {
            "question": "Which country has the largest population in the world (as of recent estimates)?",
            "choices": ["China", "India", "U.S", "Indonesia"],
            "answer": "India",
            "image": "Image/population.png"
        },
        {
            "question": "Which metal is most commonly used to make electrical wires?",
            "choices": ["Gold ", "Silver", "Copper", "Iron"],
            "answer": "Copper",
            "image": "Image/wires.png"
        },
        {
            "question": "Which language has the most native speakers in the world?",
            "choices": ["Hindi", "Spanish", "Mandarin Chinese", "English"],
            "answer": "Mandarin Chinese",
            "image": "Image/language.png"
        },
        {
            "question": "Which river is the longest in South America?",
            "choices": ["Orinoco River", "Amazon River", "Magdalena River", "Paraná River"],
            "answer": "Amazon River",
            "image": "Image/amazon.png"
        },
        {
            "question": "Which scientist is known for discovering radioactivity?",
            "choices": ["Niels Bohr", "Albert Einstein", "Isaac Newton", "Marie Curie"],
            "answer": "Marie Curie",
            "image": "Image/marie.png"
        }
    ]
 
    current_question_index = 0
    score = 0
    random_questions = []
    answered = False
    selected_category = None
 
    sound1 = None
    sound2 = None
 
    question_text = ft.Text(size=22, weight="bold")
    feedback_text = ft.Text(size=18, weight="bold")
    questionImage = ft.Image(src="nosource.png")
 
    options_column = ft.Column()
    radio_group = ft.RadioGroup(content=options_column)
 
    next_button = ft.ElevatedButton("Submit")
 
    category_selection = ft.Dropdown(
        label="Choose a category",
        options=[
            ft.dropdown.Option("Common Knowledge (Random Facts)"),
            ft.dropdown.Option("Cars (For the smart people who know's true ball!!!)"),
            ft.dropdown.Option("Common Knowledge Part 2 (Harder Random Stuff)")
        ]
    )
 
    start_button = ft.ElevatedButton("Start Quiz")
 
    def start(e):
        nonlocal current_question_index, score, random_questions, answered, selected_category, sound1, sound2
 
        selected_category = category_selection.value
        if selected_category is None:
            feedback_text.value = "Select a category first."
            playsound("assets/audio/boom.mp3", block=False)
            page.add(feedback_text)
            page.update()
            return
 
        if sound1:
            sound1.stop()
        if sound2:
            sound2.stop()
 
        if selected_category == "Common Knowledge (Random Facts)":
            random_questions = ranStuff_category
            sound1 = playsound("assets/audio/Bike.mp3", block=False)
 
        elif selected_category == "Cars (For the smart people who know's true ball!!!)":
            random_questions = cars_category
            sound2 = playsound("assets/audio/lv999.mp3", block=False)
 
        elif selected_category == "Common Knowledge Part 2 (Harder Random Stuff)":
            random_questions = ranStufftwo_category
            sound1 = playsound("assets/audio/Bike.mp3", block=False)
 
        random.shuffle(random_questions)  # ADDED
 
        current_question_index = 0
        score = 0
        answered = False
 
        show_question()
 
    def show_question():
        nonlocal answered
        answered = False
        page.controls.clear()
 
        question_data = random_questions[current_question_index]
        question_text.value = question_data["question"]
        questionImage.src = question_data["image"]
 
        feedback_text.value = ""
        feedback_text.color = None
 
        radio_group.value = None
        options_column.controls.clear()
 
        for option in question_data["choices"]:
            options_column.controls.append(ft.Radio(value=option, label=option))
 
        next_button.text = "Submit"
 
        page.add(
            ft.Column(
                [
                    question_text,
                    questionImage,
                    radio_group,
                    feedback_text,
                    ft.Row([next_button], alignment=ft.MainAxisAlignment.CENTER)
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
            )
        )
        page.update()
 
    def next_question(e):
        nonlocal current_question_index, score, answered
 
        if not answered:
 
            if radio_group.value is None:
                return
 
            correct_answer = random_questions[current_question_index]["answer"]
 
            if radio_group.value == correct_answer:
                score += 1
                feedback_text.value = "Correct!"
                playsound("assets/audio/good.mp3", block=False)
 
            else:
                feedback_text.value = f"Incorrect! Correct answer: {correct_answer}"
                playsound("assets/audio/FAHHH.mp3", block=False)
 
            answered = True
            next_button.text = "Next"
            page.update()
 
        else:
 
            current_question_index += 1
 
            if current_question_index < len(random_questions):
                show_question()
 
            else:
                results()
 
    def results():
        page.controls.clear()
 
        if score < 6:
            playsound("assets/audio/LOL.mp3", block=False)
 
        elif score > 6:
            playsound("assets/audio/yay.mp3", block=False)
 
        elif score == 6:
            playsound("assets/audio/LOL.mp3", block=False)
 
        page.add(
            ft.Column(
                [
                    ft.Text("Quiz Finished!", size=30, weight="bold"),
                    ft.Text(f"Final Score: {score} / {len(random_questions)}", size=20),
                    ft.ElevatedButton("Restart Quiz", on_click=restart)
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
            )
        )
 
        page.update()
 
    def restart(e):
 
        page.controls.clear()
 
        page.add(
            ft.Column(
                [
                    ft.Text("Welcome to the Trivia Quiz!", size=30, weight="bold"),
                    category_selection,
                    start_button
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
            )
        )
 
        page.update()
 
    next_button.on_click = next_question
    start_button.on_click = start
 
    page.add(
        ft.Column(
            [
                ft.Text("Welcome to the Trivia Quiz!", size=30, weight="bold"),
                category_selection,
                start_button
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )
    )
 
ft.app(target=main, assets_dir="Assets")