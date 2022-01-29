package transcricao;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.File;
import java.io.FileReader;
import java.io.FileWriter;

public class Arquivo {

	public void criarArquivo() {
		File arquivo = new File("RNA.txt");

		try {
			arquivo.createNewFile();
			// arquivo.delete();
			// arquivo.mkdir();
		} catch (Exception e) {
			// TODO: handle exception
		}
	}

	public void escreverArquivo(String path, String conteudo) {
		File arquivo = new File(path);

		try {
			FileWriter escrever = new FileWriter(arquivo);
			BufferedWriter linha = new BufferedWriter(escrever);
			
			linha.write(conteudo);

			linha.close();
			escrever.close();

		} catch (Exception e) {
			// TODO: handle exception
		}
	}

	public void AbrirArquivo(String path) {
		File arquivo = new File(path);

		try {
			FileReader ler = new FileReader(arquivo);
			BufferedReader leitura = new BufferedReader(ler);
			// arquivo.createNewFile();
			// arquivo.delete();
			// arquivo.mkdir();

			String linha = leitura.readLine();

			while (linha != null) {
				linha = leitura.readLine();
			}

		} catch (Exception e) {
			// TODO: handle exception
		}
	}
}
