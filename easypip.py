from pip._internal import main as pipmain
try:
    import colorama
except:
    pipmain(['install','colorama'])
    import colorama
    colorama.init(autoreset=True)
class Pipver(object):
    '''...'''
    def __init__(self,
                 input_ver : str,
                 ingore_fail : bool = True,
                 ingore_succ : bool = True):
        '''...'''
        self.ver=input_ver
        self.if_succ=None
        self.ingore_fail=ingore_fail
        self.ingore_succ=ingore_succ
    def Fail(self,
             fail_func = None,
             fail_args = None):
        '''...'''
        self.if_succ=False
        if self.ingore_fail:
            pass
        else:
            try: 
                fail_func(fail_args)
            except Exception as err:
                print('There is something wrong with {} or {} .'.format('fail_func','fail_args'))
                print('The following is the error message:\n'+err+colorama.Fore.RED+'[end of output]')
    def Succ(self,
             succ_func = None,
             succ_args = None):
        '''...'''
        self.if_succ=True
        if self.ingore_succ:
            pass
        else:
            try: 
                succ_func(succ_args)
            except Exception as err:
                print('There is something wrong with {} or {} .'.format('succ_func','succ_args'))
                print('The following is the error message:\n'+err+colorama.Fore.RED+'[end of output]')

class Pipver2:
    def __init__(self, input_ver: str, ignore_fail=True, ignore_succ=True):
        self.ver = input_ver
        self.if_succ = None
        self.ignore_fail = ignore_fail
        self.ignore_succ = ignore_succ
    
    def Fail(self, fail_func=None, fail_args=None):
        self.if_succ = False
        if not self.ignore_fail and fail_func is not None:
            try:
                fail_func(fail_args)
            except Exception as err:
                print(f"There is something wrong with {fail_func} or {fail_args}.")
                print("The following is the error message:\n" + str(err) + colorama.Fore.RED + "[end of output]")
    def Succ(self, succ_func=None, succ_args=None):
        self.if_succ = True
        if not self.ignore_succ and succ_func is not None:
            try:
                succ_func(succ_args)
            except Exception as err:
                print(f"There is something wrong with {succ_func} or {succ_args}.")
                print("The following is the error message:\n" + str(err) + colorama.Fore.RED + "[end of output]")

class Pipack2:
    def __init__(self, input_pack: str, ignore_fail=True, ignore_succ=True):
        self.pack = input_pack
        self.if_succ = None
        self.ignore_fail = ignore_fail
        self.ignore_succ = ignore_succ
    
    def Fail(self, fail_func=None, fail_args=None):
        self.if_succ = False
        if not self.ignore_fail and fail_func is not None:
            try:
                fail_func(fail_args)
            except Exception as err:
                print(f"There is something wrong with {fail_func} or {fail_args}.")
                print("The following is the error message:\n" + str(err) + colorama.Fore.RED + "[end of output]")
    
    def Succ(self, succ_func=None, succ_args=None):
        self.if_succ = True
        if not self.ignore_succ and succ_func is not None:
            try:
                succ_func(succ_args)
            except Exception as err:
                print(f"There is something wrong with {succ_func} or {succ_args}.")
                print("The following is the error message:\n" + str(err) + colorama.Fore.RED + "[end of output]")

class Pipack(object):
    def __init__(self,
                 input_pack : str,
                 ingore_fail : bool = True,
                 ingore_succ : bool = True):
        self.pack=input_pack
        self.if_succ=None
        self.ingore_fail=ingore_fail
        self.ingore_succ=ingore_succ
    def Fail(self,
             fail_func = None,
             fail_args = None):
        self.if_succ=False
        if self.ingore_fail:
            pass
        else:
            try: 
                fail_func(fail_args)
            except Exception as err:
                print('There is something wrong with {} or {} .'.format('fail_func','fail_args'))
                print('The following is the error message:\n'+err+colorama.Fore.RED+'[end of output]')
    def Succ(self,
             succ_func = None,
             succ_args = None):
        self.if_succ=True
        if self.ingore_succ:
            pass
        else:
            try: 
                succ_func(succ_args)
            except Exception as err:
                print('There is something wrong with {} or {} .'.format('succ_func','succ_args'))
                print('The following is the error message:\n'+err+colorama.Fore.RED+'[end of output]')
def Pips(command:str,         
         pack : Pipack | Pipack2 = None,
         version : Pipver | Pipver2= None,
         return_istalled_pack : bool = True,
         fail_func = None,
         succ_func = None,
         fail_args = None,
         succ_args = None,
        ):
    if version.ver==None :
        v=''
    else:
        v='=='
    pac_and_ver=pack.pack+v+version.ver
    try:
        pipmain([command,pac_and_ver])
    except:
        if version.ingore_fail:
            pass
        else:
            ffunc=fail_func
            fargs=fail_args
            version.Fail(fail_func=ffunc,fail_args=fargs)
            pack.Fail(fail_func=ffunc,fail_args=fargs)            
    if version.ingore_succ:
        pass
    else:
        sfunc=succ_func
        sargs=succ_args
        version.Succ(succ_func=sfunc,succ_args=sargs)
        pack.Succ(succ_func=sfunc,succ_args=sargs)
    
    if return_istalled_pack:
        return __import__(pack)

