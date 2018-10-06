from mycroft import MycroftSkill, intent_file_handler

class Skill(MycroftSkill):
    """The skill class"""
    def __init__(self):
        """Init"""
        MycroftSkill.__init__(self)

    @intent_file_handler('check.email.intent')
    def handle_email(self, message):
         """intent handle"""
         pass
def create_skill():
    return Skill()
