# Тестовая работа для Forkiteh

python version: 3.12.10

Для запуска
```bash

pip install -r requirements.txt

python create_database.py

uvicorn main:app

```

Для тестирования
```bash
pytest
```


### post /get_wallet_info

data: {address: str}

returned: { address: str, balance: float, bandwidth: int, energy: int}

### get /get_data

returned: [{ id: str, address: str, ip_address: str, port: int}]

### Warning:

Введите api_key в config.js, так как без него на запросы накладываются серьёзные ограничения, что мешает работе api.

