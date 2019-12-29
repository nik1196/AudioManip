import os, math, sys

class AudioManip:
    def __init__(self):
        self.ratio = 1
        self.int_size = 4

        
    def set_ratio(self, r):
        self.ratio = r

        
    def reduce(self, filename):
        file_stats = os.stat(filename)
        file_size = file_stats.st_size
        with open(filename, 'rb') as ifile:
            with open(filename.split('.')[0]+'_reduced.wav', 'wb+') as ofile1:
                header = ifile.read(44)
                ofile1.write(header)
                for byte in range(44,file_size,self.ratio*self.int_size):
                    if byte % 50000 == 0:
                        print(byte, '/', file_size)
                    ifile.seek(byte) 
                    data = ifile.read(4)
                    for i in range(self.ratio):
                        ofile1.write(data)

                        
    def slow1(self, filename):
        file_stats = os.stat(filename)
        file_size = file_stats.st_size
        with open(filename, 'rb') as ifile:
            with open(filename.split('.')[0]+'_slowed1.wav', 'wb+') as ofile2:
                header = bytearray(44)
                ifile.readinto(header)
                print(header[4])
##                header[4:8] = bytearray(int(math.ceil(int.from_bytes(header[40:],sys.byteorder)/ratio)).to_bytes(4,sys.byteorder))
                print(header[4])
                print(header[24])
                header[24:28] = bytearray((int.from_bytes(header[24:28],sys.byteorder)//self.ratio).to_bytes(4,sys.byteorder))
                header[28:32] = bytearray((int.from_bytes(header[28:32],sys.byteorder)//self.ratio).to_bytes(4,sys.byteorder))
                print(header[24])
                ofile2.write(header)
                for byte in range(44,file_size,self.int_size):
                    if byte % 50000 == 0:
                        print(byte, '/', file_size)
                    ifile.seek(byte) 
                    data = ifile.read(self.int_size)
                    ofile2.write(data)

                    
    def slow2(self, filename):
        file_stats = os.stat(filename)
        file_size = file_stats.st_size
        with open(filename, 'rb') as ifile:
            with open(filename.split('.')[0]+'_slowed2.wav', 'wb+') as ofile1:
                header = bytearray(44)
                ifile.readinto(header)
                print(header[4])
##                header[4:8] = bytearray(int(math.ceil(int.from_bytes(header[40:],sys.byteorder)/self.ratio)).to_bytes(4,sys.byteorder))
                print(header[4])
                print(header[24])
                header[24:28] = bytearray((int.from_bytes(header[24:28],sys.byteorder)//self.ratio).to_bytes(4,sys.byteorder))
                header[28:32] = bytearray((int.from_bytes(header[28:32],sys.byteorder)//self.ratio).to_bytes(4,sys.byteorder))
                print(header[24])
                ofile1.write(header)
                for byte in range(44,file_size,self.ratio*self.int_size):
                    if byte % 50000 == 0:
                        print(byte, '/', file_size)
                    ifile.seek(byte) 
                    data = ifile.read(4)
                    for i in range(self.ratio):
                        ofile1.write(data)
                        
    def desample(self, filename):
        file_stats = os.stat(filename)
        file_size = file_stats.st_size
        with open(filename, 'rb') as ifile:
            with open(filename.split('.')[0]+'_desampled.wav', 'wb+') as ofile2:
                header = bytearray(44)
                ifile.readinto(header)
                print(header[4])
                header[4:8] = bytearray(int(math.ceil(int.from_bytes(header[40:],sys.byteorder)/self.ratio)).to_bytes(4,sys.byteorder))
                print(header[4])
                print(header[24])
                header[24:28] = bytearray((int.from_bytes(header[24:28],sys.byteorder)//self.ratio).to_bytes(4,sys.byteorder))
                header[28:32] = bytearray((int.from_bytes(header[28:32],sys.byteorder)//self.ratio).to_bytes(4,sys.byteorder))
                print(header[24])
                ofile2.write(header)
                for byte in range(44,file_size,self.ratio*self.int_size):
                    if byte % 50000 == 0:
                        print(byte, '/', file_size)
                    ifile.seek(byte) 
                    data = ifile.read(self.int_size)
                    ofile2.write(data)

        
        
        
