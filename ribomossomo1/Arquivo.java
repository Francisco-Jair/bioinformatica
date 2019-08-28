package ribomossomo1;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.File;
import java.io.FileReader;
import java.io.FileWriter;
import java.util.ArrayList;

public class Arquivo {

	private ArrayList<CG> codons = new ArrayList<CG>();

	public ArrayList<CG> getCodons() {
		return codons;
	}

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
		
		CG valor = null;
		try {
			FileReader ler = new FileReader(arquivo);
			BufferedReader leitura = new BufferedReader(ler);
			// arquivo.createNewFile();
			// arquivo.delete();
			// arquivo.mkdir();

			String linha = leitura.readLine();
			while (linha != null) {
				valor = CG.codons(linha);
				codons.add(valor);
				linha = leitura.readLine();
			}

		} catch (Exception e) {
			// TODO: handle exception
		}
	}
}
