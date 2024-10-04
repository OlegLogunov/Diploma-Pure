import requests
import json


async def image_proc(cont):
    #
    #

    url = "https://ngw.devices.sberbank.ru:9443/api/v2/oauth"

    payload = 'scope=GIGACHAT_API_PERS'
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept': 'application/json',
        'RqUID': 'b4c4e431-d4ef-475e-9b0f-e5cde0318d40',
        'Authorization': 'Basic Y2Q2ZDg1YjAtOTc2Yi00Y2RjLTgzNjAtNWJjOWNjMjE1ZjY1OmI0YzRlNDMxLWQ0ZWYtNDc1ZS05YjBmLWU1Y2RlMDMxOGQ0MA=='
    }

    response = requests.request("POST", url, headers=headers, data=payload, verify=False, cert=None)

    # print(response.text)

    # Преобразуем текст ответа в JSON
    response_json = json.loads(response.text)

    # Извлекаем значение access_token
    ac_tok = response_json.get("access_token")

    # Выводим значение
    # print(ac_tok)
    #
    #

    url = "https://gigachat.devices.sberbank.ru/api/v1/chat/completions"

    payload = json.dumps({
        "model": "GigaChat",
        "messages": [
            {
                "role": "user",
                "content": f"Опиши {cont} с учетом его замечательных потребительских свойств, доступной цены, современного стильного дизайна. Описание для размещения в карточке товара интернет-магазина"
            }
        ],
        "stream": False,
        "repetition_penalty": 1
    })
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'Authorization': f'Bearer {ac_tok}'
    }

    response = requests.request("POST", url, headers=headers, data=payload, verify=False, cert=None)

    # print(response.text)

    # Преобразуем текст в JSON
    response_json = json.loads(response.text)

    # Извлекаем значение content
    content = response_json["choices"][0]["message"]["content"]

    # Выводим значение
    # print(content)

    return content
