import time
from dotenv import load_dotenv, find_dotenv
import os


load_dotenv(find_dotenv())
checking = float(os.environ.get("checking"))
savings = float(os.environ.get("savings"))


def withdraw(c_data=checking, s_data=savings):
    try:
        selections = input("would you like to withdraw from [C]hecking or [S]avings: ")
        amount = float(input("how much would you like to withdraw: "))
        if selections == "c":
            if amount <= c_data:
                print("dispensing cash...")
                time.sleep(2)
                c_data = c_data - amount
                print(f"your new account balance is ${c_data}")
            else:
                print("insufficient funds")
        if selections == "s":
            if amount <= s_data:
                print("dispensing cash...")
                time.sleep(2)
                s_data = s_data - amount
                print(f"your new account balance is ${s_data}")
            else:
                print("insufficient funds")
    except (ValueError, TypeError) as E:
        print(f"there has been an error\n{E}")


def deposit(c_data=checking, s_data=savings):
    try:
        selections = input("would you like to deposit to [C]hecking or [S]avings: ")
        amount = float(input("how much will you like to deposit: "))
        if selections == "c":
            print("depositing cash...")
            time.sleep(2)
            c_data = c_data + amount
            print(f"your new account balance is ${c_data}")
        if selections == "s":
            print("depositing cash...")
            time.sleep(2)
            s_data = s_data + amount
            print(f"your new account balance is ${s_data}")
    except Exception as E:
        print(f"you did not enter a valid number\n{E}")


def balance(c_data=checking, s_data=savings):
    print(f"checking balance ${c_data} || savings balance ${s_data}")


def transfer(c_data=checking, s_data=savings):
    try:
        selection = input("do you want transfer to [C]heckings or [S]avings: ")
        amount = float(input("how much would you like to transfer: "))
        if selection == "c":
            if amount <= s_data:
                print("transferring cash...")
                time.sleep(2)
                c_data = c_data + amount
                s_data = s_data - amount
                print(f"checking balance ${c_data} savings balance ${s_data}")
            else:
                print("insufficient funds")
        if selection == "s":
            if amount <= c_data:
                print("transferring cash...")
                time.sleep(2)
                s_data = s_data + amount
                c_data = c_data - amount
                print(f"savings balance is ${s_data} checking balance ${c_data}")
            else:
                print("insufficient funds")
    except ValueError as E:
        print("you did not enter a valid number")


def main():
    print("Welcome to hitham Bank")
    print("*********ATM**********")
    selection = input("[W]ithdraw  [D]eposit\n[B]alance   [T]ransfer\n>>>: ").lower()
    if selection == "w":
        withdraw()
    elif selection == "d":
        deposit()
    elif selection == "b":
        balance()
    elif selection == "t":
        transfer()


main()




