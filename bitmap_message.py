import sys
bitmap_message = """
Hello!Hello!Hello!Hello!Hello!Hello!Hello!Hello!Hello!Hello!Hello!He
   lo!Hello!Hello   l  !He lo  e      llo!Hello!Hello!Hello!Hello!He
  llo!Hello!Hello!Hello He lo H  l !Hello!Hello!Hello!Hello!Hello H
 el      lo!Hello!Hello!He       lo!Hello!Hello!Hello!Hello!Hel
          o!Hello!Hello          lo  e lo!H ll !Hello!Hello!H l
           !Hello!He            llo!Hel   Hello!Hello!Hell ! e
            Hello!He           ello!Hello!Hello!Hello!Hell  H
   l        H llo! ell         ello!Hello!Hell !Hello  el o
               lo!H  l         ello!Hello!Hell   ell !He  o
                 !Hello         llo!Hello!Hel    el   He  o
                 !Hello!H        lo!Hello!Hell    l  !H llo
                   ello!Hel         Hello!He          H llo Hell
                   ello!Hell         ello!H  l        Hell !H l o!
                   ello!Hell         ello!H l o           o!H l   H
                     lo!Hel          ello! el             o!Hel   H
                     lo!He            llo! e            llo!Hell
                    llo!H             llo!              llo!Hello
                    llo!              ll                 lo!Hell   e
                    llo                                       l    e
                    ll     l                    H
Hello!Hello!Hello!Hello!Hello!Hello!Hello!Hello!Hello!Hello!Hello!He"""
print('enter the message to display with bitmap')
message = input('...')
if message == '':
    sys.exit()

for i in bitmap_message.splitlines():
    for k,j in enumerate(i): 
        if j ==' ':
            print(' ',end='')
        else:
            print(message[k % len(message)],end='')#this is a  bit tricky the trace would be somthing like
    print()