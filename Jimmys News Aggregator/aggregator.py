#-----Statement of Authorship----------------------------------------#
#
#  This is an individual assessment item.  By submitting this
#  code I agree that it represents my own work.  I am aware of
#  the University rule that a student must not act in a manner
#  which constitutes academic dishonesty as stated and explained
#  in QUT's Manual of Policies and Procedures, Section C/5.3
#  "Academic Integrity" and Section E/2.1 "Student Code of Conduct".
#
#    Student no: n10260439
#    Student name: James Chapman
#
#  NB: Files submitted without a completed copy of this statement
#  will not be marked.  Submitted files will be subjected to
#  software plagiarism analysis using the MoSS system
#  (http://theory.stanford.edu/~aiken/moss/).
#
#--------------------------------------------------------------------#



#-----Assignment Description-----------------------------------------#
#
#  News Feed Aggregator
#
#  In this assignment you will combine your knowledge of HTMl/XML
#  mark-up languages with your skills in Python scripting, pattern
#  matching, and Graphical User Interface design to produce a useful
#  application that allows the user to aggregate RSS news feeds.
#  See the instruction sheet accompanying this file for full details.
#
#--------------------------------------------------------------------#



#-----Imported Functions---------------------------------------------#
#
# Below are various import statements for helpful functions.  You
# should be able to complete this assignment using these
# functions only.  Note that not all of these functions are
# needed to successfully complete this assignment.
#
# NB: You may NOT use any Python modules that need to be downloaded
# and installed separately, such as "Beautiful Soup" or "Pillow".
# Only modules that are part of a standard Python 3 installation may
# be used. 

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
from tkinter import messagebox
# Import a special Tkinter widget we used in our demo
# solution.  (You do NOT need to use this particular widget
# in your solution.  You may import other such widgets from the
# Tkinter module provided they are ones that come bundled
# with a standard Python 3 implementation and don't have to
# be downloaded and installed separately.)
from tkinter.scrolledtext import ScrolledText

# Functions for finding all occurrences of a pattern
# defined via a regular expression, as well as
# the "multiline" and "dotall" flags.  (You do NOT need to
# use these functions in your solution, because the problem
# can be solved with the string "find" function, but it will
# be difficult to produce a concise and robust solution
# without using regular expressions.)
from re import findall, finditer, MULTILINE, DOTALL, sub

# Import the standard SQLite functions (just in case they're
# needed one day).
from sqlite3 import *

import xml.etree.ElementTree as ET

#
#--------------------------------------------------------------------#



#-----------------------------------------------------------
#
# A function to download and save a web document. If the
# attempted download fails, an error message is written to
# the shell window and the special value None is returned.
#
# Parameters:
# * url - The address of the web page you want to download.
# * target_filename - Name of the file to be saved (if any).
# * filename_extension - Extension for the target file, usually
#      "html" for an HTML document or "xhtml" for an XML
#      document or RSS Feed.
# * save_file - A file is saved only if this is True. WARNING:
#      The function will silently overwrite the target file
#      if it already exists!
# * char_set - The character set used by the web page, which is
#      usually Unicode UTF-8, although some web pages use other
#      character sets.
# * lying - If True the Python function will hide its identity
#      from the web server. This can be used to prevent the
#      server from blocking access to Python programs. However
#      we do NOT encourage using this option as it is both
#      unreliable and unethical!
# * got_the_message - Set this to True once you've absorbed the
#      message about Internet ethics.

