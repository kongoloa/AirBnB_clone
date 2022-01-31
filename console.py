#!/usr/bin/python3
""" command interpreter """


import cmd
from re import findall, sub
from models import clases, storage
from models.base_model import BaseModel
from datetime import datetime
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """ interpreter of commands"""
    prompt = '(hbnb) '
    up_clases = clases

    def do_quit(self, args):
        """ quit command """
        return True

    def do_EOF(self, args):
        """ EOF command """
        print()
        quit()

    def do_help(self, args):
        """ details of a command"""
        cmd.Cmd.do_help(self, args)

    def emptyline(self):
        """ back to the prompt"""
        return

    def do_create(self, args):
        """ Creates a new instance of BaseModel """
        argumentos = args.split(" ")
        if len(args) == 0:
            print("** class name missing **")
            return
        if (argumentos[0] in self.up_clases):
            crear = eval("{}()".format(argumentos[0]))
            crear.save()
            print("{}".format(crear.id))
        else:
            print("** class doesn't exist **")

    def do_show(self, args):
        """ Prints the string representation """
        argumentos = args.split(" ")
        objetos = storage.all()
        try:
            if len(args) == 0:
                print("** class name missing **")
                return
            if (argumentos[0] in self.up_clases):
                if len(argumentos) > 1:
                    llave = argumentos[0]+"."+argumentos[1]
                    if llave in objetos:
                        obj = objetos[llave]
                        print(obj)
                    else:
                        print("** no instance found **")
                else:
                    print("** instance id missing **")
            else:
                print("** class doesn't exist **")
        except AttributeError:
            print("** instance id missing **")

    def do_destroy(self, args):
        """  Deletes an instance based on the class """
        argumentos = args.split(" ")
        objetos = storage.all()
        if len(args) == 0:
            print("** class name missing **")
            return
        if (argumentos[0] in self.up_clases):
            if len(argumentos) < 2:
                print("** instance id missing **")
                return
            llave = argumentos[0]+"."+argumentos[1]
            if llave in objetos:
                obj = objetos[llave]
                if obj:
                    dobj = storage.all()
                    del dobj["{}.{}".format(type(obj).__name__, obj.id)]
                    storage.save()
            else:
                print("** no instance found **")
        else:
            print("** class doesn't exist **")

    def do_all(self, args):
        """ Prints all string representation of all instances """
        argumentos = args.split(" ")
        objetos = storage.all()
        instancias = []
        if len(args) == 0:
            for name in objetos:
                instancias.append(str(objetos[name]))
            print(instancias)
            return
        if (argumentos[0] in self.up_clases):
            for name in objetos:
                if name[0:len(argumentos[0])] == argumentos[0]:
                    instancias.append(str(objetos[name]))
            print(instancias)
        else:
            print("** class doesn't exist **")

    def do_update(self, args):
        """ updates an instance based on the class name and id """
        if len(args) == 0:
            print("** class name missing **")
            return
        argumentos = args.split(" ")
        objetos = storage.all()
        if (argumentos[0] in self.up_clases):
            if len(argumentos) < 2:
                print("** instance id missing **")
                return
            llave = argumentos[0]+"."+argumentos[1]
            if llave in objetos:
                obj = objetos[llave]
                notocar = ["id", "created_at", "updated_at"]
                if obj:
                    argumento = args.split(" ")
                    if len(argumento) < 3:
                        print("** attribute name missing **")
                    elif len(argumento) < 4:
                        print("** value missing **")
                    elif argumento[2] not in notocar:
                        arg3 = argumento[3]
                        if arg3.isdigit():
                            arg3 = int(arg3)
                        elif arg3.replace('.', '', 1).isdigit():
                            arg3 = float(arg3)
                        obj.__dict__[argumento[2]] = arg3
                        obj.updated_at = datetime.now()
                        storage.save()
            else:
                print("** no instance found **")
        else:
            print("** class doesn't exist **")

    def count(self, args):
        """ Retrieve the number of instances
            of a class: <class name>.count()
        """
        argumentos = args.split(" ")
        objetos = storage.all()
        instancias = []
        if len(args) == 0:
            for name in objetos:
                instancias.append(objetos[name])
            print(len(instancias))
        if (argumentos[0] in self.up_clases):
            for name in objetos:
                if name[0:len(argumentos[0])] == argumentos[0]:
                    instancias.append(objetos[name])
            print(len(instancias))

    def build_dict(self, dprm):
        dprm = dprm.replace(" ", "").replace("'", "")
        dprm = dprm.replace('"', '')
        listd = dprm.split(',')
        final_dic = {}
        for i in listd:
            kval = i.split(':')
            value = kval[1]
            if value.isdigit():
                value = int(value)
            elif value.replace('.', '', 1).isdigit():
                value = float(value)
            final_dic[kval[0]] = value
        return final_dic

    def update_from_dict(self, dprm, tokens, msk, objects):
        obj_dic = self.build_dict(dprm)
        classes = self.up_clases
        if tokens[0] in classes:
            if msk in objects:
                obj = objects[msk]
                for k, v in obj_dic.items():
                    setattr(obj, k, v)
                obj.updated_at = datetime.now()
                storage.save()

    def default(self, inp):
        ''' shorthand methods '''
        try:
            methods = {'all()': self.do_all, 'count()': self.count}
            methods2 = {'show': self.do_show, 'destroy': self.do_destroy}
            tokens = inp.split('.', 1)
            if tokens[1] in methods:
                return methods[tokens[1]](tokens[0])
            elif tokens[1].split('(')[0] in methods2:
                key = tokens[1].split('(')[0]
                # id_parm = tokens[1].split('("', 1)[1].split('")')[0]
                id_parm = findall('\(([^)]+)', tokens[1])
                if len(id_parm) != 0:
                    id_m = id_parm[0].split('"', 1)[1].split('"')[0]
                    args = tokens[0] + " " + id_m
                else:
                    args = tokens[0]
                return methods2[key](args)
            elif tokens[1].split('(')[0] == 'update':
                if "{" in tokens[1]:
                    id_key = tokens[1].split('"', 1)[1].split('"')[0]
                    objects = storage.all()
                    msk = tokens[0]+"."+id_key
                    if msk not in objects:
                        print("** no instance found **")
                    dprm = tokens[1].split('{', 1)[1].split('}')[0]
                    if dprm:
                        self.update_from_dict(dprm, tokens, msk, objects)
                else:
                    params = findall('\(([^)]+)', tokens[1])
                    args = tokens[0]
                    if params:
                        newstr = sub(r'''["',]''', '', params[0])
                        if newstr:
                            args = tokens[0] + " " + newstr
                    return self.do_update(args)
        except IndexError:
            pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
