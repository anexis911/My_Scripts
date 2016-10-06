# -*- coding: utf-8 -*-

import random
import operator
import json
import os

conj = {
        'der':{'G':'des', 'D':'dem', 'A':'den'},
        'das':{'G':'des', 'D':'dem', 'A':'das'},
        'die':{'G':'der', 'D':'den', 'A':'die'},
        'pl':{'G':'der', 'D':'den', 'A':'die'}}

#Файл для сбора статистики
stats = 'conj_stats'

#Количество всех вопросов и неправильных ответов
all_q = {}
wrong_q = {}

test_num = int(raw_input("Сколько тестов Вы хотите пройти? "))


def key_in_d(key, d):
    if key in d:
        d[key] += 1
    else:
        d[key] = 1

def gen_report(alles, wrong):
    report = {}

    for k in alles:
        if k in wrong:
            report[k] = float(wrong[k])/alles[k] * 100
        else:
            report[k] = 0
    sorted_report = sorted(report.items(), key=operator.itemgetter(1), reverse=True)

    for key, val in sorted_report:
        print "%-10s %.2f" % (key, val)


for test in range(test_num):
    art = random.choice(conj.keys())
    con = random.choice(conj['der'].keys())
    r_key = '%s + %s' % (con, art)

    print r_key
    answer = raw_input()

    key_in_d(r_key, all_q)

    if answer == conj[art][con]:
        print "Правильно!"
    else:
        print "Ошибка"
        key_in_d(r_key, wrong_q)

print '-' * 20
print "Ошибок: %s из %s" % (sum(wrong_q.values()), sum(all_q.values()))

print "Статистика для текущего занятия:"
gen_report(all_q, wrong_q)


#Добавляем информацию текущей сесии в файл и выводим суммарную статистику
stats_is_new = not os.path.exists(stats)

if stats_is_new:
    with open(stats, 'w') as stat:
        json.dump([all_q, wrong_q], stat)
        print "Суммарная статистика будет доступна только после двух тестов."
else:
    with open(stats, 'r+') as stat:
        g_all_q, g_wrong_q = json.load(stat)
        for k1 in all_q:
            key_in_d(k1, g_all_q)
        for k2 in wrong_q:
            key_in_d(k2, g_wrong_q)
        stat.seek(0)
        stat.truncate()
        json.dump([g_all_q, g_wrong_q], stat)
        print '-' * 20
        print "Суммарная статистика для всех занятий:"
        gen_report(g_all_q, g_wrong_q)
