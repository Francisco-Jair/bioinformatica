package smithwaterman;

public class Matriz {

	private int i;
	private int j;
	private int gap;
	private int mis;
	private int ma;
	private String dn1;
	private String dn2;
	private int score;

	private Object[][] matriz;
	private NO matrizTrace[][];

	public Matriz(String dna1, String dna2, int gap, int mis, int ma) {
		this.dn1 = dna1.toUpperCase();
		this.dn2 = dna2.toUpperCase();

		// valores para o tamanho da matriz
		this.i = dna1.length() + 2;// Linha
		this.j = dna2.length() + 2;// Coluna

		// Valores do GAP, MISMATCH, MATCH
		this.mis = mis;
		this.gap = gap;
		this.ma = ma;

		this.matriz = new Object[i][j];
		this.matrizTrace = new NO[i][j];
	}

	private void montarMatriz() {

		char[] array1 = dn1.toCharArray();
		char[] array2 = dn2.toCharArray();

		matriz[0][0] = 0;
		matriz[1][1] = 0;
		matriz[0][1] = 'U';
		matriz[1][0] = 'U';

		NO n1 = new NO();
		Data d1 = new Data();
		d1.setValor(0);
		d1.setI(1);
		d1.setJ(1);
		n1.setDiagonal(d1);
		n1.setLado(d1);
		n1.setSuperior(d1);
		matrizTrace[1][1] = n1;

		// Matriz do BackTrace

		int aux3 = gap;
		int aux4 = gap;

		for (int aux = 2; aux < i; aux++) {
			matriz[aux][0] = array1[aux - 2];
			matriz[aux][1] = aux3;

			NO nAUX = new NO();
			Data dAu = new Data();
			dAu.setValor(aux3);
			dAu.setI(aux);
			dAu.setJ(1);

			nAUX.setLado(dAu);

			matrizTrace[aux][1] = nAUX;

			aux3 = aux3 + gap;
			for (int aux2 = 2; aux2 < j; aux2++) {
				matriz[0][aux2] = array2[aux2 - 2];
			}
		}

		for (int aux2 = 2; aux2 < j; aux2++) {
			matriz[1][aux2] = aux4;

			NO nAUX = new NO();
			Data dAu = new Data();
			dAu.setValor(aux4);
			dAu.setI(1);
			dAu.setJ(aux2);

			nAUX.setLado(dAu);
			nAUX.setDiagonal(dAu);
			nAUX.setSuperior(dAu);

			matrizTrace[1][aux2] = nAUX;

			aux4 = aux4 + gap;
		}

		for (int aux = 0; aux < i; aux++) {
			for (int aux2 = 0; aux2 < j; aux2++) {
				if (matriz[aux][aux2] == null) {

					int valor = verificarOque(aux, aux2);

					matriz[aux][aux2] = ver(valor, aux, aux2);

					// BackTrace
					matrizTrace[aux][aux2] = montar(aux, aux2, valor);
				}
			}
		}
	}

	private int ver(int valor, int aux, int aux2) {

		int superior;
		int lado;
		int diagonal;

		superior = gap + Integer.parseInt(matriz[aux - 1][aux2].toString());

		lado = gap + Integer.parseInt(matriz[aux][aux2 - 1].toString());

		diagonal = valor + Integer.parseInt(matriz[aux - 1][aux2 - 1].toString());

		return maior(superior, lado, diagonal);
	}

	private NO montar(int aux, int aux2, int valor) {

		NO no = new NO();
		Data d = new Data();

		int superior = gap + Integer.parseInt(matriz[aux - 1][aux2].toString());

		int lado = gap + Integer.parseInt(matriz[aux][aux2 - 1].toString());

		int diagonal = valor + Integer.parseInt(matriz[aux - 1][aux2 - 1].toString());

		int m = maior(superior, lado, diagonal);

		if (superior == m) {

			d.setValor(m);
			d.setI(aux - 1);
			d.setJ(aux2);

			no.setSuperior(d);
		}

		if (lado == m) {
			d.setValor(m);
			d.setI(aux);
			d.setJ(aux2 - 1);

			no.setLado(d);
		}

		if (diagonal == m) {
			d.setValor(m);
			d.setI(aux - 1);
			d.setJ(aux2 - 1);

			no.setDiagonal(d);
		}

		return no;
	}

