# Парсер сайта-словаря по Английскому языку

Для работы с парсером необходимо установить зависимости, находящиеся в файле requirements.txt

Парсер работает в два этапа, так как парсим сайт со вложенными каталогами.

Для начала необходимо запустить код, который закомментирован, тем самым собираем ссылки на категории и записываем их в json фаил.
Вторым этапом запускаем оставшийся код и собираем необходимые нам слова и выражения с переводом. Каждая категория сохраняется в отдельный json фаил. 