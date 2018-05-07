#!/usr/bin/env python3.6

import sys
import os
import pyperclip
from credential import Credential
from user_data import User
from pyfiglet import figlet_format
from termcolor import colored, cprint
from colorama import init
init(strip=not sys.stdout.isatty())

terminal_width = os.get_terminal_size().columns
def create_new_account(username, password):
    new_account = User(username, password)
    return new_account


def check_user_exists(userName):
    return User.user_exists(userName)


def save_account(account):
    account.save_user()


def delete_account(account):
    account.user_delete_account()        


def login_user(userName, passwrd):
    return User.confirm_user(userName, passwrd)


def user_change_password(userName, new_pass):
    return User.change_userpass(userName, new_pass)    


def create_new_profile(profile_name, profile_username = None, profile_email = None, profile_password = None):
    new_profile = Credential(profile_name, profile_username = None, profile_email = None, profile_password = None)
    return new_profile


def save_profile(new_profile):
    new_profile.save_profile()    


def delete_profile(profile):
    profile.delete_profile()


def generate_pass(length):
    generated_password = Credential.generate_random_password  
    return generated_password


def check_profile_exists(profile_name, profile_username = None, profile_email = None):
    return Credential.check_profile_exist(profile_name, profile_username = None, profile_email = None)



def search_profile(search):
    return Credential.search_profile(search)


def copy_password(search_item):
    return Credential.copy_credentials(search_item)

def display_profiles():
    return Credential.profile_list

