<p align="center">
  <img src="docs/v1/Neiros-logo.jpg" width="300">
</p>

Тестовое задание для позиции **junior Python Backend Developer** в Neiros.

Программа реализует CLI для работы с геометрическими фигурами:  
Создание, сохранение, отображение и уаделение фигур, а также взаимодествие со сторонними JSON файлами.

---

## 📂 Структура репозитория
```  
├── editor
      ├── editor.py            # 📄 Класс управления фигурами
      └── menu.py              # 📄 Класс меню программы
├── storage/
      ├── data/
            └── Shapes.json    # 📄 Файл для хранения фигур  
      └── json_storage.py      # 📄 Интерфейс фигур             
├── shapes/
      ├── shape.py             # 📄 Интерфейс фигур
      ├── point.py             # 📄 Класс, описывающий точку
      ├── line.py              # 📄 Класс, описывающий линию
      ├── square.py            # 📄 Класс, описывающий квадрат
      ├── rectangle.py         # 📄 Класс, описывающий прямоугольник
      ├── circle.py            # 📄 Класс, описывающий круг
      ├── oval.py              # 📄 Класс, описывающий овал
      └── factory.py           # 📄 Фабрика созданию фигур  
└── main.py                    # 📄 Точка входа в программу  
```
---

### 🚀 Запуск программы

1. Клонировать репозиторий
2. Собрать Docker образ
3. Запустить контейнер
```bash
docker build -t vector-editor .
docker run -it --name vector-cli vector-editor
```

### 🖥 Демонстрация работы

### Меню
<img src="docs/v2/Menu.jpg" width="600">

### Создание Точки
<img src="docs/v2/Create-Point.jpg" width="600">

### Создание Линии
<img src="docs/v2/Create-Line.jpg" width="600">

### Создание Квадрата
<img src="docs/v2/Create-Square.jpg" width="600">

### Создание Прямоугольника
<img src="docs/v2/Create-Rectangel.jpg" width="600">

### Создание Круга
<img src="docs/v2/Create-Circle.jpg" width="600">

### Создание Овала
<img src="docs/v2/Create-Oval.jpg" width="600">

### Просмотр списка фигур
<img src="docs/v2/Print-Shapes.jpg" width="600">

### Удаление фигуры
<img src="docs/v2/Delete-Shape.jpg" width="600">

### Удаление всех фигур
<img src="docs/v2/Delete-All-Shapes.jpg" width="600">

### Работа с файлом
<img src="docs/v2/File-Menu.jpg" width="600">

### Выбор файла
<img src="docs/v2/Init-File.jpg" width="600">

### Загрузка из файла

<img src="docs/v2/Json-Data.jpg" width="600">

<img src="docs/v2/Load-File.jpg" width="600">

<img src="docs/v2/Load-Data.jpg" width="600">
