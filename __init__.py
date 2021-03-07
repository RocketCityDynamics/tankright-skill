from mycroft import MycroftSkill, intent_file_handler


class Tankright(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('tankright.intent')
    def handle_tankright(self, message):
        self.speak_dialog('tankright')

        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(in1,GPIO.OUT)
        GPIO.setup(in2,GPIO.OUT)
        GPIO.setup(en,GPIO.OUT)
        GPIO.setup(in3,GPIO.OUT)
        GPIO.setup(in4,GPIO.OUT)
        GPIO.setup(en2,GPIO.OUT)
        p=GPIO.PWM(en,1000)
        p2=GPIO.PWM(en2,1000)
        # tank forward
        # Motor power setup here. Just one speed.
        p.start(40)
        p2.start(45) # l motor is a little weaker on my setup.
        # Compensate with slightly more juice going to the weaker motor to help it drive straighter.

        #Below is from Backwards function to spin inside motor backwards, bit like an e-brake."
        GPIO.output(in1,GPIO.HIGH)
        GPIO.output(in2,GPIO.LOW)
        GPIO.output(in3,GPIO.HIGH)
        GPIO.output(in4,GPIO.LOW)
        
        time.sleep(3) #This finally worked.
        
        #We then set all of the GPIO outputs to "low" to kill the power.
        GPIO.output(in1,GPIO.LOW)
        GPIO.output(in2,GPIO.LOW)
        GPIO.output(in3,GPIO.LOW)
        GPIO.output(in4,GPIO.LOW)


def create_skill():
    return Tankright()