	private int maior(int valor, int valor2, int valor3) {
		int[] ma = new int[3];
		ma[0] = valor;
		ma[1] = valor2;
		ma[2] = valor3;

		int temp = -100000000;
		for (int a = 0; a < 3; a++) {
			for (int b = a + 1; b < 3; b++) {

				if (ma[a] < ma[b]) {
					temp = ma[a];
					ma[a] = ma[b];
					ma[b] = temp;
				}
			}
		}

		return ma[0];
	}

	private int verificarOque(int aux, int aux2) {

		if (matriz[aux - aux][aux2] == matriz[aux][aux2 - aux2]) {
			return ma;
		} else {
			return mis;
		}
	}

	private int maiorString() {

		if (dn1.length() > dn2.length()) {
			return dn1.length();
		} else {
			return dn2.length();
		}
	}

	public void traceback() {

		int maior = -99999999, poI = 0, poJ = 0;
		// Encotra o maior elemento da matriz e sua posição
		for (int aux = 2; aux < i; aux++) {
			for (int aux2 = 2; aux2 < j; aux2++) {
				if ((Integer) (matriz[aux][aux2]) >= maior) {
					poI = aux;
					poJ = aux2;
					maior = (Integer) (matriz[aux][aux2]);
				}
			}
		}

		int cont = 0, auxF = 0, pj = 0;
		int CONS = maiorString();
		char mat[][] = new char[2][CONS];
		while (cont < CONS) {
			NO n = matrizTrace[poI][poJ];

			if (n.getDiagonal() != null) {

				mat[0][pj] = (char) matriz[poI - poI][poJ];
				mat[1][pj] = (char) matriz[poI][poJ - poJ];

				poI = n.getDiagonal().getI();
				poJ = n.getDiagonal().getJ();
				auxF++;
			}

			if (n.getLado() != null) {
				mat[0][pj] = (char) matriz[poI - poI][poJ];
				mat[1][pj] = (char) matriz[poI][poJ - poJ];
				poI = n.getLado().getI();
				poJ = n.getLado().getJ();
				auxF++;
			}

			if (n.getSuperior() != null) {
				mat[0][pj] = (char) matriz[poI - poI][poJ];
				mat[1][pj] = (char) matriz[poI][poJ - poJ];
				poI = n.getSuperior().getI();
				poJ = n.getSuperior().getJ();
				auxF++;
			}

			if (auxF == CONS) {
				break;
			}
			pj++;
			cont++;
		}

		int gapCont = 0, misCont = 0, maCont = 0;

		for (int au1 = 1; au1 >= 0; au1--) {
			for (int au2 = CONS - 1; au2 >= 0; au2--) {
				if (mat[au1][au2] == 'U') {
					System.out.print('-');
				} else {
					System.out.print(mat[au1][au2]);
				}
			}
			System.out.println();
		}

		for (int au1 = 0; au1 < CONS; au1++) {

			if (mat[0][au1] == mat[1][au1] && (mat[0][au1] != 'U') && (mat[1][au1] != 'U')) {
				maCont++;
			} else {
				if (mat[0][au1] != mat[1][au1] && (mat[0][au1] != 'U') && (mat[1][au1] != 'U')) {
					misCont++;
				} else {
					if ((mat[0][au1] == 'U') || (mat[1][au1] == 'U')) {
						gapCont++;
					}
				}
			}
		}
		score = (gap * gapCont) + (mis * misCont) + (ma * maCont);
		System.out.println("Score: " + score);
	}

	public void mostrarMatriz() {

		montarMatriz();

		for (int aux = 0; aux < i; aux++) {
			for (int aux2 = 0; aux2 < j; aux2++) {
				System.out.print(matriz[aux][aux2] + "  ");
			}
			System.out.println();
		}
		System.out.println("-----------------------------------");
		traceback();

	}

}
