class Human:
    height = 180
    weight= 80
    eye_color = 'Blue'

    def __init__(self, name):
        self.weight = 175
        self.name = name
    def work(self):
        print('I am working')
    def sleep(self):
        print('I am trying to sleep')

Bob = Human('Bob')

print(Bob.height)
print(Bob.eye_color)
Bob.work()
Bob.sleep()