def download(url = 'http://www.wikipedia.org/',
             target_filename = 'download',
             filename_extension = 'xhtml',
             save_file = True,
             char_set = 'UTF-8',
             lying = False,
             got_the_message = False):

    # Import the function for opening online documents and
    # the class for creating requests
    from urllib.request import urlopen, Request

    # Import an exception raised when a web server denies access
    # to a document
    from urllib.error import HTTPError

    # Open the web document for reading
    try:
        if lying:
            # Pretend to be something other than a Python
            # script (NOT RECOMMENDED!)
            request = Request(url)
            request.add_header('User-Agent', 'Mozilla/5.0')
            if not got_the_message:
                print("Warning - Request does not reveal client's true identity.")
                print("          This is both unreliable and unethical!")
                print("          Proceed at your own risk!\n")
        else:
            # Behave ethically
            request = url
        web_page = urlopen(request)
    except ValueError:
        print("Download error - Cannot find document at URL '" + url + "'\n")
        return None
    except HTTPError:
        print("Download error - Access denied to document at URL '" + url + "'\n")
        return None
    except Exception as message:
        print("Download error - Something went wrong when trying to download " + \
              "the document at URL '" + url + "'")
        print("Error message was:", message, "\n")
        return None

    # Read the contents as a character string
    try:
        web_page_contents = web_page.read().decode(char_set)
    except UnicodeDecodeError:
        print("Download error - Unable to decode document from URL '" + \
              url + "' as '" + char_set + "' characters\n")
        return None
    except Exception as message:
        print("Download error - Something went wrong when trying to decode " + \
              "the document from URL '" + url + "'")
        print("Error message was:", message, "\n")
        return None

    # Optionally write the contents to a local text file
    # (overwriting the file if it already exists!)
    if save_file:
        try:
            text_file = open(target_filename + '.' + filename_extension,
                             'w', encoding = char_set)
            text_file.write(web_page_contents)
            text_file.close()
        except Exception as message:
            print("Download error - Unable to write to file '" + \
                  target_filename + "'")
            print("Error message was:", message, "\n")

    # Return the downloaded document to the caller
    return web_page_contents

#
#--------------------------------------------------------------------#



#-----Student's Solution---------------------------------------------#
#
# Put your solution at the end of this file.
#

# Name of the exported news file. To simplify marking, your program
# should produce its results using this file name.

# Downloading the url's.
download(url = 'https://www.sbs.com.au/news/feed',
         target_filename = 'sources/sbs',
         filename_extension = 'xml')

download(url = 'https://www.dailymail.co.uk/home/index.rss',
         target_filename = 'sources/dm',
         filename_extension = 'xml')

argsNum = 4
storiesNum = 10
sourcesNum = 4

stories = [[[0 for x in range(argsNum)] for y in range(storiesNum)] for z in range(sourcesNum)]
names = ['SBS', 'Daily Mail', 'Mirror', 'RT']
xml_filenames = ['sbs.xml', 'dm.xml', 'mirror.xml', 'rt.xml']

for sources in range(sourcesNum):
    # Open and clean XML files.
    with open('sources/' + xml_filenames[sources], 'r', encoding='utf8', errors='ignore') as file:
        raw = file.read()
        file.close()
    cleaned = sub(r'& ?(ld|rd)quo ?[;\]]', '\"', raw)
    cleaned = sub(r'& ?(ls|rs)quo ?;', '\'', cleaned)
    cleaned = sub(r'& ?ndash ?;', '-', cleaned)
    root = ET.fromstring(cleaned)
    counter = 0
    for channel in root:
        for item in channel.findall('item'):
            stories[sources][counter][0] = item.find('title').text
            rawDesc = item.find('description').text
            cleanDesc = sub(r'<.*?>', '', rawDesc)
            cleanDesc = sub(' Read Full Article at RT.com', '', cleanDesc)
            stories[sources][counter][1] = cleanDesc
            stories[sources][counter][2] = item.find('pubDate').text
            stories[sources][counter][3] = item.find('enclosure').attrib['url']
            counter += 1
            if counter == 10:
                break
 # Placing of all the Labels, Images and Spin-boxes.
root = Tk()
root.title('News Feed')
root.resizable(0, 0)
canvas = Frame(root, padx=10, pady=10, width=400, height=400)
canvas.grid(row=0)
fntTitle = ('Verdana', 20)
fntSub = ('Verdana', 16)
fntText = ('Verdana', 12)
fntTextB = ('Verdana', 12, 'bold')
fntSmall = ('Verdana', 10)

