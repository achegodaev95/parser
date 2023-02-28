Руководство пользователя.
Представленное приложение предназначено для поиска и скачивания научных статей по пользовательскому запросу

Элементы управления:
1.	Ввод ключевых слов. Ключевые слова должны быть разделены пробелами. При этом они могут представлять собой предложения.
2.	Ввод авторов. Авторы должны быть разделены запятой с пробелом. Допускается пустое поле.
3.	Ввод стоп-слов. Стоп-слова должны быть разделены запятой с пробелом. Допускается пустое поле.
4.	Ввод числа максимального количества обрабатываемых страниц результатов. Каждая страница имеет по 50 результатов. Таким образом, 5 страниц результатов означают обработку до 250 результатов (при их наличии). Значение по умолчанию: 1 (до 50 результатов).
5.	Поле вывода найденных результатов. Каждый результат характеризуется названием, авторами и ссылкой на скачивание статьи в формате pdf.
6.	Кнопка «Сохранить в файл» – позволяет сохранить результаты парсинга из списка результатов в текстовый файл для дальнейшего изучения или обработкой сторонним программным обеспечением. Требуется указать путь для сохранения файла.
7.	Кнопка «Скачать выделенное» – позволяет загрузить pdf-файл выбранного элемента из списка результатов. Требуется указать путь для сохранения файла.
8.	Кнопка «Скачать все файлы» – позволяет скачать все pdf-файлы статей из списка результатов. Требуется указать путь для сохранения файлов (папку).
9.	Кнопка «Очистить список» – очистка списка найденных результатов.
10.	Кнопка «Запустить парсинг» – запуск процесса парсинга и добавления результатов в список. Стоит учитывать, что процесс парсинга занимает некоторое время, которое зависит от количества обрабатываемых страниц результатов. В процессе работы программа может не отвечать на действия пользователя (не перетаскиваться и т.д.).

Возможные проблемы и способы их решения:
1.	Нет результатов. Возможна ошибка сетевого соединения – необходимо проверить корректность интернет-подключения. Поле ключевых слов не должно быть пустое.
Вывод команды ping google.com при наличии интернет-соединения. Пакеты не должны быть потеряны в процессе запросов.
2.	Ошибки или падения программы при попытке запуска парсинга. Необходимо проверить, чтобы все поля имели корректный формат. Например, ключевые слова, авторы, стоп-слова должны быть разделены между собой запятой, после которой следует пробел, а затем следующее слово. Данное замечание не относится к списку ключевых слов.
3.	Ошибка сохранения в файл. Необходимо проверить, что накопитель доступен и готов к записи файлов.
4.	Результаты парсинга нерелевантны. Необходимо проверить, что в поле ключевых слов указаны нужные ключевые слова или предложение. Слишком общая формулировка может привести к снижению точности выводимых результатов.
5.	Ошибка скачивания pdf-файла статьи. Необходимо проверить, что в названии файла для сохранения отсутствуют недопустимые символы для его пути в операционной системе Windows.

Также стоит отметить, что скачивание pdf-файла статьи в зависимости от его размера может занять некоторое время (обычно от нескольких секунд до пары минут).
 
