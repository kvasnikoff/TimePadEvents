from django.http import HttpResponse
import requests
from datetime import datetime, date, time, timedelta

#организации, мероприятия которых мы берем, разбитые по категориям. Пригодится для API

all_ids = '&organization_ids=112048,96892,108856,112048,22493,54324,110765,72736,69272,119918,113356,104358,123515,2381,4598,7447,70317,8680,2599,111924,42303,109455,55,124518,55575'
excurs_ids = '&organization_ids=112048,96892,108856,131400'
science_ids = '&organization_ids=22493,54324,110765,72736,69272,119918'
culture_ids = '&organization_ids=113356,104358,123515,2381,4598,7447,70317,8680'
entertainment_ids = '&organization_ids=2599,111924,42303,54853'
startups_ids = '&organization_ids=109455,55'
english_ids = '&organization_ids=55575'




def mainfunc(request):
    dt = datetime.now().date() # текущая дата
    d1 = dt + timedelta(days=1)
    d2 = d1 + timedelta(days=1)
    d3 = d1 + timedelta(days=2)
    d4 = d1 + timedelta(days=3)
    d5 = d1 + timedelta(days=4)
    d6 = d1 + timedelta(days=5)

    #смотрим, какая страница запрашивает функцию, чтобы вывести нужные мероприятия

    ids = ''


    if request.path == '/':
        ids = all_ids
    elif request.path == '/excurs' or request.path == '/excurs/':
        ids = excurs_ids
    elif request.path == '/science' or request.path == '/science/':
        ids = science_ids
    elif request.path == '/culture' or request.path == '/culture/':
        ids = culture_ids
    elif request.path == '/entertainment' or request.path == '/entertainmant/':
        ids = entertainment_ids
    elif request.path == '/startups' or request.path == '/startups/':
        ids = startups_ids
    elif request.path == '/english' or request.path == '/english/':
        ids = english_ids
    
    
   #API-ключ (опционально) 
   api key = 'token= ' + '&'
    


    #ссылки на API на 6 дней начиная с сегодняшнего. Меняется только дата

    url0 = 'https://api.timepad.ru/v1/events.json?' + api_key + 'skip=0&cities=Москва' + ids + '&fields=organization&sort=+starts_at&price_max=0' + '&starts_at_min=' + dt.strftime(
        '%Y/%m/%d') + '&starts_at_max=' + d1.strftime('%Y/%m/%d')
    url1 = 'https://api.timepad.ru/v1/events.json?' + api_key + 'skip=0&cities=Москва' + ids + '&fields=organization&sort=+starts_at&price_max=0' + '&starts_at_min=' + d1.strftime(
        '%Y/%m/%d') + '&starts_at_max=' + d2.strftime('%Y/%m/%d')
    url2 = 'https://api.timepad.ru/v1/events.json?' + api_key + 'skip=0&cities=Москва' + ids + '&fields=organization&sort=+starts_at&price_max=0' + '&starts_at_min=' + d2.strftime(
        '%Y/%m/%d') + '&starts_at_max=' + d3.strftime('%Y/%m/%d')
    url3 = 'https://api.timepad.ru/v1/events.json?' + api_key + 'skip=0&cities=Москва' + ids + '&fields=organization&sort=+starts_at&price_max=0' + '&starts_at_min=' + d3.strftime(
        '%Y/%m/%d') + '&starts_at_max=' + d4.strftime('%Y/%m/%d')
    url4 = 'https://api.timepad.ru/v1/events.json?' + api_key + 'skip=0&cities=Москва' + ids + '&fields=organization&sort=+starts_at&price_max=0' + '&starts_at_min=' + d4.strftime(
        '%Y/%m/%d') + '&starts_at_max=' + d5.strftime('%Y/%m/%d')
    url5 = 'https://api.timepad.ru/v1/events.json?' + api_key + 'skip=0&cities=Москва' + ids + '&fields=organization&sort=+starts_at&price_max=0' + '&starts_at_min=' + d5.strftime(
        '%Y/%m/%d') + '&starts_at_max=' + d6.strftime('%Y/%m/%d')

    #переводим полученные запросы в строки

    data0 = requests.get(url0).json()
    data1 = requests.get(url1).json()
    data2 = requests.get(url2).json()
    data3 = requests.get(url3).json()
    data4 = requests.get(url4).json()
    data5 = requests.get(url5).json()

    #одна из частей, которую мы возвращаем -- меню (html + css код)

    archive0 = '<title>Kvasnikoff TimePad – лучшие бесплатные мероприятия Москвы</title><link rel="shortcut icon" type="image/png" href="https://kvasnikoff.com/wp-content/uploads/2018/03/navigate-to-start-letter-k-sign-3.png"/><div class="container"><section class="section section-stats"><div class="card-panel"><div class="row"><div class="col right"><h6><a href="https://kvasnikoff.com"><font color="FIREBRICK">Основной сайт</font></a></h6></div><div class="col left"><h6> <a href="/">🏠</a></h6></div><div class="col right"><h6><a href="/startups">Стартапы</a></h6></div><div class="col right"><h6><a href="/english">Английский</a></h6></div><div class="col right"><h6><a href="/entertainment">Развлечения</a></h6></div><div class="col right"><h6><a href="/excurs">Экскурсии</a></h6></div><div class="col right"><h6><a href="/science">Наука</a></h6></div><div class="col right"><h6><a href="/culture">Культура</a></h6></div></div></div></section></div>'

    #начинаем обрабатывать первый день
    # если событий на этот день нет, то пишем, что их нет
    if data0["total"] == 0:
        archive0 = archive0 + '<style>html{background-color:#F2F2F2;} .section-stats .card-panel {margin: 8px;border-radius:12px;padding25px;}</style> <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0-rc.2/css/materialize.min.css"> <div class ="container"><section class ="section section-stats"><div class ="col 14">' + '<div class ="card-panel center"><i><h5>На %s мероприятий на найдено</h5></i></div></div></section></div>' % dt.strftime(
            '%d/%m/%Y') + ' ' + '<br/>'
    else: #если есть, то сначала выводим число, потом сами мероприятия
        archive0 = archive0 + '<style>html{background-color:#F2F2F2;} .section-stats .card-panel {margin: 8px;border-radius:12px;padding25px;}</style> <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0-rc.2/css/materialize.min.css"> <div class ="container"><section class ="section section-stats"><div class ="col 14">' + '<div class ="card-panel center"><h5>Мероприятия на %s:</h5></div></div></section></div>' % dt.strftime(
            '%d/%m/%Y') + ' ' + '<br/>'
        for i in data0['values']:
            archive0 = archive0 + '<style>html{background-color:#F2F2F2;} .section-stats .card-panel {margin: 8px;border-radius:12px;padding25px;}</style> <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0-rc.2/css/materialize.min.css"> <div class ="container"><section class ="section section-stats"><div class ="col 14">' + '<div class ="card-panel"><h5><b><a href="{0}">{1}</a></b></h5>'.format(
                i['url'], i['name']) + '<h6>Организатор: %s</h6>' % (
                       i['organization']['name']) + '<h6>Начало: %s</h6></div></div></section></div>' % str(
                i['starts_at'])[11:16] + ' ' + '<br/>'
    #аналогично для остальных дней
    archive1 = ''
    if data1["total"] == 0:
        archive1 = '<style>html{background-color:#F2F2F2;} .section-stats .card-panel {margin: 8px;border-radius:12px;padding25px;}</style> <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0-rc.2/css/materialize.min.css"> <div class ="container"><section class ="section section-stats"><div class ="col 14">' + '<div class ="card-panel center"><i><h5>На %s мероприятий на найдено</h5></i></div></div></section></div>' % d1.strftime(
            '%d/%m/%Y') + ' ' + '<br/>'
    else:
        archive1 = '<style>html{background-color:#F2F2F2;} .section-stats .card-panel {margin: 8px;border-radius:12px;padding25px;}</style> <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0-rc.2/css/materialize.min.css"> <div class ="container"><section class ="section section-stats"><div class ="col 14">' + '<div class ="card-panel center"><h5>Мероприятия на %s:</h5></div></div></section></div>' % d1.strftime(
            '%d/%m/%Y') + ' ' + '<br/>'
        for i in data1['values']:
            archive1 = archive1 + '<style>html{background-color:#F2F2F2;} .section-stats .card-panel {margin: 8px;border-radius:12px;padding25px;}</style> <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0-rc.2/css/materialize.min.css"> <div class ="container"><section class ="section section-stats"><div class ="col 14">' + '<div class ="card-panel"><h5><b><a href="{0}">{1}</a></b></h5>'.format(
                i['url'], i['name']) + '<h6>Организатор: %s</h6>' % (
                       i['organization']['name']) + '<h6>Начало: %s</h6></div></div></section></div>' % str(
                i['starts_at'])[11:16] + ' ' + '<br/>'

    archive2 = ''
    if data2["total"] == 0:
        archive2 = '<style>html{background-color:#F2F2F2;} .section-stats .card-panel {margin: 8px;border-radius:12px;padding25px;}</style> <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0-rc.2/css/materialize.min.css"> <div class ="container"><section class ="section section-stats"><div class ="col 14">' + '<div class ="card-panel center"><i><h5>На %s мероприятий на найдено</h5></i></div></div></section></div>' % d2.strftime(
            '%d/%m/%Y') + ' ' + '<br/>'
    else:
        archive2 = '<style>html{background-color:#F2F2F2;} .section-stats .card-panel {margin: 8px;border-radius:12px;padding25px;}</style> <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0-rc.2/css/materialize.min.css"> <div class ="container"><section class ="section section-stats"><div class ="col 14">' + '<div class ="card-panel center"><h5>Мероприятия на %s:</h5></div></div></section></div>' % d2.strftime(
            '%d/%m/%Y') + ' ' + '<br/>'
        for i in data2['values']:
            archive2 = archive2 + '<style>html{background-color:#F2F2F2;} .section-stats .card-panel {margin: 8px;border-radius:12px;padding25px;}</style> <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0-rc.2/css/materialize.min.css"> <div class ="container"><section class ="section section-stats"><div class ="col 14">' + '<div class ="card-panel"><h5><b><a href="{0}">{1}</a></b></h5>'.format(
                i['url'], i['name']) + '<h6>Организатор: %s</h6>' % (
                       i['organization']['name']) + '<h6>Начало: %s</h6></div></div></section></div>' % str(
                i['starts_at'])[11:16] + ' ' + '<br/>'

    archive3 = ''
    if data3["total"] == 0:
        archive3 = '<style>html{background-color:#F2F2F2;} .section-stats .card-panel {margin: 8px;border-radius:12px;padding25px;}</style> <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0-rc.2/css/materialize.min.css"> <div class ="container"><section class ="section section-stats"><div class ="col 14">' + '<div class ="card-panel center"><i><h5>На %s мероприятий на найдено</h5></i></div></div></section></div>' % d3.strftime(
            '%d/%m/%Y') + ' ' + '<br/>'
    else:
        archive3 = '<style>html{background-color:#F2F2F2;} .section-stats .card-panel {margin: 8px;border-radius:12px;padding25px;}</style> <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0-rc.2/css/materialize.min.css"> <div class ="container"><section class ="section section-stats"><div class ="col 14">' + '<div class ="card-panel center"><h5>Мероприятия на %s:</h5></div></div></section></div>' % d3.strftime(
            '%d/%m/%Y') + ' ' + '<br/>'
        for i in data3['values']:
            archive3 = archive3 + '<style>html{background-color:#F2F2F2;} .section-stats .card-panel {margin: 8px;border-radius:12px;padding25px;}</style> <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0-rc.2/css/materialize.min.css"> <div class ="container"><section class ="section section-stats"><div class ="col 14">' + '<div class ="card-panel"><h5><b><a href="{0}">{1}</a></b></h5>'.format(
                i['url'], i['name']) + '<h6>Организатор: %s</h6>' % (
                       i['organization']['name']) + '<h6>Начало: %s</h6></div></div></section></div>' % str(
                i['starts_at'])[11:16] + ' ' + '<br/>'

    archive4 = ''
    if data4["total"] == 0:
        archive4 = '<style>html{background-color:#F2F2F2;} .section-stats .card-panel {margin: 8px;border-radius:12px;padding25px;}</style> <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0-rc.2/css/materialize.min.css"> <div class ="container"><section class ="section section-stats"><div class ="col 14">' + '<div class ="card-panel center"><i><h5>На %s мероприятий на найдено</h5></i></div></div></section></div>' % d4.strftime(
            '%d/%m/%Y') + ' ' + '<br/>'
    else:
        archive4 = '<style>html{background-color:#F2F2F2;} .section-stats .card-panel {margin: 8px;border-radius:12px;padding25px;}</style> <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0-rc.2/css/materialize.min.css"> <div class ="container"><section class ="section section-stats"><div class ="col 14">' + '<div class ="card-panel center"><h5>Мероприятия на %s:</h5></div></div></section></div>' % d4.strftime(
            '%d/%m/%Y') + ' ' + '<br/>'
        for i in data4['values']:
            archive4 = archive4 + '<style>html{background-color:#F2F2F2;} .section-stats .card-panel {margin: 8px;border-radius:12px;padding25px;}</style> <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0-rc.2/css/materialize.min.css"> <div class ="container"><section class ="section section-stats"><div class ="col 14">' + '<div class ="card-panel"><h5><b><a href="{0}">{1}</a></b></h5>'.format(
                i['url'], i['name']) + '<h6>Организатор: %s</h6>' % (
                       i['organization']['name']) + '<h6>Начало: %s</h6></div></div></section></div>' % str(
                i['starts_at'])[11:16] + ' ' + '<br/>'

    archive5 = ''
    if data5["total"] == 0:
        archive5 = '<style>html{background-color:#F2F2F2;} .section-stats .card-panel {margin: 8px;border-radius:12px;padding25px;}</style> <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0-rc.2/css/materialize.min.css"> <div class ="container"><section class ="section section-stats"><div class ="col 14">' + '<div class ="card-panel center"><i><h5>На %s мероприятий на найдено</h5></i></div></div></section></div>' % d5.strftime(
            '%d/%m/%Y') + ' ' + '<br/>'
    else:
        archive5 = '<style>html{background-color:#F2F2F2;} .section-stats .card-panel {margin: 8px;border-radius:12px;padding25px;}</style> <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0-rc.2/css/materialize.min.css"> <div class ="container"><section class ="section section-stats"><div class ="col 14">' + '<div class ="card-panel center"><h5>Мероприятия на %s:</h5></div></div></section></div>' % d5.strftime(
            '%d/%m/%Y') + ' ' + '<br/>'
        for i in data5['values']:
            archive5 = archive5 + '<style>html{background-color:#F2F2F2;} .section-stats .card-panel {margin: 8px;border-radius:12px;padding25px;}</style> <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0-rc.2/css/materialize.min.css"> <div class ="container"><section class ="section section-stats"><div class ="col 14">' + '<div class ="card-panel"><h5><b><a href="{0}">{1}</a></b></h5>'.format(
                i['url'], i['name']) + '<h6>Организатор: %s</h6>' % (
                       i['organization']['name']) + '<h6>Начало: %s</h6></div></div></section></div>' % str(
                i['starts_at'])[11:16] + ' ' + '<br/>'

    #источники
    sources = '<div class ="container"><section class ="section section-stats"><div class ="col 14">' + '<div class ="card-panel center"><h5>Источники мероприятий <a href="https://docs.google.com/document/d/1-XSMFfqXapsiNg79NNf7i5Tg-l9orX42BC_XjFiXaaQ/">доступны по ссылке</a> </h5></div></div></section></div>' + '<br/>'
    #лого
    kvasnikoff = '<center><div class ="container"><object data="https://kvasnikoff.com/wp-content/uploads/2018/03/Kvasnikov_final_logo.svg" type="image/svg+xml" class="mailicon"></object></div></center>' + '<br/>'
    final = archive0 + '<br/>' + archive1 + '<br/>' + archive2 + '<br/>' + archive3 + '<br/>' + archive4 + '<br/>' + archive5 + '<br/>' + sources + kvasnikoff
    return (HttpResponse(final))
