package smithwaterman;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;

public class Arquivo {

	private String dna1;
	private String dna2;

	public void AbrirArquivo(String path) {
		File arquivo = new File(path);

		try {
			FileReader ler = new FileReader(arquivo);
			BufferedReader leitura = new BufferedReader(ler);
			// arquivo.createNewFile();
			// arquivo.delete();
			// arquivo.mkdir();

			String linha = leitura.readLine();

			int cont = 0;
			while (linha != null) {

				if (cont == 0) {
					dna1 = linha;
				}

				if (cont == 1) {
					dna2 = linha;
				}

				linha = leitura.readLine();
				cont++;
			}

		} catch (Exception e) {
			// TODO: handle exception
		}
	}

	public String getDna1() {
		return dna1;
	}

	public String getDna2() {
		return dna2;
	}
}