lblTitle = Label(canvas, text="Jimmy's News Mix", font=fntTitle, justify='center')
lblTitle.grid(row=1, column=0)

imgLogo = PhotoImage(file='logo/logo.png')
pbxLogo = Label(canvas, image=imgLogo).grid(row=0, column=0)

lblSpacer = Label(canvas)
lblSpacer.grid(row=2)

frmSelect = LabelFrame(canvas, text='News Feeds', font=fntSub, relief=SUNKEN, padx=5, pady=5)
frmSelect.grid(row=3, sticky=S+W+N+E)

imgSbs = PhotoImage(file='logo/sbs.png')
pbxSbs = Label(frmSelect, image=imgSbs)
pbxSbs.grid(row=0, column=0, sticky=E)
lblSbs = Label(frmSelect, text=names[0], font=fntTextB, anchor=W, justify=LEFT)
lblSbs.grid(row=0, column=1, sticky=W)
lblSbsDate = Label(frmSelect, text='Current', font=fntText, anchor=CENTER, justify=CENTER)
lblSbsDate.grid(row=0, column=2, sticky=W+E)
spnSbs = Spinbox(frmSelect, from_=0, to = 10, width=5, font=fntText, state='readonly', justify=CENTER)
spnSbs.grid(row=0, column=3, stick=E)

imgDm = PhotoImage(file='logo/dm.png')
pbxDm = Label(frmSelect, image=imgDm)
pbxDm.grid(row=1, column=0, sticky=E)
lblDm = Label(frmSelect, text=names[1], font=fntTextB, anchor=W, justify=LEFT)
lblDm.grid(row=1, column= 1, sticky=W)
lblDmDate = Label(frmSelect, text='Current', font=fntText, anchor=CENTER, justify=CENTER)
lblDmDate.grid(row=1, column=2, sticky=W+E)
spnDm = Spinbox(frmSelect, from_=0, to = 10, width=5, font=fntText, state='readonly', justify=CENTER)
spnDm.grid(row=1, column=3, stick=E)

imgMirror = PhotoImage(file='logo/mirror.png')
pbxMirror = Label(frmSelect, image=imgMirror)
pbxMirror.grid(row=2, column=0, sticky=E)
lblMirror = Label(frmSelect, text=names[2], font=fntTextB, anchor=W, justify=LEFT)
lblMirror.grid(row=2, column=1, sticky=W)
lblMirrorDate = Label(frmSelect, text='16/10/19', font=fntText, anchor=CENTER, justify=CENTER)
lblMirrorDate.grid(row=2, column=2, sticky=W+E)
spnMirror = Spinbox(frmSelect, from_=0, to = 10, width=5, font=fntText, state='readonly', justify=CENTER)
spnMirror.grid(row=2, column=3, stick=E)

imgRt = PhotoImage(file='logo/rt.png')
pbxRt = Label(frmSelect, image=imgRt)
pbxRt.grid(row=3, column=0, sticky=E)
lblRt = Label(frmSelect, text=names[3], font=fntTextB, anchor=W, justify=LEFT)
lblRt.grid(row=3, column=1, sticky=W)
lblRtDate = Label(frmSelect, text='16/10/19', font=fntText, anchor=CENTER, justify=CENTER)
lblRtDate.grid(row=3, column=2, sticky=W+E)
spnRt = Spinbox(frmSelect, from_=0, to = 10, width=5, font=fntText, state='readonly', justify=CENTER)
spnRt.grid(row=3, column=3, stick=E)

lblSpacer = Label(frmSelect)
lblSpacer.grid(row=4)

lblOutput = Text(frmSelect, font=fntSmall, wrap=NONE, height=10, width=50, relief=SUNKEN, state=DISABLED)
lblOutput.grid(row=5, columnspan=4)
scrX = Scrollbar(frmSelect, command=lblOutput.xview, orient=HORIZONTAL)
scrX.grid(row=6, columnspan=4, sticky='nsew')
lblOutput['xscrollcommand'] = scrX.set
scrY = Scrollbar(frmSelect, command=lblOutput.yview, orient=VERTICAL)
scrY.grid(row=5, column=4, sticky='nsew')
lblOutput['yscrollcommand'] = scrY.set

