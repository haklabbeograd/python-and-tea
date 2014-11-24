def python_workshop(date):
    d = {
    '08.09.2014': 'Radili tool-ing, napravili okvirni plan, upoznali se sa materijom, poceli tipove podataka',
    '15.09.2014': 'Razjasnili nejasnoce oko domaceg string.py, ucili liste i pogledati dictionary za domaci, imali kratku samorefleksiju',
    '22.09.2014': 'Radili domaci list.py, recnike i funkcije, igrali se sa debagerom',
    '29.09.2014': 'Radili domaci wordcount.py, regularne izraze, poceli rekurzivne funkcije, puskice :)',
    '06.10.2014': 'Radili OS module, igrali se sa fajlovima i direktorijumima',
    '13.10.2014': 'Ponovili OS module, OOP, poceli obradjivati klase, objekte i metode',
    '20.10.2014': 'Obnova gradiva, usli smo u sustinu, prakticirali sa pythonom pisali kod za idea_selection',
    '27.10.2014': 'Obnovili gradivo, testirali idea_selection program koji nam je odabrao prvi eko-elektro projekat: ocitavanje temperature u labu i njeno daljinsko menjanje',
    '03.11.2014': 'Povezali tem. senzor na openwrt ruter, pisali i postavili python web aplikaciju na heroku sve komitovali na git kao i obicno :)',
    '10.11.2014': 'Obnovili gradivo, Instalirali digitemp i drajvere za usb-serial, omogucili da ruter otvorene mreze podatke salje na heroku',
    '17.11.2014': 'Debagovali kod, radili kalibraciju, rekurzija, dotakli lisp i haskel, plesali sa algoritmom neutralnog broja',
    '24.11.2014': 'Obnova gradiva, flask, dekoratori, plan alarmnog sistema + poceli skripting, (jacina, vreme, tip, shablon)',
    }
    if 0:
      for k,v in d.items():
        print (k,':', v)
    if 1:
      for k in d:
        print(k, ':', d[k])
python_workshop('stagod')
