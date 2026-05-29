from utils.table import Seat
from utils.openspace import Table
from utils.openspace import Openspace

new_collegues = ["Anna", "Dan", "Gaetan", "Guillermo", "Gunay", "Hiba", "Hussein", "Ibrahim", "Ibtihel", "Imad", "Iness", "Irene", "Jeong", "Mahalakshmi", "Max", "Neha", "Siegried", "Sitara", "Sooyoung", "Stephane", "Thi", "Uzair", "Victor", "Vanessa"]

Openspace_1 = Openspace(6)
Openspace_1.organize(new_collegues)
Openspace_1.display()
print(Openspace_1)