
#-----Statement of Authorship----------------------------------------#
#
#  This is an individual assessment item.  By submitting this
#  code I agree that it represents my own work.  I am aware of
#  the University rule that a student must not act in a manner
#  which constitutes academic dishonesty as stated and explained
#  in QUT's Manual of Policies and Procedures, Section C/5.3
#  "Academic Integrity" and Section E/2.1 "Student Code of Conduct".
#
#    Student no: *****n10505024*****
#    Student name: *****Shu Du*****
#
#  NB: Files submitted without a completed copy of this statement
#  will not be marked.  Submitted files will be subjected to
#  software plagiarism analysis using the MoSS system
#  (http://theory.stanford.edu/~aiken/moss/).
#
#--------------------------------------------------------------------#



#-----Assignment Description-----------------------------------------#
#
#  What's On?: Online Entertainment Planning Application
#
#  In this assignment you will combine your knowledge of HTMl/XML
#  mark-up languages with your skills in Python scripting, pattern
#  matching, and Graphical User Interface design to produce a useful
#  application for planning an entertainment schedule.  See
#  the instruction sheet accompanying this file for full details.
#
#--------------------------------------------------------------------#



#-----Imported Functions---------------------------------------------#
#
# Below are various import statements for helpful functions.  You
# should be able to complete this assignment using these
# functions only.  Note that not all of these functions are
# needed to successfully complete this assignment.

# The function for opening a web document given its URL.
# (You WILL need to use this function in your solution,
# either directly or via our "download" function.)
from urllib.request import urlopen

# Import the standard Tkinter functions. (You WILL need to use
# these functions in your solution.  You may import other widgets
# from the Tkinter module provided they are ones that come bundled
# with a standard Python 3 implementation and don't have to
# be downloaded and installed separately.)
from tkinter import *

# Functions for finding all occurrences of a pattern
# defined via a regular expression, as well as
# the "multiline" and "dotall" flags.  (You do NOT need to
# use these functions in your solution, because the problem
# can be solved with the string "find" function, but it will
# be difficult to produce a concise and robust solution
# without using regular expressions.)
from re import findall, finditer, MULTILINE, DOTALL

# Import the standard SQLite functions (just in case they're
# needed one day).
from sqlite3 import *

#
#--------------------------------------------------------------------#



#-----Downloader Function--------------------------------------------#
#
# This is our function for downloading a web page's content and both
# saving it as a local file and returning its source code
# as a Unicode string. The function tries to produce
# a meaningful error message if the attempt fails.  WARNING: This
# function will silently overwrite the target file if it
# already exists!  NB: You should change the filename extension to
# "xhtml" when downloading an XML document.  (You do NOT need to use
# this function in your solution if you choose to call "urlopen"
# directly, but it is provided for your convenience.)
#
def download(url = 'https://www.rottentomatoes.com/browse/upcoming/',
             target_filename = 'download',
             filename_extension = 'html'):

    # Import an exception raised when a web server denies access
    # to a document
    from urllib.error import HTTPError

    # Open the web document for reading
    try:
        web_page = urlopen(url)
    except ValueError:
        raise Exception("Download error - Cannot find document at URL '" + url + "'")
    except HTTPError:
        raise Exception("Download error - Access denied to document at URL '" + url + "'")
    except:
        raise Exception("Download error - Something went wrong when trying to download " + \
                        "the document at URL '" + url + "'")

    # Read its contents as a Unicode string
    try:
        web_page_contents = web_page.read().decode('UTF-8')
    except UnicodeDecodeError:
        raise Exception("Download error - Unable to decode document at URL '" + \
                        url + "' as Unicode text")

    # Write the contents to a local text file as Unicode
    # characters (overwriting the file if it
    # already exists!)
    try:
        text_file = open(target_filename + '.' + filename_extension,
                         'w', encoding = 'UTF-8')
        text_file.write(web_page_contents)
        text_file.close()
    except:
        raise Exception("Download error - Unable to write to file '" + \
                        target_file + "'")

    # Return the downloaded document to the caller
    return web_page_contents


