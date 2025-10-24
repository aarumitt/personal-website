# A. Import the sqlite library
import sqlite3

#######################################################
# 1. ADD PROJECT TO DB
#######################################################
def saveProjectDB(Title, Description, ImageFileName):
    #A. Make a connection to the database
    conn = None
    conn = sqlite3.connect("projects.db")

    #B. Write a SQL statement to insert a specific row (based on Title name)
    sql='INSERT INTO projects (Title, Description, ImageFileName) values (?,?,?)'

    # B. Create a workspace (aka Cursor)
    cur = conn.cursor()

    # C. Run the SQL statement from above and pass it 1 parameter for each ?
    cur.execute(sql, (Title, Description, ImageFileName, ))

    # D. Save the changes
    conn.commit()
    if conn:
        conn.close()

#######################################################
# 2.  SHOW PROJECTS IN A TABLE
#######################################################
#   THIS RETURNS AS LIST OF DICTIONARIES
def getAllProjects():
    # A. Connection to the database
    conn = sqlite3.connect('projects.db')

    # B. Create a workspace (aka Cursor)
    cursorObj = conn.cursor()

    # D. Run the SQL Select statement to retrieve the data
    cursorObj.execute('SELECT Title, Description, ImageFileName FROM projects;')

    # E. Tell Python to 'fetch' all of the records and put them in
    #     a list called allRows
    allRows = cursorObj.fetchall()

    projectListOfDictionaries = []

    for individualRow in allRows:
        # Make sure we have an image name
        if individualRow[2] is not None and individualRow[2] != "":
            Image = individualRow[2]
        else:
            Image = "placeholder.png"
        # Create a dictionary for each row
        p = {"Title" : individualRow[0], "Description": individualRow[1], "Image": Image}
        projectListOfDictionaries.append(p)

    if conn:
        conn.close()

    return projectListOfDictionaries

def deleteProjectDB(Title):
    #A. Make a connection to the database
    conn = None
    conn = sqlite3.connect("projects.db")

    #B. Write a SQL statement to delete a specific row (based on Title name)
    sql='DELETE FROM projects WHERE Title = ?'

    # B. Create a workspace (aka Cursor)
    cur = conn.cursor()

    # C. Run the SQL statement from above and pass it 1 parameter for each ?
    cur.execute(sql, (Title, ))

    # D. Save the changes
    conn.commit()
    if conn:
        conn.close()
