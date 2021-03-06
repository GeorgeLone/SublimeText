#-*- encoding: utf-8 -*-
import sublime, sublime_plugin, datetime

class insertSignatureCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        fileName = self.view.file_name()
        nPos = fileName.rindex('/')+1
        fileName = fileName[nPos:len(fileName)]
        fileLine = "/**\n * @file " + fileName + "\n"
        text_author = """ * @author nobidagu<long88730@gmail.com>\n *\n"""
        date = datetime.datetime.now()
        dateStr = " * @Created on " + date.strftime("%Y/%m/%d") + "\n */\n"
        classBlock = "\nusing UnityEngine;\n\npublic class " + fileName[0:(fileName.index('.'))] + " : MonoBehaviour\n{\n\n}\n"

        text = fileLine + text_author + dateStr + classBlock

        #for region in the selection
        #一个region是一个选择块，一次可以选择多个块
        for r in self.view.sel():
            str_r = self.view.substr(r)#str_r是所选择块的文本内容
            print(str_r)
            if 'Created on ' in str_r:
                if 'Updated on ' in str_r:
                    text = str_r[0:str_r.find('Updated on ')] + 'Updated on ' + dateStr + text_author
                else:
                    text = str_r.replace(text_author, '\nUpdated on ' + dateStr + text_author)
            self.view.erase(edit, r)
            self.view.insert(edit, r.begin(), text)
