package ribomossomo1;

public class CG {

	private String nome;
	private String letra;

	public static CG codons(String seq) {

		CG con = new CG();

		// Transforma a String em um Array de caracter
		char[] valor = seq.toCharArray();

		if (valor.length == 5) {
			con.nome = seq.substring(0, 3);
			con.letra = seq.substring(4, 5);
		} else {
			if (valor.length == 6) {
				con.nome = seq.substring(0, 3);
				con.letra = seq.substring(4, 6);
			}
		}

		return con;
	}

	public String getNome() {
		return nome;
	}

	public void setNome(String nome) {
		this.nome = nome;
	}

	public String getLetra() {
		return letra;
	}

	public void setLetra(String letra) {
		this.letra = letra;
	}
}