#
#--------------------------------------------------------------------#



#-----Student's Solution---------------------------------------------#
#
# Put your solution at the end of this file.
#

# Name of the planner file. To simplify marking, your program should
# generate its entertainment planner using this file name.
planner_file = 'planner.html'

import webbrowser
from time import asctime

url1='https://www.rottentomatoes.com/browse/upcoming/'
url2='https://www.giantbomb.com/new-games/'
url3='https://www.brisent.com.au/Event-Calendar'

#Create lists containing different variable names for the first window.
variable_list=['vone','vtwo','vthree','vfour','vfive','vsix','vseven','veight','vnine','vten']
#Create another lists to give variables to the second window.
y=0
variable_list1=[]
for a in range(10):
    variable_list1.append(variable_list[y]+'x')
    y=y+1
#Create another lists to give variables to the third window.
y=0
variable_list2=[]
for b in range(10):
    variable_list2.append(variable_list[y]+'z')
    y=y+1

M_list=[]#The main list to save tiles, dates, images.
Sql_list=[]#The list to save titles and dates that will be saved to DB.
selected=0#To record how many boxes selected.

def find_titles(url,beginning,endding):#Fuction to find things from web.
    page=urlopen(url)
    html_code=page.read().decode('UTF-8')
    page.close()
    start_marker =beginning
    end_marker=endding
    end_position = 0
    starting_position = html_code.find(start_marker,end_position)
    end_position=html_code.find(end_marker,starting_position)
    titlelist=[]
    for ten in range(15):
        if starting_position != -1 and end_position != -1:
            titlelist.append( html_code[starting_position + len(start_marker) : end_position])
            starting_position = html_code.find(start_marker, end_position)
            end_position = html_code.find(end_marker, starting_position)
    return titlelist

def find_titles_off_line(html_file,beginning,endding):#Fuction to find things from html doc.
    html_code = open(html_file).read()
    start_marker =beginning
    end_marker=endding
    end_position = 0
    starting_position = html_code.find(start_marker,end_position)
    end_position=html_code.find(end_marker,starting_position)
    titlelist=[]
    for ten in range(15):
        if starting_position != -1 and end_position != -1:
            titlelist.append( html_code[starting_position + len(start_marker) : end_position])
            starting_position = html_code.find(start_marker, end_position)
            end_position = html_code.find(end_marker, starting_position)
    return titlelist

#Find all tiltes, dates and images from websites.
movies=find_titles(url1,'"title":"','","url":')
mdates=find_titles(url1,
                  '"theaterReleaseDate":"',
                  '","mpaaRating":')
mimages=find_titles(url1,'"primary":"','},"actors"')

games=find_titles(url2,'<h3 class="title">','</h3>')
gdates=find_titles(url2,
                  '<time class="date">',
                  '</time>')
gimages=find_titles(url2,'<div class="img imgboxart"><img src="','alt="')

events=find_titles(url3,'<h1 class="event-title">','</h1>')
edates=find_titles(url3,
                  '<h2 class="Event-Date">',
                  '</h2>')
eimages=find_titles(url3,'<img src="','" width="270" />')


html_template = """<!DOCTYPE html>
<html>

<head>
<meta charset = 'UTF-8'>
<style>
  .bordered {
    width: 500px;
    height: 530px;
    padding: 10px;
    border: 5px outset yellowgreen;
    margin:20px auto; 
  }
</style>

</head>

<body>

<h1 style="color:red;font-size:40px;"><center>The Entertainment Guide<center></h1>
<p align="center"><img src="tk.gif" border="3"></p>
<p >***TEXT***</p>

<p>This document is generated on ***TIME***</p>

<h2>References</h2>

    <big>
    <ul>
      <li><a href="https://www.rottentomatoes.com">Movies</a></li>
      <li><a href="https://www.giantbomb.com">Games</a></li>   
      <li><a href="https://www.brisent.com.au">Events</a></li>
    </ul>
    </big>
 

</body>

 </html>
"""
#Function to convert list into strings.
def convert(mylist): 
    aa = [str(i) for i in mylist]  
    bb = ("".join(aa))  
    return(bb) 
