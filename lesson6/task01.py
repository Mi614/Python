from collections import Counter


def get_spam_ip(log_file):
    with open('log_pars.txt', 'w') as pars_logs:
        with open(log_file, 'r+') as f_logs:
            con = ((line.split()[0], line.split()[5][1:], line.split()[6]) for line in f_logs)
            for el in con:
                print(el, file=pars_logs)

    with open('log_pars.txt', 'r+') as ip_list:
        my_dict = Counter()
        for el in ip_list:
            my_dict[el.split()[0]] += 1
        ip_spammer = my_dict.most_common(1)
    return print(ip_spammer)


get_ip = get_spam_ip('nginx_logs.txt')

