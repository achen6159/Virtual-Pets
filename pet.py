class Pet:

    def __init__(self, name):
        self.name = name
        self.x = 0
        self.y = 0
        self.direction = 0
        self.is_alive = True
        self.health = 10
        
            
    def eat(self):
        if self.is_alive:
            print(self.name + " goes Nom Nom Nom...")
        else:
            print("Dis boi ded.")

    def sleep(self):
        if self.is_alive:
            print("zzzzzzzzzzzzzz...")
        else:
            print("Dis pet in eternal sleep.")

    def play(self):
        if self.is_alive:
            print("Yippee!")
        else:
            print(self.name + " is dancing somewhere up in that big sky.")

    def rotate_right(self):
        self.direction += 1

        if self.direction == 4:
            self.direction = 0

    def rotate_left(self):
        self.direction -= 1

        if self.direction == -1:
            self.direction = 3

    def move(self):
        if self.direction == 0:
            self.y += 1
        elif self.direction == 1:
            self.x += 1
        elif self.direction == 2:
            self.y -= 1
        elif self.direction == 3:
            self.x -= 1
        

    def attack(self, other):
        if self.is_alive:
            other.health -= 2
            self.health -= 1
            print("That's tuff." + self.name + " has " + str(self.health) + \
                  " health " + other.name + " has " + str(other.health) + \
                  " health.")
            
            if self.health == 0:
                self.is_alive = False
                print(self.name + " is dead now.")

            elif other.health == 0:
                other.is_alive = False
                print(other.name + " is dead now.")
                
            
    
        
    def kill(self, other):
        print(self.name + " kills " + other.name + "!")
        print(other.name + " goes ouch and dies.")
        other.is_alive = False
        

    def __repr__(self):
        return "Name: " + self.name + \
               " [x=" + str(self.x) + \
               ", y=" + str(self.y) + \
               ", d=" + str(self.direction) + "]"
    
    
pet1 = Pet("Mere")
pet2 = Pet("Jaqueso")
pet3 = Pet("Lauryn")
