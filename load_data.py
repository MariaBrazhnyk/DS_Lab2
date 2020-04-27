from urllib import request

def preprocess_raw_data(line):  
    if '/' in line:
        return ''         
    line = line.replace(' ', ',',2)   
    return (line + '\n') 

def loadVHI(): 
    url = "https://www.star.nesdis.noaa.gov/smcd/emb/vci/VH/get_provinceData.php?country=UKR&provinceID={}&year1=1981&year2=2019&type=Mean"
    base_filename = "vhi_" 
    for i in range(1, 28): 
        if i == 12 or i == 20: #если Киев,Севастополь, то пропускаем их
            continue
        j = swap_id(i) #меняем индексы областей
        print('{}{}{}'.format('loading vhi_', j, '.csv'))   
        local_url = url.format(str(i)) 
        response = request.urlopen(local_url)
        csv = response.read() # read() возвращает двоичные данные
        csv_str = str(csv)     
        lines = csv_str.split("\\n")  #разбиваем строку на части и возвращаем эти части списком
        with open(base_filename + str(j) + ".csv", "w") as fx:  
            fx.write("year,week,SMN,SMT,VCI,TCI,VHI\n")
            for line in lines:   
                fx.write(preprocess_raw_data(line)) 
                

def swap_id(i): 
    my_dict = { 
    1:22,
    2:24,
    3:23,
    4:25,
    5:3,
    6:4,
    7:8,
    8:19,
    9:20,
    10:21,
    11:9,
    13:10,
    14:11,
    15:12,
    16:13,
    17:14,
    18:15,
    19:16,
    21:17,
    22:18,
    23:6,
    24:1,
    25:2,
    26:7,
    27:5
}
    return my_dict[i]

loadVHI()