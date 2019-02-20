import CPSintolSDK as sintolsdk

#args = [c_wchar_p('UnrealRTOS'),c_wchar_p('Admin'),c_wchar_p('C:/SintolRTOS/UnrealRTOS/Binaries/Win64/multiAI.xml')]
#创建联盟参数
arg0 = 'UnrealRTOS'
arg1 = 'Admin'
arg2 = 'C:/SintolRTOS/UnrealRTOS/Binaries/Win64/multiAI.xml'
federaambassador = sintolsdk.RTIambassador(arg0,arg1,arg2)
