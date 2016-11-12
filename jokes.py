from errbot import BotPlugin, botcmd
import os, json, random

#Version 1.0, 2016.11.12
#Arttu Huttunen, Oulu, Finland <arttuhut@gmail>

class Jokes(BotPlugin):
    """Tells a joke from a list."""
            
    def __init__(self, dummy=None): #sometimes there seems to be an extra argument
        self.datafile = 'jokes.txt' 
    
    @botcmd
    def joke(self, msg, args):
        """Tells a random joke. With number as an argument gives specific joke."""
       
       #if no arguments, args = ''
        output = 'No jokes.'

        if os.path.isfile(self.datafile):    
            with open(self.datafile, 'r') as file:
                data=json.load(file)

            if args=='':
                output = data[random.randint(0, len(data)-1)]
            else:
                try:
                    output = data[int(args)-1]
                except:
                   output = 'Good not parameters is. Must number be. Not larger'\
                   ' than ' + str(len(data)) +'.'
                   
        return output


    @botcmd
    def jokeadd(self, msg, args):
        """Add a joke to the list. Usage: jokeadd Your joke here. """
        
        if os.path.isfile(self.datafile):    
            with open(self.datafile, 'r') as file:
                data=json.load(file)
        else:
            data = ['What do you give your favourite electrical engineer on'\
            ' Christmas? \n - Shorts!']
        
        if args != '':      
            output = args
            data.append(args)
            with open(self.datafile, 'w') as outfile:
                json.dump(data, outfile)
        else: 
            output = 'None is your joke.'
        
        return output
        

    @botcmd
    def jokeremove(self, msg, args):
        """Remove a joke from the list. To remove joke number 5: jokeremove 5"""
        
        output = 'Think joke remove did I.'

        if os.path.isfile(self.datafile):    
            with open(self.datafile, 'r') as file:
                data=json.load(file)

            if args =='':
                output = 'The number of joke to remove give. Jokes have we: '+ \
                str(len(data))
            else:
                try:
                    del data[int(args)-1]
                    with open(self.datafile, 'w') as outfile:
                        json.dump(data, outfile)                    
                    
                except:
                    output = 'The command a failure is.'

                
        else:
            output = 'No joke file.'
                
        return output       