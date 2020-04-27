from spyre import server
import pandas as pd

class MyApp(server.App):
    title = "Lab2"

    inputs = [ {    "type": 'dropdown',
                    "label": 'Choose year',
                    "options": [{'label': str(i), 'value': i} for i in range(1982, 2020)],
                    'key': 'year',
                    'value': '1982'},
                {
                    "type":'dropdown',
                    "label": 'Choose province',
                    "options" : [ {"label": "Вінницька", "value":"1"},
                                  {"label": "Волинська", "value":"2"},
                                  {"label": "Дніпропетровська", "value":"3"},
                                  {"label": "Донецька", "value":"4"},
                                  {"label": "Житомирська", "value":"5"},
                                  {"label": "Закарпатська", "value":"6"},
                                  {"label": "Запорізька", "value":"7"},
                                  {"label": "Івано-Франківська", "value":"8"},
                                  {"label": "Київська", "value":"9"},
                                  {"label": "Кіровоградська", "value":"10"},
                                  {"label": "Луганська", "value":"11"},
                                  {"label": "Львівська", "value":"12"},
                                  {"label": "Миколаївська", "value":"13"},
                                  {"label": "Одеська", "value":"14"},
                                  {"label": "Полтавська", "value":"15"},
                                  {"label": "Рівенська", "value":"16"},
                                  {"label": "Сумська", "value":"17"},
                                  {"label": "Тернопільська", "value":"18"},
                                  {"label": "Харківська", "value":"19"},
                                  {"label": "Херсонська", "value":"19"},
                                  {"label": "Хмельницька", "value":"20"},
                                  {"label": "Черкаська", "value":"21"},
                                  {"label": "Чернівецька", "value":"22"},
                                  {"label": "Чернігівська", "value":"23"},
                                  {"label": "Крим", "value":"24"}],
                    "key": 'province'
                },
                {
                    "type" : 'text',
                    "key" : 'min',
                    "label" : 'Choose min week'
                },
                {
                    "type" : 'text',
                    "key" : 'max',
                    "label" : 'Choose max week'
                }
                    
            ]

    outputs = [ {   'type': 'table',
                    'id': 'table1',
                    'control_id': 'submit',
                    'tab': 'Table1'
                    },
                {   'type': 'plot',
                    'id': 'plot1',
                    'control_id': 'submit',
                    'tab': 'Plot1'},
                    {'type': 'table',
                    'id': 'table2',
                    'control_id': 'submit',
                    'tab': 'Table2'},
                    {   'type': 'plot',
                    'id': 'plot2',
                    'control_id': 'submit',
                    'tab': 'Plot2'}
                    ]

    controls = [{   "type": 'button',
                    'id': 'submit',
                    'label': 'Submit'   }]

    tabs = ["Plot1", "Table1", "Plot2", "Table2"]

    def table1(self, params):
        name='Data/vhi_{}.csv'
        df = pd.DataFrame()
        year = int(params['year'])
        min_week = int(params['min'])       
        max_week = int(params['max']) 
        province = int(params['province'])
        temp = pd.read_csv(name.format(province), sep='[, ]+', engine='python')
        df = df.append(temp, ignore_index=True)
        f = df[(df['year'] == year) & (df['week'] >= min_week) & (df['week'] <= max_week)][['year', 'week', 'VHI', 'TCI', 'VCI']]
        return f

    def table2(self, params):
        name='Data/vhi_{}.csv'
        year = int(params['year'])
        min_week = int(params['min'])       
        max_week = int(params['max']) 
        province = int(params['province'])
        df = pd.read_csv(name.format(province), sep='[, ]+', engine='python')
        Month = []
        Week = []
        VHI = []
        Year = []
        for week in range(min_week, max_week + 1):
            month = week // 4.34 + 1
            Year.append(year)
            Month.append(month)
            Week.append(week)
            y2019 = df[(df['week'] == week) & (df['year'] == year)]['VHI']
            VHI.append(y2019)
        df3 = pd.DataFrame({'Year': Year, 'Month': Month, 'Week': Week, 'VHI': VHI})
        return df3

    def plot1(self, params):
        f1 = self.table1(params)
        f = f1[['VCI', 'TCI', 'VHI']]
        return f.set_index(f1['week']).plot()


    def plot2(self, params):
        f1 = self.table1(params)
        f = f1[['VHI']]
        return f.set_index(f1['week']).plot()

app = MyApp()
app.launch(port = 9090)