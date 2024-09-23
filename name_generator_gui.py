import sys
import random
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QComboBox
from PySide6.QtCore import Qt, QPropertyAnimation
from PySide6.QtGui import QIcon  # Importa QIcon aquí

# Diccionarios de nombres y apellidos por estilo
nombres_por_estilo = {
    "Fantástico": [
        "Aeliana", "Balthazar", "Celestria", "Dorian", "Elowen", "Faelan", "Galadriel", "Hespera",
        "Ithilwen", "Jareth", "Kaelith", "Lirael", "Morrigan", "Nimue", "Orin", "Phaedra", "Quillon",
        "Rhiannon", "Sylas", "Thorne", "Ulric", "Valen", "Wynter", "Xerxes", "Ysolde", "Zephyra",
        "Alaric", "Belladonna", "Calista", "Damon", "Elysia", "Fenris", "Gwendolyn", "Hawke",
        "Isolde", "Jasper", "Kaelin", "Leif", "Mira", "Nerys", "Oberon", "Persephone", "Quinn",
        "Rowan", "Sable", "Tamsin", "Ursula", "Vesper", "Wren", "Xandra", "Yvain", "Zara"
    ],
    "Ciencia Ficción": [
        "Aeron", "Brielle", "Caspian", "Dahlia", "Eowyn", "Feylan", "Galen", "Helena",
        "Iridian", "Jorah", "Kynan", "Lyra", "Malachi", "Nyx", "Orion", "Pyrus", "Quorra",
        "Riven", "Seraphine", "Talon", "Urien", "Valloria", "Wysteria", "Xenith", "Yara",
        "Zariel", "Ashryn", "Cinder", "Dax", "Elira", "Fiora", "Griffin", "Harlow", "Indira",
        "Jareth", "Kiera", "Lysander", "Morrigan", "Niall", "Oriana", "Peregrine", "Quintus",
        "Rune", "Selene", "Thalia", "Umbra", "Violet", "Wilder", "Xeraphina", "Ygraine", "Zayden"
    ],
    "Histórico": [
        "Adelaide", "Alaric", "Anastasia", "Augustus", "Beatrix", "Cassandra", "Charlemagne",
        "Cleopatra", "Constantine", "Darius", "Edmund", "Eleanor", "Eliza", "Emperor",
        "Frederick", "Galileo", "Gideon", "Gustavus", "Heloise", "Henry", "Isabella",
        "Julius", "Juliet", "Katherine", "Leonidas", "Livia", "Margaret", "Marcus", "Maria",
        "Maximilian", "Napoleon", "Nefertiti", "Octavian", "Oriana", "Persephone", "Pharaoh",
        "Reginald", "Roxanne", "Salvador", "Sofía", "Solomon", "Tiberius", "Valeria",
        "Victoria", "William", "Xerxes", "Yvonne", "Zachariah"
    ],
    "Romántico": [
        "Alfred", "Balthazar", "Chloe", "Diana", "Eustace", "Ferdinand", "Hector", "Ingrid",
        "Jasper", "Katherine", "Leopold", "Magnus", "Nadia", "Ophelia", "Ptolemy", "Quintus",
        "Ragnar", "Sigrid", "Tessa", "Ulysses", "Vera", "Wilhelmina", "Zara"
    ],
    "Futurista": [
        "Axel", "Blitz", "Cortex", "Droid", "Eon", "Fable", "Gage", "Helix", "Ionis",
        "Jax", "Kora", "Lynx", "Meteor", "Nyx", "Omni", "Pixel", "Quill", "Raven",
        "Sirius", "Trek", "Ultra", "Vela", "Wiz", "Xander", "Yonder", "Zane"
    ],
    "Oriental": [
        "Takahashi", "Chen", "Wang", "Kim", "Nguyen", "Yamamoto", "Zhang", "Kobayashi",
        "Park", "Li", "Tanaka", "Huang", "Miyamoto", "Liu", "Shimizu", "Sato", "Ito",
        "Yamashita", "Kwon", "Hsieh", "Feng", "Choi", "Huang", "Zhou", "Mao", "Ishikawa",
        "Ng", "Saito", "Yuan", "Yoshida"
    ],
    "Clásico": [
        "Addams", "Barrett", "Carter", "Davenport", "Ellington", "Fitzgerald", "Grayson",
        "Hawthorne", "Ives", "Jenkins", "Kingsley", "Lawrence", "Montgomery", "Newton",
        "Olivier", "Parker", "Quincy", "Reynolds", "Sullivan", "Thompson", "Underwood",
        "Vaughn", "Wellington", "Xavier", "Yates", "Zachary", "Abbot", "Beaumont", "Cunningham",
        "Delaney", "Everett", "Fowler", "Harrington", "Jefferson", "Kendall", "Lockhart",
        "Milford", "Northfield", "O'Sullivan", "Pemberton"
    ]
    # Agrega más estilos según sea necesario
}

