import random



re = input("¿Quieres tirarn el dado? (Y/N)")


while re == "Y":
        
        tirardado = random.randint(1,6)
            
        if tirardado == 1:
                    print("[-----]")
                    print("[     ]")
                    print("[  0  ]")
                    print("[     ]")
                    print("[-----]")

        if tirardado == 2:
                    print("[-----]")
                    print("[  0  ]")
                    print("[     ]")
                    print("[  0  ]")
                    print("[-----]")

        if tirardado == 3:
                    print("[-----]")
                    print("[  0  ]")
                    print("[  0  ]")
                    print("[  0  ]")
                    print("[-----]")

        if tirardado == 4:
                    print("[-----]")
                    print("[0   0]")
                    print("[     ]")
                    print("[0   0]")
                    print("[-----]")

        if tirardado == 5:
                    print("[-----]")
                    print("[0   0]")
                    print("[  0  ]")
                    print("[0   0]")
                    print("[-----]")

        if tirardado == 6:
                    print("[-----]")
                    print("[0   0]")
                    print("[0   0]")
                    print("[0   0]")
                    print("[-----]")

        re = input("Quieres tirar el dado (Y/N)")

