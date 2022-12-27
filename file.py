#1

class animals:
    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age

    def say(self, text):
        print(text)

class mammals(animals):
    def __init__(self, name, gender, age, color_wool, walking_upright):
        super().__init__(name, gender, age)
        self.color_wool = color_wool
        self.walking_upright = walking_upright

    def mam(self):
        print(f"I`m mammals and my name is {self.name}")

class human(mammals):
    def __init__(self, name, gender, age, color_wool, walking_upright, surname, level_of_education, height):
        super().__init__(name, gender, age, color_wool, walking_upright)
        self.surname = surname                                                     
        self.level_of_education = level_of_education                                        
        self.height = height      

    def edu(self):
        print(f"My level of education is {self.level_of_education}")

class cat(mammals):
    def __init__(self, name, gender, age, color_wool, walking_upright, bald):
        super().__init__(name, gender, age, color_wool, walking_upright)
        self.bald = bald
    
    def say_meow():
        print("Meow!")

class dog(mammals):
    def __init__(self, name, gender, age, color_wool, walking_upright, curly):
        super().__init__(name, gender, age, color_wool, walking_upright)
        self.curly = curly   
    
    def say_woof():
        print("Woof!")                                             


#2 and 3

class student(human):
    def __init__(self, name, gender, age, color_wool, walking_upright, surname, level_of_education, height, hw_count):
        super().__init__(self, name, gender, age, color_wool, walking_upright, surname, level_of_education, height)
        self.hw_count = hw_count

    def count(self):
        print(f"Я, {self.name}, сдал такое количество домашних работ: {self.hw_count}")

    def __lt__(self, other):
        return int(self.hw_count) < int(other.hw_count)

    def __eq__(self, other):
        return int(self.hw_count) == int(other.hw_count)

    def __ne__(self, other):
        return int(self.hw_count) != int(other.hw_count)

    def __gt__(self, other):
        return int(self.hw_count) > int(other.hw_count)


