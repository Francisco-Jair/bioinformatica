package transcricao;

public class Transcricao {

	public String transcricao(String dna) {

		char[] rna = dna.toCharArray();

		for (int i = 0; i < rna.length; i++) {
			if (rna[i] == 'T') {
				rna[i] = 'U';
			}
		}

		String rnam = String.valueOf(rna);

		return rnam;
	}
}