def handle_short_codes(short_code):
    short_code = short_code.lower().replace(" ", "")
    if short_code == "np":
        cprint("You have entered a command to Create a New Profile".center(terminal_width), "black")
        print("Kindly input a Profile Name...example github")
        profile_name_entered = input()
        if not profile_name_entered:
            cprint("Your Profile Name Cannot Be Blank", "red")
        else:
            print("Kindly enter Username of the Profile Account(optional)")    
            profile_username_entered = input()
            print("Kindly enter Email of the Profile Account(optional)")
            profile_email_entered = input()
            print("Kindly enter Password of the Account(optional)")
            profile_password_entered = input()

            new_profile = Credential(profile_name_entered, profile_username_entered, profile_email_entered, profile_password_entered)
            profile_exist = check_profile_exists(profile_name_entered, profile_username_entered, profile_email_entered)
            if profile_exist:
                print("\n")
                cprint("New Profile Created".center(terminal_width),"green")
                print("\n")
            else:
                if not save_profile(new_profile):
                    print("\n")    
                    cprint("Your Profile Has Not Been Created.Kindly Attempt Once More".center(terminal_width), "red")
                    print("\n")

    elif short_code == "dp":
        show_profile = display_profiles()            
        if not show_profile:
            print("\n")
            cprint("THERE IS NO PROFILE SAVED IN YOUR ACCOUNT".center(terminal_width), "red")
            print("\n")
        else:
            cprint("Here's a list of all your profiles".center(terminal_width),"black")
            print("\n")
            print(("-*-"*25).center(terminal_width))

            for profile in display_profiles():
                print(f"PROFILE NAME:{profile.profile_name}".center(terminal_width))
                print(f"PROFILE USERNAME:{profile.profile_username}".center(terminal_width))
                print(f"PROFILE EMAIL:{profile.profile_email}".center(terminal_width))
                print(f"PROFILE PASSWORD:{profile.profile_password}".center(terminal_width))
                print(("-*-"*25).center(terminal_width))
                print("\n")

    elif short_code == "gp":
        print("Kindly enter the profile name you want to generate a password for")            
        profile_gen_passwrd = input()
        profile_to_change = search_profile(profile_gen_passwrd)
        if profile_to_change:
            print("Input the length of password you want:")
            passwrd_length = input()
            try:
                pw_length = int(passwrd_length)
                if passwrd_length.isdigit():
                    new_passwrd = generate_pass(pw_length)
                    profile_to_change.profile_password = new_passwrd
                    print("\n")
                    cprint("A New Password was Generated and has been Successfully Saved".center(terminal_width), "green")
                    print("\n")
                else:
                    cprint("\t Negative numbers are NOT allowed", "red")    
                    print("\n")
            except ValueError:
                cprint("\t You MUST input a number...example 7", "red")        
                print("\n")
        else:
            print("\n")        
            cprint("There is no Profile with That Name".center(terminal_width), "red")
            print("\n")

    elif short_code == "search":
        print("Kindly enter your search")
        search_string = input()
        if search_string:
            search_result = search_profile(search_string)
            if search_result:
                print("\n")
                cprint("SEARCH RESULTS".center(terminal_width),"green")
                print("\n")
                print(("-*-"*25).center(terminal_width))
                print(f"PROFILE NAME:{search_result.profile_name}".center(terminal_width))
                print(f"PROFILE USERNAME:{search_result.profile_username}".center(terminal_width))
                print(f"PROFILE EMAIL:{search_result.profile_email}".center(terminal_width))
                print(f"PROFILE PASSWORD:{search_result.profile_password}".center(terminal_width))
                print(("-*-"*25).center(terminal_width))
                print("\n")
            else:
                print("\n")
                cprint("No items were found using that criteria".center(terminal_width),"magenta")
                print("\n")
        else:
            cprint("You MUST input a search item","red")

    elif short_code == "copy":
        print("Kindly enter the profile you want to copy(password)")
        search_passwrd = input()
        found_copy_profile = search_profile(search_passwrd)
        if not search_passwrd:
            cprint("You MUST input the profile you want to copy password","red")
        else:
            if not found_copy_profile:
                cprint("\t Profile NOT found!","red",attrs=["bold"])
            else:
                found_copy_profile = copy_password(search_passwrd)
                paste_passwrd = pyperclip.paste()
                if paste_passwrd:
                    cprint("\t Copied!!","green")
                    print("\n")
                else:
                    cprint("\t NOT copied!!!","red")
                    print("\n")

    elif short_code == "del":
        cprint("PROCEED WITH CAUTION!".center(terminal_width),"red",attrs=["bold","blink"])
        print("Enter the name of the profile you want to delete:")
        del_profile = input()
        found_profile = search_profile(del_profile)
        if found_profile:
            cprint("DO YOU WANT TO CONTINUE TO DELETE? Y/N",attrs=["bold"])
            continue_prompt = input().upper()
            if continue_prompt == "Y":
                delete_profile(found_profile)
                print("\n")
                cprint("Profile DELETED!".center(terminal_width),"green")
                print("\n")
            elif continue_prompt == "N":
                return
            else:
                cprint("\t You input an unrecognised command","red")
        else:
            print("\n")
            cprint("The profile does NOT exist".center(terminal_width),"red")
            print("\n")

    elif short_code=="acp":
        cprint("WE NEED TO CONFIRM ITS YOU!".center(terminal_width),"red",attrs=['bold','blink'])
        print("Enter your username")
        passwrd_change_username = input()
        print("Enter your account password")
        passwrd_change_password = input()
        if not (passwrd_change_password or passwrd_change_username):
            cprint("You submitted empty field(s)")
            print("\n")
        else:
            data_match = login_user(passwrd_change_username, passwrd_change_password)
            if data_match:
                print("Enter your new password")
                new_entered_passwrd = input()
                print("Confirm password")
                confirm_entered_passwrd = input()
                if new_entered_passwrd == confirm_entered_passwrd:
                    user_change_password(passwrd_change_username, new_entered_passwrd)
                    print("\n")
                    cprint("Password changed","green")
                    print("\n")
                else:
                    print("\n")
                    cprint("Password confirmation does NOT match","red")
                    print("\n")
            else:
                print("\n")
                cprint("ERROR, please check your login details and try again","red")
                print("\n")

    elif short_code=="delete":
        cprint("WE NEED TO CONFIRM ITS YOU!".center(terminal_width),"red",attrs=["bold","blink"])
        print("Enter your username")
        passwrd_change_username = input()
        print("Enter your account password")
        passwrd_change_password = input()
        if not (passwrd_change_password or passwrd_change_username):
            cprint("You submitted empty field(s)")
            print("\n")
        else:
            data_match = login_user(passwrd_change_username, passwrd_change_password)
            user_acc = user_change_password(passwrd_change_username, passwrd_change_password)
            if data_match:
                delete_account(user_acc)
                print("\n")
                cprint("User DELETED","green")
                print("\n")
                return
            else:
                print("\n")
                cprint("ERROR, please check your Account Details and try again","red")
                print("\n")


    elif short_code=="logout":
        return

    elif short_code == "ex":
        cprint("\t BYE. . ...","cyan")
        sys.exit()
    else:
        print("\n")
        cprint("You input an unrecognised command".center(terminal_width),"red")
        print("\n")

