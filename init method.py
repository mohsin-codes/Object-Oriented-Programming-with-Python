class Computer:
    def __init__(self, cpu, ram):
        self.cpu = cpu
        self.ram = ram

    def config(self):
<<<<<<< HEAD
        print("Config is : ", self.ram, self.cpu)


com1 = Computer('i5', '16GB')
com2 = Computer('Ryzen 3', '8GB')
=======
        print(self.cpu, self.ram)

com1 = Computer("i5", "16GB")
com2 = Computer("Ryzen 5", "8GB")
>>>>>>> f7bcad5750b3f267ab283bf72653ac5057eaca9e

com1.config()
com2.config()