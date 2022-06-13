class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self, name, age, tracks, score):
        pass
        self.name = name
        self.age = age
        self.tracks = tracks
        self.score = score

    def change_name(self, newName):
        self.name = newName

    def change_age(self, newAge):
        self.age = newAge

    def add_track(self, trackItem):
        self.tracks.append(trackItem)

    def get_score(self):
        return self.score

    def update_score(self, newScore):
        self.score = newScore


Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)

# Expected methods
Bob.change_name("Shalom")
Bob.change_age(25)
Bob.add_track("Full Stack")
Bob.get_score()

Bob.update_score(45.3)
Bob.add_track("Full Stack")

print("\n")
print(Bob.name)
print(Bob.age)
print(Bob.tracks)
print(Bob.score)