def main():
    cprint(figlet_format('LOCKER', font='speed'),'green', attrs=['bold'])
    cprint("\033[1m" +  "Hello and Welcome to the Password Locker".center(terminal_width),"white", attrs=['bold','blink'])
    while True:
        print("Do you have an account? Y/N")
        account_prompt = input().upper().strip()
        if account_prompt == "Y":
            print("Enter your username:")
            existing_username = input()
            if not existing_username:
                cprint("You have not entered a username !","red")
                print("Enter your username:")
                existing_username = input()
            print("Enter your password:")
            existing_password = input()
            if not existing_password:
                cprint("You have not entered a password!","red")
                print("Enter your password:")
                existing_password = input()
            login_success = login_user(existing_username, existing_password)
            if not login_success:
                print("\n")
                cprint("Incorrect username / password combination","red")
                print("\n")
            else:
                while True:
                    print("\033[1m PROFILE CONTROLS:- "+'\033[0m'+"Use these short codes : np - Add a new profile, dp-Display all profiles, gp - generate new password for a profile, search - find a profile, copy - copy password to clipboard, del - delete a profile, logout- logout of session, ex - exit the application")
                    print("\033[1m ACCOUNT CONTROLS:- "+'\033[0m'+"Use these short codes : acp - Change your account password, delete - Delete your account")
                    short_code = input()
                    handle_short_codes(short_code)
                    if short_code=="logout" or short_code=="delete":
                        break

        elif account_prompt == "N":
            print("Enter your details to create a new account".center(terminal_width))
            print("Please enter your preffered username")
            new_user_username = input()
            if not new_user_username:
                cprint("You have not entered any username!","red")
                new_user_username = input()
            print("Please enter your password")
            new_user_password = input()
            if not new_user_password:
                cprint("You have not entered any password!","red")
                new_user_password = input()
            user_already_exist = check_user_exists(new_user_username)
            if not user_already_exist:
                user_new = User(new_user_username, new_user_password)
                if not save_account(user_new):
                    print("\n")
                    cprint("\033[1m Account created successfully \033[0m".center(terminal_width),"green")
                    print("\n")
                    while True:
                        print("\033[1m PROFILE CONTROLS:- "+'\033[0m'+"Use these short codes : np - Add a new profile, dp-Display all profiles, gp - generate new password for a profile, search - find a profile, copy - copy password to clipboard, del - delete a profile, logout- logout of session,  ex - exit the application")
                        print("\033[1m ACCOUNT CONTROLS:- "+'\033[0m'+"Use these short codes : acp - Change your account password, delete - Delete your account")
                        short_code = input()
                        handle_short_codes(short_code)
                        if short_code=="logout" or short_code=="delete":
                            break
            else:
                print("\n")
                cprint("The username is already in use","magenta")
                cprint("Please try another username","magenta")
                print("\n")

        else:
            print("\n")
            cprint("You Input an unrecognised command...Please enter Y/N!","red")
            print("\n")

        print("\n")
        cprint("An interrupt detected...Exiting..", "red", attrs=["bold"])
        sys.exit()        


if __name__ == "__main__":
    main()