# Welcome to my pizza shop's behind the scenes!

flag = False
loop = True
# self type
from time import sleep


def printt(string, delay):
    for i in str(string):
        print(i, end="", flush=True)
        sleep(delay)


DISCOUNT = 0
language = input("English - 1, Spanish - 2 -- ")

if language == "1":
    # welcome!
    printt("Welcome to Adith Pizzeria.\n", 0.005)
    # order name
    name = input("What would you like your order name to be? ")
    # boss's command pallete
    if name == "Boss" or name == "boss":
        printt("Hello Boss. Menu?", 0.005)
        menu = input("Would you like the menu?y/n")
        if menu == "y" or menu == "Y":
            print(
                "Menu \n Follow exact capitlization!\n 1. Large Pizza - $12 \n 2. Medium Pizza - $8 \n 3. Small Pizza - $5 \n 4. Thin Crust - No extra charge\n O. olives-.50 \n A. Artichokes-.50 \n P. Pinaples-.50 \n 5. Thick Crust - $1 extra charge!\n Drinks \n 6. Cola - $2 \n 7. Orange Juice - $2 \n 8. Water - Free \n Dessert \n 9. Ice Cream - $2 \n 10. Brownie- $1 \n 11. Cookie- 50 cents \n end. End Order \n menu. menu ")
        else:
            printt("Ok. Your shop works perfectly", 0.005)
    # normal command pallete
    else:
        printt("Welcome to my fully automated pizza shop! Here is my menu", 0.005)
        print(
            "\n Follow exact capitlization!\n 1. Large Pizza - $12 \n 2. Medium Pizza - $8 \n 3. Small Pizza - $5 \n 4. Thin Crust - No extra charge\n O. olives-.50 \n A. Artichokes-.50 \n P. Pinaples-.50 \n 5. Thick Crust - $1 extra charge!\n Drinks \n 6. Cola - $2 \n 7. Orange Juice - $2 \n 8. Water - Free \n Dessert \n 9. Ice Cream - $2 \n 10. Brownie- $1 \n 11. Cookie- 50 cents \n end. End Order \n menu. menu ")
    # define cost and number
    cost = 0
    number = 0

    # ordering mechanisim
    while loop == True:
        order = input("What would you like? Print the number of your desired item to buy.")
        if order == "end" or order == "End":
            loop = False
        elif order == "1":
            number_things = eval(input("How many would you like?"))
            cost = cost + int(number_things) * 12
            number = number + 1
        elif order == "2":
            number_things = eval(input("How many would you like?"))
            cost = cost + int(number_things) * 8
            number = number + 1
        elif order == "3":
            number_things = eval(input("How many would you like?"))
            cost = cost + int(number_things) * 5
            number = number + 1
        elif order == "4":
            number_things = eval(input("How many would you like"))
            printt("FREE", 0.005)
            cost = cost + int(number_things) * 0
        elif order == "5":
            number = number + 1
            number_things = eval(input("How many would you like?"))
            cost = cost + int(number_things) * 1
        elif order == "6":
            number = number + 1
            number_things = eval(input("How many would you like?"))
            cost = cost + int(number_things) * 2
            number = number + 1
        elif order == "7":
            number = number + 1
            number_things = eval(input("How many would you like?"))
            cost = cost + int(number_things) * 2
            number = number + 1
        elif order == "8":
            number = number + 1
            number_things = eval(input("How many would you like?"))
            cost = cost + int(number_things) * 0
            printt("FREE!!", 0.005)
        elif order == "9":
            number = number + 1
            number_things = eval(input("How many would you like?"))
            cost = cost + int(number_things) * 2
        elif order == "10":
            number_things = eval(input("How many would you like?"))
            number = number + 1
            cost = cost + int(number_things) * 1
        elif order == "11":
            number_things = eval(input("How many would you like?"))
            number = number + 1
            cost = cost + int(number_things) * 0.050
        elif order == "A" or order == "a":
            number_things = eval(input("How many would you like?"))
            number = number + 1
            cost = cost + int(number_things) * 0.050
        elif order == "O" or order == "o":
            number_things = eval(input("How many would you like?"))
            number = number + 1
            cost = cost + int(number_things) * 0.050
        elif order == "P" or order == "p":
            number_things = eval(input("How many would you like?"))
            number = number + 1
            cost = cost + int(number_things) * 0.050
        elif order == "menu" or order == "Menu":
            print(
                "Menu \n 1. Large Pizza - $12 \n 2. Medium Pizza - $8 \n 3. Small Pizza - $5 \n 4. Thin Crust - No extra charge\n O. olives-.50 \n A. Artichokes-.50 \n P. Pinaples-.50 \n 5. Thick Crust - $1 extra charge!\n Drinks \n 6. Cola - $2 \n 7. Orange Juice - $2 \n 8. Water - Free \n Dessert \n 9. Ice Cream - $2 \n 10. Brownie- $1 \n 11. Cookie- 50 cents \n End. End Order \n menu. menu ")
        else:
            break
    DISCOUNT = input("What is the discount code?(ENTER 5 FOR 5 DOLLARS OFF!!!!)")
    if DISCOUNT == "5":
        cost = cost - 5
    else:
        printt("OK your loss.", 0.005)

    sales = cost + number
    tip = input("What is your tip?(Whole number. No decimals...)")
    cost = cost + int(tip)
    if name == "Boss" or name == "boss":
        password = input("What is the password?")
        if password == "34745":
            cost = 0
            sales = 0
            print("Total cost for", number, "items is $", cost, "and your sales tax is", sales)
            restore = input("System Restoration needed?")
            if restore == "yes" or restore == "y" or restore == "Y":
                printt("System Restoration Started\n", 0.05)
                printt("1------2------3------4------5\n", 0.5)
                printt("System Restoration Completed\n", 0.05)
                number == 0
                cost == 0
                sales == 0
                print("\nTotal cost for", number, "items is $", cost, "and your sales tax is", sales)
            elif restore == "no" or restore == "No" or restore == "n" or restore == "N":
                printt("Ok, Bye", 0.005)
                flag = True
        else:
            printt("Boss system failed.", 0.005)



    else:
        print("Total cost for", number, "items is $", cost, "and your sales tax is", sales)
        print("Thank You,", name, "for eating at Adiths Pizzeria." ,0.005)
        flag = True
        printt(
            "Your pizza can be found at: https://bit.ly/whatyoupaidfor. You have to copy and paste the link in a different tab, or else it will give you an error. Idk why.",
            0.005)

