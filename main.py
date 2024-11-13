import inspect, logging, platform , requests, sys
from datetime import datetime

s_system = platform.system()
if s_system == "Linux":
    folder_path = '/'.join(
            inspect.getfile(  inspect.currentframe()  )\
                .split('/')[0:-1]
    ) + '/'+'DATA/RESULT/'
elif s_system == "Windows":
    folder_path = '\\'.join(
            inspect.getfile(  inspect.currentframe()  )\
                .split('\\')[0:-1]
    ) + '\\'+'DATA\\RESULT\\'

logging.info(   f'⚠️ FOLDER PATH TO SAVE RESULTAS ⏩ {folder_path}'   ) ;  print(f'⚠️ FOLDER PATH TO SAVE RESULTAS ⏩ {folder_path}')
logging.info(   f'⚠️ EL SISTEMA OPERATIVO ⏩ {s_system}'   ) 
logging.info(    f"Default encoding: {sys.getdefaultencoding()}"    )
s_fecha_inicio_ejecucion = str(  datetime.today().strftime('%Y-%m-%d %H-%M-%S') ) ; s_fecha_inicio_ejecucion=''

# s_result = folder_path +'\\DATA\\RESULT\\result.html'
s_result = folder_path +'result.html'
s_path_result_to_save = folder_path +'result.html'
# s_path_result_to_save = folder_path  +'DATA\\RESULT\\results_Google_'+ s_fecha_inicio_ejecucion   + '.html'

s_target_url = "https://www.bing.com/search?pglt=43&q=qu%C3%A9+han+aprobado+en+el+congreso+de+diputados+after%3A11-11-2024"
# https://www.google.com/search?q=qu%C3%A9+han+aprobado+en+el+congreso+de+diputados+after%3A11-11-2024

s_UserAgent = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36","Accept-Language":"en-US,en;q=0.9","Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","Accept-Encoding":"gzip, deflate, br","upgrade-insecure-requests":"1"}
# ➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖
resp = requests.get(   s_target_url,
                    headers = s_UserAgent   )
resp.encoding = 'utf-8' 

s_result = resp.text
# ➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖
with open(s_path_result_to_save, 'w', encoding='utf-8') as file:
    file.write(resp.text)

s_fecha_fin_ejecucion = str(  datetime.today().strftime('%Y-%m-%d %H-%M-%S') )