#Command to print html doc.  
def generate_html():
    title="planner"
    time = asctime()
    content=convert(M_list)#Convert the main list.
    html_code= html_template.replace('***TEXT***', content)
    
    html_code = html_code.replace('***TIME***', time)
    
    html_file = open(title + '.html', 'w', encoding = 'UTF-8')
    html_file.write(html_code)
    html_file.close()
    webbrowser.open_new_tab('planner.html')

#The window for movies coming.
def Movies_window():
    Movies_window=Toplevel()
    Movies_window.title('Movies Coming Soon')
    Movies_window['bg']='light green'
    Title_label=Label(Movies_window, text='Movies Comming Soon',
                font=('Arial',30),fg='white',bg='light green')
    Title_label.pack(padx = 5, pady = 5)

#Command to save selected stuff in movies window.       
    def I_like(n):
        global selected
        if  variable_list[n].get()==1:
            Sql_list.append(str(movies[n]))
            Sql_list.append(str(mdates[n]))
            M_list.append('<div class="bordered"><p align= "center">'+str(movies[n])+'</p>'+
               '<p align= "center"><img src="'+str(mimages[n])+
                        'width=275&height= 125/>'+'<p align= "center">'+str(mdates[n])+'</p></div>')
            selected=selected+1
            Button(Entertainment_guide, text = ' Print planner'+'('+str(selected)+'/30 selected)',
                   font = ('Arial', 11),fg='purple',bg='light green',command=generate_html).\
                      grid(row = 8, column = 3, sticky = W, pady = 10)
            
        elif  variable_list[n].get()==0:
            Sql_list.remove(str(movies[n]))
            Sql_list.remove(str(mdates[n]))
            M_list.remove('<div class="bordered"><p align= "center">'+str(movies[n])+'</p>'+
               '<p align= "center"><img src="'+str(mimages[n])+
                        'width=275&height= 125/>'+'<p align= "center">'+str(mdates[n])+'</p></div>')
            selected=selected-1
            Button(Entertainment_guide, text = ' Print planner'+'('+str(selected)+'/30 selected)',
                   font = ('Arial', 11),fg='purple',bg='light green',command=generate_html).\
                      grid(row = 8, column = 3, sticky = W, pady = 10)
            
#Create 10 checkbuttons.          
    n=0
    for i in range(10):
        Checkbutton(Movies_window, text=movies[n]+'('+mdates[n]+')',bg='light green',
                           font =('Arial', 18),variable=variable_list[n],onvalue = 1,
                    offvalue = 0,command=lambda n=n:I_like(n)).pack(padx = 5, pady = 5,side=TOP)
        n=n+1
        


    url_label=Label(Movies_window,text=url1,font=('Arial',11),fg='white',bg='light green')
    url_label.pack(padx =5, pady = 5,side=BOTTOM)
    Movies_window.mainloop()
    
    
#The window for games coming.    
def Games_window():
    Games_window=Toplevel()
    Games_window.title('Games Coming Soon')
    Games_window['bg']='light blue'
    Title_label=Label(Games_window, text='Games Comming Soon',
                font=('Arial',30),fg='white',bg='light blue')
    Title_label.pack(padx = 5, pady = 5)
    
