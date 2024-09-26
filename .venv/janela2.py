# Importar os controles (QtWidgets) para a biblioteca gráfica PyQt5.
# Neste exemplo estamos utilizando o comando import com a opção
# asterisco (*) quem importa todos os controles da biblioteca
from PyQt5.QtWidgets import *
# Importação da biblioteca de sistema para abrir e fechar a janela que será construída.
# Ao fechar a janela, também estaremos retirando-a da memória
import sys

# Criação da estrutura geral da nossa janela.
# A janela e seus controles estão sendo criados de forma agrupada dentro de uma classe.
# A classe Janela2 está herdando todas as configurações estruturais de uma tela normal
# classe Qwidget. Esta classe define os botões: minimizar, maximizar e fechar.
# Além de apresentar um título para a janela.
class Janela2(QWidget):
    # O comando def(definition->definição) define uma função. Neste caso, estamos definindo
    # a função de inicialização da classe init(__init__). Esta função realiza o start (coloca para
    # funcionar) a classe Janela2. Na função __init__ passamos como parâmetro o comando self que
    # indica a classe que teremos controles que devem ser usados por ela. Portanto, todo controle
    # que está com o prefixo self, faz referência à própria classe. Ex.: self.label_nome = QLabel :
    # isso indica que a Label pertence à classe Janela2, assim como os demais controles(label, 
    # line edit, setlayout).
    def __init__(self):
        super().__init__()
        # Adicionar um texto do título da janela
        self.setWindowTitle("Janela de cadastro")

        # Configurar tamanho e posição
        # O primeiro valor é a posição x medida em pixel
        # O segundo valor é a posição y medida em pixel
        # O terceiro valor é a largura (width) medida em pixel
        # O quarto valor é a altura (height) medida em pixel
        self.setGeometry(50,200,500,200)

        # Adicionar uma label à janela
        # Uma label (rótulo) é um texto que é apresentado em uma janela para indicar o que deve ser
        # feito à frente (geralmente uma caixa de texto). No exemplo abaixo, estamos criando uma label para
        # apresentar o texto "Nome Completo", isso indica ao usuário que ele deve escrever o nome em uma
        # caixa de texto à frente. Geralmente, uma label é usada em combinação com uma caixa de texto (QLineEdit).
        self.label_nome = QLabel("Nome completo:")

        # Adicionar uma caixa de texto
        self.edit_nome = QLineEdit()

        # Adicionar layout para organizar os elementos
        # Estamos usando o gerenciador de layout vertical (QVBoxLayout)
        # Ele é utilizado para organizar os controles que irão aparecer na Janela2.
        # O QVBoxLayout foi utilizado para dispor os controles um abaixo do outro. Para exibir um ao lado do outro,
        # usamos o comando QHBoxLayout.
        layout = QVBoxLayout()

        # Para adicionar a label_nome e o edit_nome ao organizador (layout) vertical, usamos o comando
        # add (adicionar) Widget(controle). Assim os controles irão aparecer um abaixo do outro, pois este organizador
        # é do tipo vertical.
        layout.addWidget(self.label_nome)
        layout.addWidget(self.edit_nome)

        # Adicionar o layout à tela
        self.setLayout(layout)

app = QApplication(sys.argv)
jan = Janela2()
jan.show()
app.exec_()