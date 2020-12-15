
## Creation of program Menu

# File Menu Commands
        self.fileMenu = tk.Menu(self, tearoff= 0)
        self.file_commands = [("Exit", quit)
                              ]
        for commands in self.file_commands:
            self.fileMenu.add_command(label= commands[0],
                                      command= commands[1])
    # Database Menu Commands
        self.databaseMenu = tk.Menu(self, tearoff= 0)
        self.database_commands = [("Create", create_database_window),
                                  ("Change", 'pass'),
                                  ("Settings", 'pass')
                                   ]
        for commands in self.database_commands:
            self.databaseMenu.add_command(label= commands[0],
                                          command= commands[1])
    # Menu Headers
        menus = [("File", self.fileMenu),
                 ("Database", self.databaseMenu)]
        for menu in menus:
            self.add_cascade(label= menu[0], menu= menu[1])
            
#programMenu = Taskbar(root)
#root.config(menu = programMenu)

def create_database_window():

    cd_window = tk.Tk()
    cd_window.title('Create Database')
    cd_frame = CreateDatabaseWindow(cd_window)
    cd_frame.pack()
    

class CreateDatabaseWindow(ttk.Frame):

    def __init__(self, master= None):
        super().__init__(master= master)
        self.create_widgets()

    def create_widgets(self):
        self.db_name_label = ttk.Label(self, text = "Name")
        self.db_name_label.pack()
        self.db_name_entry = ttk.Entry(self)
        self.db_name_entry.pack()
        self.confirm_button = ttk.Button(self, text = "Create")
        self.confirm_button.pack()
        self.cancel_button = ttk.Button(self, text = "Cancel",
                                        command= self.master.destroy)
        self.cancel_button.pack()

###############
##  Classes  ##
###############

class Airport(object):

    def __init__(self):
        pass

class Aircraft(object):

    def __init__(self):
        pass
    

#class LoginPage(ttk.Frame):

#    def __init__(self, master= None):
#        super().__init__(master= master)