#Command to save selected stuff in movies window. 
    def I_like1(n):
        global selected
        if  variable_list1[n].get()==1:
            Sql_list.append(str(games[n]))
            Sql_list.append(str(gdates[n]))
            selected=selected+1
            M_list.append('<div class="bordered"><p align= "center">'+str(games[n])+'</p>'+
               '<p align= "center"><img src="'+str(gimages[n])+
                        ' width=400&height= 200/>'+'<p align= "center">'+str(gdates[n])+'</p></div>')
            Button(Entertainment_guide, text = ' Print planner'+'('+str(selected)+'/30 selected)',
                   font = ('Arial', 11),fg='purple',bg='light green',command=generate_html).\
                      grid(row = 8, column = 3, sticky = W, pady = 10)
           
        elif  variable_list1[n].get()==0:
            Sql_list.remove(str(games[n]))
            Sql_list.remove(str(gdates[n]))
            selected=selected-1
            M_list.remove('<div class="bordered"><p align= "center">'+str(games[n])+'</p>'+
               '<p align= "center"><img src="'+str(gimages[n])+
                        ' width=400&height= 200/>'+'<p align= "center">'+str(gdates[n])+'</p></div>')
            Button(Entertainment_guide, text = ' Print planner'+'('+str(selected)+'/30 selected)',
                   font = ('Arial', 11),fg='purple',bg='light green',command=generate_html).\
                      grid(row = 8, column = 3, sticky = W, pady = 10)
           
            
 #Create 10 checkbuttons.           
    n=0
    for ii in range(10):
        Checkbutton(Games_window, text=games[n]+'('+gdates[n]+')',bg='light blue',
                           font =('Arial', 18),variable=variable_list1[n],onvalue = 1,
                    offvalue = 0,command=lambda n=n:I_like1(n)).pack(padx = 5, pady = 5,side=TOP)
        n=n+1
        
    url_label=Label(Games_window,text=url2,font=('Arial',11),fg='white',bg='light blue')
    url_label.pack(padx =5, pady = 5,side=BOTTOM)
    Games_window.mainloop()
    
 #The window for events coming.       
def Events_window():
    Events_window=Toplevel()
    Events_window.title('Events coming soon')
    Events_window['bg']='light pink'
    Title_label=Label(Events_window, text='Entertainment Events Deals',
                font=('Arial',30),fg='white',bg='light pink')
    Title_label.pack(padx = 5, pady = 5)
    

        
 #Command to save selected stuff in movies window. 
    def I_like2(n):
        global selected
        if  variable_list2[n].get()==1:
            Sql_list.append(str(events[n]))
            Sql_list.append(str(edates[n]))
            selected=selected+1
            M_list.append('<div class="bordered"><p align= "center">'+str(events[n])+'</p>'+
               '<p align= "center"><img src="https://www.brisent.com.au'+str(eimages[n])+
                        '" />'+' <p align= "center">'+str(edates[n])+'</p></div>')
            Button(Entertainment_guide, text = ' Print planner'+'('+str(selected)+'/30 selected)',
                   font = ('Arial', 11),fg='purple',bg='light green',command=generate_html).\
                      grid(row = 8, column = 3, sticky = W, pady = 10)
            
        elif  variable_list2[n].get()==0:
            Sql_list.remove(str(events[n]))
            Sql_list.remove(str(edates[n]))
            selected=selected-1
            M_list.remove('<div class="bordered"><p align= "center">'+str(events[n])+'</p>'+
               '<p align= "center"><img src="https://www.brisent.com.au'+str(eimages[n])+
                        '" />'+' <p align= "center">'+str(edates[n])+'</p></div>')
            Button(Entertainment_guide, text = ' Print planner'+'('+str(selected)+'/30 selected)',
                   font = ('Arial', 11),fg='purple',bg='light green',command=generate_html).\
                      grid(row = 8, column = 3, sticky = W, pady = 10)
#Created 10 checkbuttons.           
    n=0
    for i in range(10):
       
        Checkbutton(Events_window, text=events[n]+'('+edates[n]+')',bg='light pink',
                           font =('Arial', 18),variable=variable_list2[n],onvalue = 1,
                    offvalue = 0,command=lambda n=n:I_like2(n)).pack(padx = 5, pady = 5,side=TOP)
        n=n+1
        


    url_label=Label(Events_window,text=url3,font=('Arial',11),fg='white',bg='light pink')
    url_label.pack(padx =5, pady = 5,side=BOTTOM)
    Events_window.mainloop()
