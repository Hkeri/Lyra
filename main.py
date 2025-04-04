'''
The Objective of this project is to assist users with a key feature

Idea:
      To assist users with constant feedback about them in a friendly way through their inputs

Name:
      Lyra {AI Name: Groq}
'''

#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
from groq import Groq
from task_automation import *
import re
import time
import os
import platform
import pyautogui

def groq(instrucations, query):
      api_key = "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"
      client = Groq(api_key=api_key)
      chat_completion = client.chat.completions.create(
      messages=[
            {
                  "role": "user",
                  "content": f"{instrucations}, {query}",
            }
      ],
      model="llama-3.3-70b-versatile",
      stream=False,
      )
      ra = (chat_completion.choices[0].message.content).replace("**", "")
      return (ra)

def append_to_file(text):
  filename = "data.txt"
  try:
    with open(filename, "a+") as file:
      if file.tell() > 0:
        file.write("\n")
      file.write(text)
      lines = file.readlines()
      if len(lines) >= 10:
        txt = file.read() 
        rtxt = txt.replace("\n", ",")
        print(groq(f'''Make a 30 words smart feedback to the user on how she can continue her objective within the inputs
                like if she is asking any study questions or inputs relate to study, then you must give a feedback on 
                how she should take a break or interest her about some games or movies that can cheer her up but encourage
                to study aswell but this is an example so if the user is doing anything else then you must give the
                feedback that can cheer them and encourage them. Here is the inputs''', {rtxt}))
        file.seek(0)
        file.truncate(0)
      else:
        return ""
  
  except FileNotFoundError:
        print(f"The file '{filename}' was not found.")
  except Exception as e:
      print(f"An error occurred: {e}")
      

if __name__ == "__main__":
    while True:
      question = input("Enter Your Question: ")
      cmd = groq('''if the query is asking about closing an application or website, respond "?!close (the application or website and make sure the website is in www and the .com also the application must be in its short form to run it in the Run Window like if the query is saying to close word, you must respond 'close winword'").
                    if the query is asking about opening an application or website, respond "?!open (the application or website and make sure the website is in www and the .com also the application must be in its short form to run it in the Run Window like if the query is saying to open word, you must respond 'open winword'")
                    if the query is asking about searching in youtube, then you must respond "?!youtube search (the youtube search)"
                    if the query is asking about the battery, respond "?!battery"
                    if the user is asking the internet speed, respond "?!internet speed"
                    if the user is asking to lower their brightness of the screen, respond "?!dim light"
                    if the user is asking to send in an email, respond "?!send email"
                    if the user is asking to change the wallpaper, respond "?!change wallpaper"
                    if the user is asking to display the top cpu and memory usage processes, respond "?!top processes"
                    if the user is asking to create a file, respond "?!create file"
                    if the user is asking to clean temporary files, respond "?!clean temporary files"
                    if the user is asking to download images from the internet, respond "?!download image"
                    if the user is asking to transcribe the audio, respond "?!transcribe audio"
                    if the user is asking to organize files, respond "?!organize files"
                    if the user is asking to read a pdf, respond "?!read pdf"
                    if the user is asking to play music, respond "?!play music"
                    if the user is asking to do an ocr, respond "?!ocr"
                    if the user is not asking for anything in this list then respond "!none"
                    if the user is asking for a whatsapp message, respond "?!whatsapp"
                    if the user is asking for downloading a youtube video, respond "?!youtube download"
                    if the user is asking to make a qrcode, respond "?!qrcode"
                    if the user is asking to shutdown the computer, respond "?!shutdown"
                    if the user is asking to restart the computer, respond "?!restart"
                    if the user is asking to take a screenshot, respond "?!screenshot"
                    if the user is asking to start a google meet, respond "?!google meeting"''', question)
      append_to_file(question)

      if re.search("?!close", cmd):
        cmd = cmd.replace("?!close", "")
        closeappweb(cmd)
      
      if re.search("?!open", cmd):
        cmd = cmd.replace("?!open", "")
        openappweb(cmd)
      
      if re.search("?!youtube search", cmd):
        cmd = cmd.replace("?!youtube search", "")
        yt_search(cmd)
    
      if re.search("?!battery", cmd):
       smart_battery()
    
      if re.search("?!internet speed", cmd):
        internet_speed()
    
      if re.search("?!dim light", cmd):
        dim_light()
        
      if re.search("?!send email", cmd):
        email = input("Please type in the sender's email: ")
        msg = input("Please type in the message: ")
        send_email(msg, email)
    
      if re.search("?!change wallpaper", cmd):
        image_path = input("Please type in the full Image Path: ")
        change_wallpaper(image_path)
    
      if re.search("?!top processes", cmd):
        display_top_processes()
    
      if re.search("?!create file", cmd):
        extension = input("Please type in the file extension: ")
        create_file(extension)
    
      if re.search("?!clean temporary files", cmd):
        clean_temp()
    
      if re.search("?!download image", cmd):
        image_url = input("Please type in the image url: ")
        download_images(image_url)

      if re.search("?!transcribe audio", cmd):
        audio_path = input("Please type in the Audio File Path: ")
        transcribe_audio(audio_path)

      if re.search("?!organize files", cmd):
        dir_ = input("Please type in the full form of the Directory Path: ")
        file_organizer(dir_)
    
      if re.search("?!read pdf", cmd):
        pdf = input("Please type in the PDF Path: ")
        read_pdf(pdf)
    
      if re.search("?!play music", cmd):
        song = input("Please type in the song name: ")
        playMusic(song)
    
      if re.search("?!ocr", cmd):
        image_ = input("Please type in the image path: ")
        ocr(image_)
    
      if re.search("?!whatsapp", cmd):
        whatsapp_send()
    
      if re.search("?!youtube download", cmd):
        url = input("Please type in the youtube url: ")
        ytDownloader(url)
        
      if re.search("?!qrcode", cmd):
        qr_url = input("Please type in the url: ")
        qrCodeGenerator(qr_url)

      if re.search("?!screenshot", cmd):
        number = 0
        print("Sure Sir, I will give you 5 seconds to show you want to Screenshot")
        time.sleep(5)
        ss = pyautogui.screenshot()
        number += 1
        ss.save(f"screenshot_{number}.png")
        print("I Have made A screenshot sir")

      if re.search("?!shutdown", cmd):
        if platform.system() == "Windows":
            os.system("shutdown /s /t 0")
        if platform.system() == "Linux":
            os.system("shutdown now")
        if platform.system() == "Darwin":  # macOS
            os.system("sudo shutdown -h now")
        else:
            print("Unsupported OS")

      if re.search("?!restart", cmd):
        if platform.system() == "Windows":
            os.system("shutdown /r /t 0")
        if platform.system() == "Linux":
            os.system("reboot")
        if platform.system() == "Darwin":  # macOS
            os.system("sudo shutdown -r now")
        else:
            print("Unsupported OS")
    
      if re.search("?!google meeting", cmd):
        os.system("start chrome https://meet.new")
    
      if re.search("!none", cmd):
        print(groq(question))

      if re.search("exit", cmd):
        print("Exiting...")
        exit(0)          
