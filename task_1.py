def convtomin(t_val, t_msr):
    if t_msr == 'h':
        return t_val*60
    elif t_msr == 'm':
        return t_val
    elif t_msr == 's':
        return t_val//60
    else:
        return 'Недопустимое значение времени' 

str_t = '1h 45m,360s,25m,30m 120s,2h 60s'
lst_str_t = str_t.split(',')
cnt_m = 0
for t_str in lst_str_t:
    for t_val in t_str.split(' '):
        cnt_m += convtomin(int(t_val[:-1]), t_val[-1])
print(cnt_m)
