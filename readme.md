В данном примере реализован паттерн "Посредник" для управления несколькими окнами интерфейса. Класс WindowMediator служит посредником, который управляет отображением и скрытием окон, обеспечивая их взаимодействие. 

### Классы

    WindowBase: Абстрактный базовый класс для всех окон. Определяет методы show() и hide(), которые должны быть реализованы в подклассах.

    MainWindow: Реализация главного окна. Содержит методы show() и hide(), которые выводят соответствующие сообщения.

    SettingWindow: Реализация окна настроек. Также реализует методы show() и hide() для отображения сообщений.

    HelpWindow: Реализация окна помощи. Содержит аналогичные методы для отображения сообщений.
    
    WindowMediator: Посредник, который управляет всеми окнами. Содержит словарь с экземплярами окон и предоставляет метод show(win), который отвечает за показ одного окна и скрытие остальных.

### Методы взаимодействия

    show(win) (в классе WindowMediator):
        Принимает объект окна в качестве аргумента.
        Скрывает все окна, кроме указанного.
        Вызывает метод show() для отображения выбранного окна.

Таким образом, при вызове метода show() на посреднике, он управляет состоянием окон, обеспечивая централизованное взаимодействие между ними без необходимости прямых ссылок между классами окон.

