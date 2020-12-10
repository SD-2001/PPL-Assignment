class animals:
	def _init_(self):
		self.legs=4
		self.eyes=2
        class herbivores(animals):
            def food(self):
                print("Eats Herbs ,Shrubs and trees")
                class wild_animals(herbivores):
                        def place(self):
                            print("place : jungle")
                            class deer(wild_animals):
                                def thorns(self):
                                    print("2 thorns on head")
                            class elephant(wild_animals):
                                def sound(self):
                                    print("sound : ",Trumpet)
                                    
                    class domestic_animals(herbivores):
                        def place(self):
                            print("within humans habitat")
                        class cow(domestic_animals):
                            def shelter(self):
                                print("shelter : shed")
                            def baby(self):
                                print("baby of cow is called calf")
                            def sound(self):
                                s='moo'
                                print("sound : ",s)
                            def thorns(self):
                                print("2 thorns on head")
                        class horse(domestic_animals):
                            def shelter(self):
                                printf("shelter : stable")
                            def baby(self):
                                print("baby of horse is called foal")
                            def sound(self):
                                s=neigh
                                print("sound : ",s)
                        class sheep(domestic_animals):
                            def shelter(self):
                                print("shelter : Brothel")
                            def baby(self):
                                print("baby of sheep is called lamb")
                        class dog(domestic_animals):
                            def shelter(self):
                                print("shelter : kennel ")
                            def sound(self):
                                print("sound : bark")
                                    
            class carnivores(animals):
                def food(self):
                    print("Eats meat")
                    class wild_animals(carnivores):
                        def place(self):
                            print("place : jungle")
                        class lion(wild_animals):
                            def shelter(self):
                                print("shelter : Den")
                            def sound(self):
                                print("sound : purrs")
                        class tiger(wild_animals):
                            def shelter(self):
                                print("shelter : caves")
                            def sound(self):
                                print("sound : roars")

            class omnivores(animals):
                def food(self):
                    print("Eats both grass and meat")
                class wild_animals(omnivores):
                    def place(self):
                        print("place : jungle")
                    class bear(wild_animals):
                        def shelter(self):
                            print("shelter : lair")
                        def sound(self):
                            print("sound : growl")
                    class fox(wild_animals):
                        def shelter(self):
                            print("shelter : dens")
                        def sound(self):
                            print("sound : ow-wow-wow-wow")

x=animals()
y=cow()
y.place()
y.food()
y.shelter()
y.sound()
print(y.legs)
print(y.eyes)

        
