main_data = {
    "data":[{
        "rh":67.3,"pod":"n","lon":108.6399,"pres":1004.89,"timezone":"Asia\/Jakarta","ob_time":"2020-07-23 18:23","country_code":"ID","clouds":91,"ts":1595528607,"solar_rad":0,"state_code":"30","city_name":"Sagara","wind_spd":1.63209,"wind_cdir_full":"east-northeast","wind_cdir":"ENE","slp":1008.85,"vis":24,"h_angle":-90,"sunset":"10:54","dni":0,"dewpt":21.7,"snow":0,"uv":0,"precip":0,"wind_dir":74,"sunrise":"23:05","ghi":0,"dhi":0,"aqi":75,"lat":-7.1115,
        "weather":{"icon":"c02n","code":802,"description":"Scattered Clouds"},
        "datetime":"2020-07-23:18","temp":28.3,"station":"WIII","elev_angle":-69.19,"app_temp":30.8
        }],
        "count":1
}

data = main_data['data']

print(data[0]['temp'])