#Command to search from pre-downloaded html files for off-line mode.
def off_line():
    global movies
    global mdates
    global mimages
    global games
    global gdates
    global gimages
    global events
    global edates
    global eimages
    if v.get()==1:#Find them from html files.
        movies=find_titles_off_line('Movies.html','"title":"','","url":')
        mdates=find_titles_off_line('Movies.html',
              '"theaterReleaseDate":"',
              '","mpaaRating":')
        mimages=find_titles_off_line('Movies.html','"primary":"','},"actors"')

        games=find_titles_off_line('Games.html','<h3 class="title">','</h3>')
        gdates=find_titles_off_line('Games.html',
              '<time class="date">',
              '</time>')
        gimages=find_titles_off_line('Games.html','<div class="img imgboxart"><img src="','alt="')

        events=find_titles_off_line('Events.html','<h1 class="event-title">','</h1>')
        edates=find_titles_off_line('Events.html',
              '<h2 class="Event-Date">',
              '</h2>')
        eimages=find_titles_off_line('Events.html','<img src="','" width="270" />')
    if v.get()==0:#Find from the websites.
        movies=find_titles(url1,'"title":"','","url":')
        mdates=find_titles(url1,
                  '"theaterReleaseDate":"',
                  '","mpaaRating":')
        mimages=find_titles(url1,'"primary":"','},"actors"')

        games=find_titles(url2,'<h3 class="title">','</h3>')
        gdates=find_titles(url2,
                  '<time class="date">',
                  '</time>')
        gimages=find_titles(url2,'<div class="img imgboxart"><img src="','alt="')

        events=find_titles(url3,'<h1 class="event-title">','</h1>')
        edates=find_titles(url3,
                  '<h2 class="Event-Date">',
                  '</h2>')
        eimages=find_titles(url3,'<img src="','" width="270" />')

#Command to save selected items to DB.
def save_to_sql():
        connection= connect(database = "entertainment_planner.db")
        elements = connection.cursor()
        elements.execute("DELETE  FROM events")
        n=0
        for sql in range(len(Sql_list)//2):
            elements.execute("INSERT INTO events VALUES (?,?)",
                             (str(Sql_list[n]),str(Sql_list[n+1])))
            n=n+2
        connection.commit()
    
#The main window.  
Entertainment_guide=Tk()
Entertainment_guide.title('Entertainment Guide')
Entertainment_guide['bg'] = 'yellow'
suface_image = PhotoImage(file = 'timg.gif')
Label(Entertainment_guide, image = suface_image).\
                 grid(row = 0, column = 2, rowspan = 9, columnspan=9)

Entertainment_guide.resizable(0, 0)
#Set different variables to IntVar.
m=0
for ii in range(10):
    variable_list[m]=IntVar()#Variables for the first window's checkbuttons.
    variable_list1[m]=IntVar()#For the second window.
    variable_list2[m]=IntVar()#For the third window.
    m=m+1


v=IntVar()#Variable for off-line checkbutton
#Off-line checkbutton.
Checkbutton(Entertainment_guide, text="Off line mode",
            variable=v, onvalue=1, offvalue=0,bg='light green',
            command=off_line).grid(row=2,column=8)
#Movies window button.
Button(Entertainment_guide, text='Movies Coming',
       font =('Arial', 11),fg='purple',bg='light green',
       command=Movies_window).\
                            grid(row=4,column=2)
#Games window button.
Button(Entertainment_guide, text='Games Coming',
       font =('Arial', 11),fg='purple',bg='light green',
       command=Games_window).\
                            grid(row=4,column=3)
#Events windwo button.
Button(Entertainment_guide, text='Events Coming',
       font =('Arial', 11),fg='purple',bg='light green',
       command=Events_window).\
                            grid(row=4,column=4)
#Print planner button.
Button(Entertainment_guide, text = ' Print planner'+'('+str(selected)+'/30 selected)',
       font = ('Arial', 11),fg='purple',bg='light green',command=generate_html
       ).\
                      grid(row = 8, column = 3, sticky = W, pady = 10)
#Save to Sql DB button.
Button(Entertainment_guide, text='Save planner',
       font =('Arial', 11),fg='purple',bg='light green',
       command=save_to_sql).\
                            grid(row=8,column=4)

Entertainment_guide.mainloop()
