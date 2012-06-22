import threading

class WriteFile(threading.Thread):

    def __init__(self, data, filename):
        self.__data = data; self.__filename = filename
        threading.Thread.__init__(self)

    def run(self):
        print 'Writting', self.__filename
        myfile = open(self.__filename,'w')
        for line in data:
            myfile.write(line+'\n')
        myfile.close()
        print self.__filename, 'is written !'


data = ["coucou %i" %i for i in range(10000)]
files = ["file%i" %i for i in range(10)]

job = []
for index, oneFile in enumerate(files):
    job.append(WriteFile(data[index], oneFile))
    job[index].start()

print "coucou, je peux travailler qd meme !!!"

