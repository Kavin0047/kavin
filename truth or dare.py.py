from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.popup import Popup
from kivy.uix.scrollview import ScrollView
from kivy.animation import Animation
from kivy.clock import Clock
import random


class TruthOrDareApp(App):
    def build(self):
        self.players = []
        self.scores = {}
        self.current_player_index = 0

        self.truths = [
            "What's the silliest thing you've ever done?",
             "What's the weirdest dream you've ever had?",
            "Have you ever sent a text to the wrong person?",
                "What's the most embarrassing thing you've done in public?",
                "If you could swap lives with anyone for a day, who would it be and why?",
                "What's the most memorable trip you've been on?",
                "What's the funniest thing that's ever happened to you?",
                "What's your most irrational fear?",
                "If you could time travel, what period would you visit and why?",
                "What's your most embarrassing childhood memory?",
                "If you had to switch lives with someone in this room, who would it be and why?",
                "What's the most daring thing you've ever done?",
                "What's the craziest thing you've done to impress someone?",
                "What's the weirdest food combination you've tried?",
                "What's the most adventurous thing you want to do?",
                "What's the most romantic thing someone has done for you?",
                "If you could erase one thing from your past, what would it be?",
                "What's the most embarrassing thing your parents have caught you doing?",
                "What's the most memorable party you've been to?",
                "If you could have any superpower, what would it be and why?",
                "Who is your best friend and why?",
                "Have you ever had a fight with your best friend? What was it about?",
                "What's the funniest thing you've done with your friends?",
                "Who in the group is most likely to get in trouble?",
                "What is the craziest thing you've done with friends?",
                "Who is the most reliable friend you have?",
                "What do you like most about your friend group?",
                "Have you ever lied to your friends about something important?",
                "What's a secret you have kept from your friends?",
                "Which friend do you admire the most and why?",
                "Have you ever had a crush on a friend's sibling?",
                "What is the most embarrassing thing you've done in front of your friends?",
                "Who is the funniest friend you have?",
                "What is the most adventurous thing you've done with friends?",
                "Have you ever gotten lost with a friend?",
                "Who is the most competitive friend in your group?",
                "Have you ever borrowed something from a friend and never returned it?",
                "Who is the most likely to be late in your friend group?",
                "What's the longest you've gone without talking to your best friend?",
                "Have you ever played a prank on a friend? What was it?",
                "What is your favourite subject in school/college and why?",
                "Have you ever bunked a class? If yes, what did you do instead?",
                "Who was your favourite teacher and why?",
                "What is your most embarrassing school/college moment?",
                "Have you ever cheated on a test?",
                "Who is your school/college crush?",
                "What was your favourite school/college event?",
                "Have you ever been in detention? If yes, why?",
                "What's the best memory you have from school/college?",
                "Who is the most interesting person you have met at school/college?",
                "Have you ever forgotten to do your homework?",
                "What was the funniest thing that happened in your classroom?",
                "Who is the most popular person in your school/college?",
                "Have you ever pulled an all-nighter for an exam?",
                "What's your favourite place to hang out at school/college?",
                "Who is the strictest teacher you have had?",
                "Have you ever participated in a school/college play?",
                "What was your favourite sports activity in school/college?",
                "Have you ever fallen asleep in class?",
                "What is the most memorable field trip you have gone on?",
        ]

        self.dares = [
            "Imitate a famous South Indian movie star for 1 minute.",
                "Speak in a different South Indian language for the next 5 minutes.",
                "Do a traditional dance move.",
                "Tell a joke in your mother tongue.",
                "Recite a dialogue from a popular South Indian movie.",
                "Pretend to be a news anchor reporting a funny incident.",
                "Act like a famous comedian from South India.",
                "Mimic the sound of an animal for 30 seconds.",
                "Act like you’re in a soap opera for 1 minute.",
                "Do a funny dance for 1 minute.",
                "Pretend to be a chef and describe how to make a dosa.",
                "Imitate your favourite teacher for 1 minute.",
                "Sing a nursery rhyme in your mother tongue.",
                "Pretend to be a movie director and describe your next blockbuster.",
                "Do a funny impression of someone in the room.",
                "Pretend you are an alien and explain how you would react to South Indian food.",
                "Act like a baby until your next turn.",
                "Pretend you are a tour guide and describe a famous South Indian landmark.",
                "Do 10 jumping jacks while counting in your mother tongue.",
                "Pretend you are a fashion model and walk the runway.",
                "Do 20 push-ups.",
                "Sing a song chosen by the group.",
                "Imitate someone until another player can guess who you are.",
                "Do your best impression of a celebrity.",
                "Let someone tickle you for 30 seconds.",
                "Try to lick your elbow.",
                "Do a cartwheel.",
                "Balance a spoon on your nose for 10 seconds.",
                "Speak in an accent for the next 3 rounds.",
                "Let someone draw on your face with a pen.",
                "Do an impression of a famous politician.",
                "Hold your breath for 10 seconds.",
                "Do 10 squats while holding your breath.",
                "Walk across the room on your knees.",
                "Make a funny face and keep it that way until your next turn.",
                "Pretend you are a waiter and take snack orders from everyone in the group.",
                "Talk in a whisper for the next 3 rounds.",
                "Let another player redo your hairstyle.",
                "Do a silly dance for 30 seconds.",
                "Imitate your favorite cartoon character."
                "Pretend to be a famous South Indian celebrity giving an interview.",
                "Tell a funny story from your childhood.",
                "Act like a teacher and teach the group something funny.",
                "Pretend to be a dancer and perform a dance move.",
                "Imitate a famous politician from South India.",
                "Pretend you are a chef and describe a recipe in detail.",
                "Pretend to be a fitness instructor and give a workout demonstration.",
                "Pretend to be an animal for the next 2 minutes.",
                "Do an impression of your favourite movie villain.",
                "Sing a song in a different South Indian language.",
                "Pretend you are an actor and perform a dramatic scene.",
                "Pretend to be a doctor and describe a funny medical condition.",
                "Act like a grandparent giving advice to the younger generation.",
                "Pretend to be a stand-up comedian and tell a joke.",
                "Pretend to be a traffic police officer directing traffic.",
                "Pretend to be a street vendor selling something to the group.",
                "Pretend to be a cricket commentator and describe a match.",
                "Act like a singer performing at a concert.",
                "Pretend to be a detective solving a mystery.",
                "Pretend you are a parent scolding a child for something funny.",
        ]

        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        self.player_input = TextInput(hint_text='Enter player name', multiline=False, size_hint=(1, 0.1))
        layout.add_widget(self.player_input)

        add_player_button = Button(text='Add Player', background_color=(0.2, 0.6, 0.8, 1), size_hint=(1, 0.1))
        add_player_button.bind(on_press=self.add_player)
        layout.add_widget(add_player_button)

        choose_player_button = Button(text='Choose Player', background_color=(0.2, 0.8, 0.6, 1), size_hint=(1, 0.1))
        choose_player_button.bind(on_press=self.choose_player)
        layout.add_widget(choose_player_button)

        self.players_label = Label(text='Players: ', size_hint=(1, 0.1))
        layout.add_widget(self.players_label)

        self.scorecard_button = Button(text='View Scorecard', background_color=(0.8, 0.6, 0.2, 1), size_hint=(1, 0.1))
        self.scorecard_button.bind(on_press=self.show_scorecard)
        layout.add_widget(self.scorecard_button)

        self.question_label = Label(text='', font_size='18sp', size_hint=(1, 0.4))
        layout.add_widget(self.question_label)

        return layout

    def add_player(self, instance):
        player_name = self.player_input.text.strip()
        if player_name:
            self.players.append(player_name)
            self.scores[player_name] = 0
            self.update_players_label()
            self.player_input.text = ''

    def choose_player(self, instance):
        if self.players:
            self.current_player_index = random.randint(0, len(self.players) - 1)
            chosen_player = self.players[self.current_player_index]
            self.show_chosen_player_animation(chosen_player)
            self.ask_truth_or_dare(chosen_player)

    def ask_truth_or_dare(self, chosen_player):
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        label = Label(text=f'{chosen_player}, choose Truth or Dare:', font_size='18sp')
        layout.add_widget(label)
        truth_button = Button(text='Truth', background_color=(0.8, 0.4, 0.4, 1))
        dare_button = Button(text='Dare', background_color=(0.4, 0.8, 0.4, 1))

        truth_button.bind(on_press=lambda instance: self.show_question(instance, chosen_player, "Truth"))
        layout.add_widget(truth_button)
        dare_button.bind(on_press=lambda instance: self.show_question(instance, chosen_player, "Dare"))
        layout.add_widget(dare_button)
        
        self.popup = Popup(title='Truth or Dare', content=layout, size_hint=(0.8, 0.8))
        self.popup.open()

    def show_question(self, instance, chosen_player, choice):
        if choice == "Truth":
            question = random.choice(self.truths)
        else:
            question = random.choice(self.dares)
        self.question_label.text = f'{chosen_player}, your {choice} question is:\n\n{question}'
        self.popup.dismiss()  # Close the popup after selecting Truth or Dare

    def show_chosen_player_animation(self, chosen_player):
        layout = self.root
        player_label = Label(text=chosen_player, font_size='24sp')
        layout.add_widget(player_label)
        animation = Animation(pos_hint={'center_x': 0.5, 'center_y': 0.5}, duration=2)
        animation.start(player_label)
        Clock.schedule_once(lambda dt: layout.remove_widget(player_label), 2)  # Remove label after animation

    def update_players_label(self):
        self.players_label.text = 'Players: ' + ', '.join(self.players)

    def show_scorecard(self, instance):
        score_layout = GridLayout(cols=1, padding=10, spacing=10, size_hint_y=None)
        score_layout.bind(minimum_height=score_layout.setter('height'))
        for player, score in self.scores.items():
            score_layout.add_widget(Label(text=f'{player}: {score} points', size_hint_y=None, height=40))
        score_scroll = ScrollView(size_hint=(1, 0.8))
        score_scroll.add_widget(score_layout)
        close_button = Button(text='Close', size_hint=(1, 0.2))
        close_button.bind(on_press=lambda instance: score_popup.dismiss())
        score_layout.add_widget(close_button)
        score_popup = Popup(title='Scorecard', content=score_scroll, size_hint=(0.8, 0.8))
        score_popup.open()


if __name__ == '__main__':
    TruthOrDareApp().run()
