import os

os.system("pip3 install scratchclient")

from scratchclient import ScratchSession




username = input("Username: ")
password = input("Password: ")
session = ScratchSession(username, password)
print("Successfully logged in as " + session.username)
    

connection_input = int(input("Insert your scratch project ID: "))
connection = session.create_cloud_connection(connection_input)



@connection.on("set")
def on_set(variable):
    print(variable.name, variable.value)
while (1 < 2) :
    connection.set_cloud_variable("views", session.get_project(723704426).view_count)
    connection.set_cloud_variable("favorites", session.get_project(723704426).favorite_count)
    connection.set_cloud_variable("likes", session.get_project(723704426).love_count)
    connection.set_cloud_variable("comments", len(session.get_project(723704426).get_comments()))
    connection.set_cloud_variable("remixes", len(session.get_project(723704426).get_remixes()))