elif language == "2":
    # welcome!
    printt("Bienvenidos a Adith Pizzeria.\n", 0.005)
    # order name
    name = input("Qual es tu nombre? ")
    # boss's command pallete
    if name == "Jefe" or name == "jefe":
        printt("Hola Jefe. Menu?", 0.005)
        menu = input("Te gustaria el meny?s/n")
        if menu == "s" or "S":
            print(
                "Menú \n ¡Siga las mayúsculas exactas!\n 1. Pizza grande - $12 \n 2. Pizza mediana - $8 \n 3. Pizza pequeña - $5 \n 4. Masa fina - Sin cargo adicional\n O. aceitunas - 0,50 \n A. Alcachofas - 0,50 \n P. Piñas - 0,50 \n 5. Masa gruesa: ¡cargo adicional de $1!\n Bebidas \n 6. Cola - $2 \n 7. Jugo de naranja - $2 \n 8. Agua - Gratis \n Postre \n 9. Helado - $2 \n 10. Brownie - $1 \n 11. Galleta - 50 centavos \n fin. Menú Finalizar pedido \n. menú")
        else:
            printt("Está bien. Tu tienda funciona perfectamente.", 0.005)
    # normal command pallete
    else:
        printt("¡Bienvenido a mi pizzería totalmente automatizada! Aquí está mi menú", 0.005)
        print(
            "\n ¡Siga las mayúsculas exactas!\n 1. Pizza grande - $12 \n 2. Pizza mediana - $8 \n 3. Pizza pequeña - $5 \n 4. Masa fina - Sin cargo adicional\n O. aceitunas - 0,50 \n A. Alcachofas - 0,50 \n P. Piñas - 0,50 \n 5. Masa gruesa: ¡cargo adicional de $1!\n Bebidas \n 6. Cola - $2 \n 7. Jugo de naranja - $2 \n 8. Agua - Gratis \n Postre \n 9. Helado - $2 \n 10. Brownie - $1 \n 11. Galleta - 50 centavos \n fin. Menú Finalizar pedido \n. menú")
    # define cost and number
    cost = 0
    number = 0

    # ordering mechanisim
    while loop == True:
        order = input("¿Qué le gustaría? Imprima el número de su artículo deseado para comprar.")
        if order == "fin":
            loop = False
        elif order == "1":
            number_things = eval(input("¿Cuantos te gustaria?"))
            cost = cost + int(number_things) * 12
            number = number + 1
        elif order == "2":
            number_things = eval(input("¿Cuantos te gustaria?"))
            cost = cost + int(number_things) * 8
            number = number + 1
        elif order == "3":
            number_things = eval(input("¿Cuantos te gustaria?"))
            cost = cost + int(number_things) * 5
            number = number + 1
        elif order == "4":
            number_things = eval(input("¿Cuantos te gustaria?"))
            printt("Gratis!", 0.005)
            cost = cost + int(number_things) * 0
        elif order == "5":
            number = number + 1
            number_things = eval(input("¿Cuantos te gustaria?"))
            cost = cost + int(number_things) * 1
        elif order == "6":
            number = number + 1
            number_things = eval(input("¿Cuantos te gustaria?"))
            cost = cost + int(number_things) * 2
            number = number + 1
        elif order == "7":
            number = number + 1
            number_things = eval(input("¿Cuantos te gustaria?"))
            cost = cost + int(number_things) * 2
            number = number + 1
        elif order == "8":
            number = number + 1
            number_things = eval(input("¿Cuantos te gustaria?"))
            cost = cost + int(number_things) * 0
            printt("Gratis!!", 0.005)
        elif order == "9":
            number = number + 1
            number_things = eval(input("¿Cuantos te gustaria?"))
            cost = cost + int(number_things) * 2
        elif order == "10":
            number_things = eval(input("¿Cuantos te gustaria?"))
            number = number + 1
            cost = cost + int(number_things) * 1
        elif order == "11":
            number_things = eval(input("¿Cuantos te gustaria?"))
            number = number + 1
            cost = cost + int(number_things) * 0.050
        elif order == "A" or "a":
            number_things = eval(input("¿Cuantos te gustaria?"))
            number = number + 1
            cost = cost + int(number_things) * 0.050
        elif order == "O" or "o":
            number_things = eval(input("¿Cuantos te gustaria?"))
            number = number + 1
            cost = cost + int(number_things) * 0.050
        elif order == "P" or "p":
            number_things = eval(input("¿Cuantos te gustaria?"))
            number = number + 1
            cost = cost + int(number_things) * 0.050
        elif order == "menu":
            print(
                "\n¡Siga las mayúsculas exactas!\n 1. Pizza grande - $12 \n 2. Pizza mediana - $8 \n 3. Pizza pequeña - $5 \n 4. Masa fina - Sin cargo adicional\n O. aceitunas - 0,50 \n A. Alcachofas - 0,50 \n P. Piñas - 0,50 \n 5. Masa gruesa: ¡cargo adicional de $1!\n Bebidas \n 6. Cola - $2 \n 7. Jugo de naranja - $2 \n 8. Agua - Gratis \n Postre \n 9. Helado - $2 \n 10. Brownie - $1 \n 11. Galleta - 50 centavos \n fin. Menú Finalizar pedido \n. menú")
        else:
            break
    DISCOUNT = input("¿Cuál es el código de descuento?(INGRESA 5 POR 1 DÓLAR DE DESCUENTO!!!!)")
    if DISCOUNT == "5":
        cost = cost - 1
    else:
        printt("Ok, su pérdida.", 0.005)

    sales = cost + number
    tip = input("¿Cuál es tu propina? (Número entero. Sin decimales...)")
    cost = cost + int(tip)
    if name == "Jefe" or name == "jefe":
        password = input("¿Cual es la contraseña?")
        if password == "34745":
            cost = 0
            sales = 0
            print("Costo total de", number, "los artículos son $", cost, "y su impuesto sobre las ventas es", sales,
                  0.005)
            restore = input("¿Se necesita restauración del sistema?")
            if restore == "S" or restore == "s":
                printt("Restauración del sistema iniciada\n", 0.05)
                printt("1------2------3------4------5\n", 0.5)
                printt("Restauración del sistema completado\n", 0.05)
                number == 0
                cost == 0
                sales == 0
                print("Costo total de", number, "los artículos son $", cost, "y su impuesto sobre las ventas es", sales)
            elif restore == "no":
                printt("Ok, adios!", 0.005)
                flag = True
        else:
            printt("El sistema de jefe falló.", 0.005)



    else:
        print("Costo total de", number, "los artículos son $", cost, "y su impuesto sobre las ventas es", sales)
        print("Grasias,", name, "por comer en Adiths Pizzeria!")
        flag = True
        printt(
            "Tu pizza se puede encontrar en: https://bit.ly/whatyoupaidfor. Tienes que copiar y pegar el enlace en una pestaña diferente, o de lo contrario te dará un error. No se porque.",
            0.005)
else:
    printt(
        "A error has occured.Please contact me. Discord = -Avdol-#1409, Matrix = -avdol-:matrix.org, Email = adith08@gmail.com, with a report.",
        0.005)
