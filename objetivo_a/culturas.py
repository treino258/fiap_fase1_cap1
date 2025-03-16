import os
import json

cultura_1 = "cana-de-açucar"
cultura_2 = "Milho"

culturas = {'cultura1': [], 'cultura2': []}

class Culturas:

    cultura_1 = []
    cultura_2 = []

    def append_cultura_1(self):
        self.cultura_1.append({
            "Tipo": tipo,
            "Área": area,
        })


    def from_json(self, json):
        self.cultura_1 = json['cultura1']
        self.cultura_2 = json['cultura2']

        with open('data.json') as f:
            data = json.load(f)
            self.from_json(data)