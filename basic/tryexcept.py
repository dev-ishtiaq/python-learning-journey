# try:
#     print(x)
# except:
#     print("except here")    


# try:
#     print(z)
# except NameError:
#     print("Variable is not defined")
# except: 
#     print("Somethin went wrong")        


# try:
#     print("hello")
# except:
#     print("somethinh went wrong")
# else:
#     print("its ok")        


try:
    f = open("demo.txt")
    try:
        f.write("Hello file")
    except:
        print("error")
    finally:
        f.close()
except:
    print("somethin went wrong")        