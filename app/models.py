class VaccinationPoint:
    def __init__(self, name, coordinates):
        self.name = name
        self.coordinates = coordinates

    def as_dict(self):
        return {'name': self.name, 'coordinates': self.coordinates}

# Lista de pontos de vacinação
raw_vaccination_points = [
    {"name": "Área interna do Maceió Shopping (Mangabeiras)", "coordinates": [-9.648592111464959, -35.715487245114105]},
    {"name": "II Centro - Unidade de Referência em Saúde Dr. Diógenes Jucá Bernardes, Praça da Maravilha, Poço", "coordinates": [-9.665971372127704, -35.72264367580231]},
    {"name": "Unidade Básica de Saúde Osvaldo Brandão Vilela, Ponta da Terra", "coordinates": [-9.661950483879423, -35.71668852883567]},
    {"name": "Centro de Atendimento ao Turista (CAT) Praia - Ponta Verde", "coordinates": [-9.664167213688364, -35.69856978886799]},
    {"name": "Unidade Básica de Saúde Professor Durval Cortez, Prado", "coordinates": [-9.672637886482983, -35.750611753719774]},
    {"name": "Unidade Básica de Saúde Roland Simon, Vergel do Lago", "coordinates": [-9.65664805652478, -35.75358082023868]},
    {"name": "Unidade de Referência em Saúde Pitanguinha", "coordinates": [-9.637395014649053, -35.732564963595685]},
    {"name": "Unidade Básica de Saúde Dr. Antônio de Pádua, Jardim Petrópolis", "coordinates": [-9.607032881218851, -35.75424309140283]},
    {"name": "Unidade de Saúde da Família João Sampaio, Conjto. João Sampaio", "coordinates": [-9.541645882567572, -35.725789154123014]},
    {"name": "Unidade Básica de Saúde José Guedes de Farias, Santa Amélia", "coordinates": [-9.591251738239055, -35.771865776059435]},
    {"name": "Unidade Básica de Saúde José Tenório, Serraria", "coordinates": [-9.60269343645939, -35.71794379140284]},
    {"name": "Unidade de Referência em Saúde João Paulo II, Jacintinho", "coordinates": [-9.642956627564512, -35.718173996955656]},
    {"name": "Unidade Básica de Saúde Aliomar de Almeida Lins, Benedito Bentes", "coordinates": [-9.563245344548646, -35.72420387605944]},
    {"name": "Unidade Básica de Saúde Arthur Ramos, Conjto. Henrique Equelman", "coordinates": [-9.564393824850148, -35.741496893253775]},
    {"name": "Área interna do Shopping Pátio Maceió (Cidade Universitária)", "coordinates": [-9.558696979876839, -35.74624856261005]},
    {"name": "Unidade de Saúde da Família Tereza Barbosa, Eustáquio Gomes", "coordinates": [-9.539629456258407, -35.78627336256698]},
    {"name": "Unidade de Referência em Saúde Ib Gatto Falcão, Tabuleiro", "coordinates": [-9.592820569500574, -35.767607547223584]},
    {"name": "Unidade Docente Assistencial (UDA) Professor Gilberto de Macedo, Campus da UFAL", "coordinates": [-9.547450134012085, -35.76134690674622]},
    {"name": "Unidade de Referência em Saúde Maria da Conceição Fonseca Paranhos, Jacarecica", "coordinates": [-9.613668133426547, -35.69011073373114]},
]

# Converte os pontos de vacinação brutos para objetos VaccinationPoint
vaccination_points = [VaccinationPoint(point["name"], point["coordinates"]) for point in raw_vaccination_points]