apellidos_por_estilo = {
    "Fantástico": [
        "Stormbringer", "Shadowthorn", "Ironfoot", "Moonwhisper", "Fireheart", 
        "Frostwind", "Goldenshadow", "Silverleaf", "Nightbloom", "Starfire"
    ],
    "Ciencia Ficción": [
        "Neutron", "Galactica", "Quantum", "Cyber", "Andromeda",
        "Starlight", "Titan", "Nexus", "Cosmos", "Hyperion"
    ],
    "Histórico": [
        "Zodiac", "Vector", "Sirius", "Krypton", "Omega",
        "Eclipse", "Axion", "Vortex", "Phaser", "Cypher"
    ],
    "Romántico": [
        "Borgia", "Lancaster", "Tudor", "Medici", "Habsburg"
    ],
    "Futurista": [
        "Ptolemy", "Carnegie", "Wellington", "Stewart", "Almeida"
    ],
    "Oriental": [
        "Barclay", "Montague", "Davenport", "Windsor", "Fitzgerald"
    ],
    "Clásico": [
        "Cortez", "Devereux", "Plantagenet", "Capulet", "Gonzalez"
    ]
    # Agrega más estilos según sea necesario
}

estilos = list(nombres_por_estilo.keys())

# Clase principal de la interfaz
class NameGenerator(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Generador de Nombres")
        self.setFixedSize(800, 500)  # Tamaño de la ventana

        # Establecer el icono de la ventana
        self.setWindowIcon(QIcon("C:\\Users\\usuario\\Downloads\\sprite_0001_6Ak_icon.ico"))  # Aquí colocas la ruta de tu icono

        self.setStyleSheet("""\
            background-color: #1A3636; 
            color: #D6BD98; 
            font-family: 'Press Start 2P'; 
            font-size: 18px;
        """)

        # Layout principal
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignCenter)

        # Título
        title = QLabel("Creador de identidades")
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("font-size: 24px; font-weight: bold; margin-bottom: 20px;")
        layout.addWidget(title)

        # ComboBox para seleccionar el estilo
        self.comboBox = QComboBox()
        self.comboBox.setStyleSheet("background-color: #40534C; color: #D6BD98; padding: 5px; border-radius: 5px;")
        for estilo in estilos:
            self.comboBox.addItem(estilo)
        layout.addWidget(self.comboBox)

        # Botón para generar nombres
        self.button = QPushButton("Generar Nombre")
        self.button.setStyleSheet("""\
            background-color: #677D6A; 
            border-radius: 10px; 
            padding: 10px; 
            font-weight: bold;
        """)
        self.button.clicked.connect(self.generate_name)
        layout.addWidget(self.button)

        # Botón para limpiar el nombre
        self.clear_button = QPushButton("Limpiar Nombre")
        self.clear_button.setStyleSheet("""\
            background-color: #B66A6A; 
            border-radius: 10px; 
            padding: 10px; 
            font-weight: bold;
        """)
        self.clear_button.clicked.connect(self.clear_name)
        layout.addWidget(self.clear_button)

        # Etiqueta para mostrar el nombre generado
        self.name_label = QLabel("Nombre Generado")
        self.name_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.name_label)

        # Aplicar el layout a la ventana
        self.setLayout(layout)

    def generate_name(self):
        estilo = self.comboBox.currentText()
        nombre = random.choice(nombres_por_estilo[estilo])
        apellido = random.choice(apellidos_por_estilo[estilo])
        self.name_label.setText(f"{nombre} {apellido}")

    def clear_name(self):
        self.name_label.setText("Nombre Generado")


# Inicializar la aplicación
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = NameGenerator()
    window.show()
    sys.exit(app.exec())