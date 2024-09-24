import pandas as pd
import random

class Steganography:
    def __init__(self, lexico_path='./data/lexico.csv') -> None:
        """
        Inicializa a classe Steganography com o caminho para o arquivo léxico.

        Args:
            lexico_path (str): Caminho para o arquivo CSV contendo o léxico.
        """
        self.lexico_path = lexico_path
        self.lexico = self._load_lexico()

    def _load_lexico(self) -> dict:
        """
        Carrega os dados do léxico a partir de um arquivo CSV.

        Returns:
            dict: Um dicionário onde as chaves são símbolos em latim e os valores são os símbolos de destino.
        """
        return pd.read_csv(
            self.lexico_path,
            index_col='latim_symbol',
            usecols=['latim_symbol', 'destination_symbol']
        )['destination_symbol'].to_dict()

    def _transliterate_text(self, text: str) -> str:
        """
        Realiza a transliteração do texto usando o léxico.

        Args:
            text (str): O texto a ser transliterado.

        Returns:
            str: O texto transliterado.
        """
        return ''.join(self.lexico.get(char, char) for char in text)

    def _insert_invisible_chars(self, text: str) -> str:
        """
        Insere caracteres invisíveis após cada caractere do texto.

        Args:
            text (str): O texto no qual os caracteres invisíveis serão inseridos.

        Returns:
            str: O texto com caracteres invisíveis inseridos.
        """
        invisible_chars = ['\u200B', '\u200C', '\u200D']
        return ''.join(f"{char}{random.choice(invisible_chars)}" for char in text)

    def encode(self, text: str) -> str:
        """
        Codifica o texto através de transliteração e inserção de caracteres invisíveis.

        Args:
            text (str): O texto a ser codificado.

        Returns:
            str: O texto codificado.
        """
        transliterated_text = self._transliterate_text(text)
        return self._insert_invisible_chars(transliterated_text)
