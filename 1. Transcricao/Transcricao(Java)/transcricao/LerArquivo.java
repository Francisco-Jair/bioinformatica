package transcricao;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;

public class LerArquivo {

	public String abrirArquivo(String loc) {

		File Arquivo = new File(loc);
		String linha = null;

		if (Arquivo.exists()) {
			try {
				FileReader Leitor = new FileReader(loc);
				BufferedReader buffer = new BufferedReader(Leitor);

				// Vai ser verdade ate o fim do arquivo onde vai quebrar o lanço

				while (true) {

					String linha1 = buffer.readLine();

					if (linha1 == null) {
						break;
					}

					linha = linha1;
				}

			} catch (Exception e) {
				System.out.println(e.getMessage());
			} finally {

			}

		} else {
			// Colocar como uma janela
			System.out.println("Arquivo não encontrado.....");
		}

		return linha;
	}

}
