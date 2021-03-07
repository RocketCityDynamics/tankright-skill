from mycroft import MycroftSkill, intent_file_handler


class Tankright(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('tankright.intent')
    def handle_tankright(self, message):
        self.speak_dialog('tankright')


def create_skill():
    return Tankright()

