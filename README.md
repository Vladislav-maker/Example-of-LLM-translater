# LLM Переводчик

# LLM Translator API and Interface
**Команда ИТМО | ML 2025**  

## О проекте  
**Задача:** Создать инструмент для перевода текстов с использованием крупных языковых моделей (LLM).

**Решение:** Docker-контейнер с **Streamlit-интерфейсом** и моделью, запускаемой из OpenRouter API.  

**Участники:**  
- [Яна Муллина](https://github.com/yanamull)
- [Дмитрий Кимельфельд](https://github.com/ku9efeld)
- [Елизавета Крылова](https://github.com/ElizavetaWow)
- [Владислав Маринин](https://github.com/Vladislav-maker)

**Демонстрация решения:**
![Demo GIF](./images/*.gif)

 - `/translate` — перевод текста с настраиваемыми параметрами
- `/health` — проверка работоспособности API

## Необходимые условия запуска 

- **Установленные Docker и Docker Compose
- **Действующий API-ключ OpenRouter

## Основные возможности

- **Поддержка 7 языков** (английский, русский, китайский и другие)
- **Интерфейс** с возможностью быстрого переключения языков
- **Мультимодельный подход** (Llama и другие)
- **Контейнеризированное развертывание** через Docker

## Инструкция по развертыванию 

1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/Vladislav-maker/Example-of-LLM-translater.git
   cd llm-translator
   ```
2. Установите зависимости:
    ```bash
    # Установка зависимостей
    pip install -r back/requirements.txt

    # Запуск backend
    python back/api.py

    # Запуск frontend
    streamlit run streamlit.py
    ```

---
