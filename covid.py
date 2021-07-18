from flask import Flask
import requests
import json

app = Flask('__name__')

@app.route('/')
def home():
    r = requests.get('https://xx9p7hp1p7.execute-api.us-east-1.amazonaws.com/prod/PortalGeralApi')
    r = json.loads(r.text)
    data = r['dt_updated']
    total = r['confirmados']['total']
    novos = r['confirmados']['novos']
    recuperados = r['confirmados']['recuperados']

    return f"<table>" \
                f"<tr>" \
                    f"<td>" \
                        f"Atualização" \
                    f"<td>" \
                    f"<td>" \
                        f"{data}" \
                    f"<td>" \
                f"</tr>" \
                f"<tr>" \
                    f"<td>" \
                        f"Total" \
                    f"<td>" \
                    f"<td>" \
                        f"{total}" \
                    f"<td>" \
                f"</tr>" \
                f"<tr>" \
                    f"<td>" \
                        f"Atualização" \
                    f"<td>" \
                    f"<td>" \
                        f"{novos}" \
                    f"<td>" \
                f"</tr>" \
                f"<tr>" \
                    f"<td>" \
                        f"Recuperados" \
                    f"<td>" \
                    f"<td>" \
                        f"{recuperados}" \
                    f"<td>" \
                f"</tr>" \
            f"</table>" \
            f"{r}"

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000)