# Exporting the html function
def export_html(a, b, c, d):
    count = [int(a), int(b), int(c), int(d)]
    news_file_name = 'news.html'
    if sum(count) > 0:
        # Layout of the HTML for the title.
        if sum(count) < 11:
            html_title = '<!DOCTYPE html>'\
                          '<html>'\
                          '<head>'\
                          "<title>Jimmy's News Mix</title>"\
                          '<style>'\
                          'body {background-color: #EDF0F5}'\
                          'div {'\
                          'border: 1px solid black;'\
                          'background-color: #FFFFFF;'\
                          'width: 530px;'\
                          'margin: 0 auto;'\
                          'padding-right: 15px;'\
                          'padding-left: 15px;'\
                          '}'\
                          '</style>'\
                          '</head>'\
                          '<body>'\
                          '<div><center>'\
                          "<h1>Jimmy's News Mix</h1>"\
                          '<img src="https://www.stickpng.com/assets/images/5a0acb755a997e1c2cea10be.png" width="500">'\
                          '<hr>'
            html_stories = ''
            for sources in range(sourcesNum):
                # Layout of the HTML converting from XML to HTML so that all stories look the same.
                for item in range(count[sources]):
                    html_stories = html_stories + '<h1>' + stories[sources][item][0] + '</h1>'\
                                   '<br>'\
                                   '<img src="' + stories[sources][item][3] + '" width="500" border="1px solid black"></center>'\
                                   '<br>'\
                                   '<p>' + stories[sources][item][1] + '</p>'\
                                   '<br>'\
                                   '<p>' + names[sources] + ' - ' + stories[sources][item][2] + '</p>'\
                                   '<hr>'
            html_concat = html_title + html_stories + \
                          '<h1>Sources:</h1><p>'\
                          '<ul><li>SBS: https://www.sbs.com.au/news/feed</li>'\
                          '<li>Daily Mail: https://www.dailymail.co.uk/home/index.rss</li>'\
                          '<li>Mirror: https://www.mirror.co.uk/news/?service=rss</li>'\
                          '<li>RT: https://www.rt.com/rss/</li></ul></p></div></body></html>'
            Html_file= open(news_file_name, 'w')
            Html_file.write(html_concat)
            Html_file.close()
            # Message boxes to show any errors and when it has run succesfully. 
            messagebox.showinfo('Export', str(sum(count)) + ' stories successfully exported to ' + news_file_name)
        else:
            messagebox.showerror('Error', (str(sum(count)) + ' stories selected. Must be equal to or less than 10.'))
    else:
        messagebox.showerror('Error', 'No Stories Selected.')

def update_stories(a, b, c, d):
    lblOutput['state'] = NORMAL
    lblOutput.delete(1.0, END)
    count = [int(a), int(b), int(c), int(d)]
    for sources in range(sourcesNum):
        for story in range(count[sources]):
            lblOutput.insert(END, str(stories[sources][story][0]) + '\n[' + names[sources] + ' - ' + stories[sources][story][2] + ']\n\n')
    lblOutput['state'] = DISABLED

btnExport = Button(frmSelect, text='Export to HTML', font=fntText, height=1, command = lambda : export_html(spnSbs.get(), spnDm.get(), spnMirror.get(), spnRt.get()))
btnExport.grid(row=7, sticky='WE', columnspan=5)
    
spnSbs['command'] = lambda : update_stories(spnSbs.get(), spnDm.get(), spnMirror.get(), spnRt.get())
spnDm['command'] = lambda : update_stories(spnSbs.get(), spnDm.get(), spnMirror.get(), spnRt.get())
spnMirror['command'] = lambda : update_stories(spnSbs.get(), spnDm.get(), spnMirror.get(), spnRt.get())
spnRt['command'] = lambda : update_stories(spnSbs.get(), spnDm.get(), spnMirror.get(), spnRt.get())

root.mainloop()
