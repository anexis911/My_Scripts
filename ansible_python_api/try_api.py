# -*- coding: utf-8 -*-

from collections import namedtuple
from ansible.parsing.dataloader import DataLoader
from ansible.vars import VariableManager
from ansible.inventory import Inventory
from ansible.playbook.play import Play
from ansible.executor.task_queue_manager import TaskQueueManager
from ansible.plugins.callback.json import CallbackModule
import yaml


def run_playbook(inventory_filename, playbook_filename):
    '''
    Эта функция выполняет playbook и возвращает все результаты
    в виде словаря

    Параметры:
        * inventory_filename - имя инвентарного файла
        * playbook_filename - имя playbook
    '''
    variable_manager = VariableManager()
    loader = DataLoader()

    Options = namedtuple('Options',
                    ['connection', 'module_path', 'forks', 'become',
                     'become_method', 'become_user', 'check'])
    options = Options(connection='local', module_path='', forks=100,
        become=False, become_method='', become_user='', check=False)
    passwords = dict(vault_pass='secret')

    inventory = Inventory(loader=loader, variable_manager=variable_manager,
                          host_list=inventory_filename)
    variable_manager.set_inventory(inventory)

    with open(playbook_filename) as f:
        playbook_content = yaml.load(f)

    return_result_dict = {}
    for play_src in playbook_content:
        play = Play().load(play_src, variable_manager=variable_manager, loader=loader)

        tqm = None
        callback = CallbackModule()

        try:
            tqm = TaskQueueManager(
                    inventory=inventory,
                    variable_manager=variable_manager,
                    loader=loader,
                    options=options,
                    passwords=passwords,
                )
            tqm._stdout_callback = callback
            result = tqm.run(play)
        finally:
            if tqm is not None:
                tqm.cleanup()

        return_result_dict[play_src['name']] = callback.results[0]
    return return_result_dict


def stdout_results(inventory_filename, playbook_filename):
    '''
    Функция run_playbook возвращает большой словарь. Не вся информация в нем может пригодится.
    Эта функция возвращает только вывод stdout для каждого хоста.
    Соответственно, эта функция ориентирована на работу с ios_command и подобными модулями,
    где возвращается вывод команд в stdout.

    Можно сделать аналогичные функции для других задач.

    Функция возвращает словарь вида:
    {'play_name': {
        'task1_name': {
            'device1': 'command output',
            'device2': 'command output'},
        'task2_name': {
            'device1': 'command output',
            'device2': 'command output'}}}
    '''
    return_result_dict = {}
    result = run_playbook(inventory_filename, playbook_filename)

    for play in result:
        result_dict = result[play]
        play_dict = {}
        play_tasks = result_dict['tasks']
        for task in play_tasks:
            task_name = task['task']['name']
            play_dict[task_name] = {}
            hosts = task['hosts']
            for ip in hosts:
                stdout = ''
                if 'stdout' in hosts[ip].keys():
                    stdout = hosts[ip]['stdout']
                play_dict[task_name][ip] = stdout
                # Это может пригодиться для понимания какие ключи в словаре
                #print hosts[ip].keys()
        return_result_dict[play] = play_dict
    return return_result_dict


result = stdout_results('myhosts', '1_ios_command.yml')

with open('results.yaml', 'w') as f:
    f.write(yaml.dump(result, default_flow_style=False))


for play in result:
    print '*'*10, play
    for task in result[play]:
        print '#'*10, task
        for device in result[play][task]:
            print device
            print result[play][task][device]
