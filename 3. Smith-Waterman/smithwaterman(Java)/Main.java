package smithwaterman;

import java.util.Scanner;

public class Main {

	public static void main(String[] args) {

		Scanner input = new Scanner(System.in);

		Arquivo arq = new Arquivo();
		String path;
		int gap, mis, ma;

		System.out.println("Entre com o valor do GAP, MATCH, MISMATCH");
		gap = input.nextInt();
		ma = input.nextInt();
		mis = input.nextInt();
		System.out.println("Entre com o caminho do arquivo");
		path = input.next();
		input.nextLine();

		arq.AbrirArquivo(path);

		Matriz mat = new Matriz(arq.getDna1(), arq.getDna2(), gap, mis, ma);

		mat.mostrarMatriz();
	}
}
