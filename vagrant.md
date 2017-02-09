Установить virtualbox и vagrant

Скачать образ
https://drive.google.com/open?id=0ByuSz65Dcv1ldkpzQ2k2ZThZYmM

```
vagrant box add pyneng pyneng_course.box
vagrant init pyneng
```
Если нужна графика:
Открыть файл Vagrantfile и раскомментировать строки:
```
config.vm.provider "virtualbox" do |vb|
     vb.gui = true
   end
```

После этого:
```
vagrant up
```

Username: vagrant

Password: vagrant

Графику запустить можно так:
```
startxfce4&
```

Просто по SSH подключаться так:
```
vagrant ssh
```

В виртуалке должна быть настроена сеть. И изнутри виртуалки доступна хостовая система.

В виртуалке установлены редакторы: vim и Geany (на рабочем столе есть иконка).

Каталоги с примерами и упражнениями находятся в каталоге pyneng_files.

Все модули, которые нужны в курсе, установлены в виртуальном окружении pyneng:
```
workon pyneng
```
