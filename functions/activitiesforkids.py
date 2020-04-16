def run(*kids):
    for kid in kids:
        print(f"{kid} ran like a fool!")

def swing(*kids):
    for kid in kids:
        print(f"{kid} swung like a fool! ")

def slide(*kids):
    for kid in kids:
        print(f"{kid} slid like a fool! ")

def hide_and_seek(*kids):
    for kid in kids:
        print(f"{kid} hid like a fool! ")

run("Pam", "Sam", "Andrea", "Will")
swing("Marybeth", "Ariel", "Kevin", "Courtney")
slide("Mike", "Jack", "Jennifer", "Earl")
hide_and_seek("Henry", "Heather", "Hayley", "Hugh")