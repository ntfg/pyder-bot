Pyder

Для установки бота на своём компьютере (debian)
Для прочих систем различия лишь в последних двух строках, их суть лишь в установке Redis
```
git clone https://github.com/ntfg/pyder-bot
cd pyder-bot
python -m venv env
pip install -r requirements.txt

sudo apt update
sudo apt install redis
```

После выполнения вышеперечисленных команд нужно лишь вставить токен бота в .env файл

Для запуска
```
python main.py
```
