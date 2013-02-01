import sublime, sublime_plugin, string
from random import sample, choice, randrange

class PasswordCommand(sublime_plugin.TextCommand):
    chars = "23456789abcdefghijkmnpqrstuvwxyzABCDEFGHKMNPQRSTUVWXYZ"
    
    def run(self, edit):
        p = ''.join(sample(self.chars, self.length()))
        for region in self.view.sel():
            self.view.replace(edit, region, p)

    def length(self):
        return randrange(6, 31)

class GenerateShortPasswordCommand(PasswordCommand):
    def length(self):
        return randrange(6, 9)

class GenerateMediumPasswordCommand(PasswordCommand):
    def length(self):
        return randrange(9, 14)

class GenerateLongPasswordCommand(PasswordCommand):
    def length(self):
        return randrange(14, 20)

class GenerateSecurePasswordCommand(PasswordCommand):
    chars = string.letters + string.digits
    def length(self):
        return randrange(20, 31)