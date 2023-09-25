import datetime

x = datetime.datetime.now()
print(x)
print(x.strftime("%B"))
print(x.strftime("%A %d %B %Y"))

'''

%Y: Anno con quattro cifre (es. 2023).
%y: Anno con due cifre (es. 23 per il 2023).
%m: Mese (01-12).
%d: Giorno del mese (01-31).
%H: Ora (00-23).
%M: Minuto (00-59).
%S: Secondo (00-59).
%A: Nome completo del giorno della settimana (es. "Monday").
%a: Nome abbreviato del giorno della settimana (es. "Mon").
%B: Nome completo del mese (es. "January").
%b o %h: Nome abbreviato del mese (es. "Jan").
%p: AM o PM.
%Z: Nome della zona oraria (es. "UTC", "EST").

'''

y = datetime.datetime(2012, 6, 13)
print(y)