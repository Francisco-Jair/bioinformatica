package ribomossomo1;

import java.util.ArrayList;
import java.util.Scanner;

public class Principal {

	public static void main(String[] args) {
		Arquivo load = new Arquivo();

		Scanner input = new Scanner(System.in);

		String rnam = null;
		String result = "";

		load.AbrirArquivo("..\\Ribomossomo1\\bibliotecatricas.txt");

		ArrayList<CG> ami = load.getCodons();

		System.out.println("Entra com o RNAm");
		rnam = input.nextLine();

		int i = 0;

		boolean begin = false;

		for (;;) {

			String rnam2 = rnam.substring(i, i + 3);
			// System.out.println(rnam2);
			if (rnam2.equals("AUG")) {
				begin = true;

			}
			if (rnam2.equals("UGA") || rnam2.equals("UAG") || rnam2.equals("UAA")) {
				begin = false;
				break;
			}

			if (begin) {

				for (int ind = 0; ind < ami.size(); ind++) {
					if (ami.get(ind).getNome().equals(rnam2)) {
						result = ami.get(ind).getLetra();
						System.out.println(result);
					}
				}

			}
			i = i + 3;
		}

		// GGCCGAUUAAUGCUUAAAUGCGGCCUAAAUUAUUAG

	}
}
