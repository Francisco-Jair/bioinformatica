package transcricao;

import java.awt.EventQueue;
import java.awt.Font;
import java.io.File;

import javax.swing.GroupLayout;
import javax.swing.GroupLayout.Alignment;
import javax.swing.JButton;
import javax.swing.JFileChooser;
import javax.swing.JFrame;
import javax.swing.JTextField;
import javax.swing.LayoutStyle.ComponentPlacement;
import javax.swing.filechooser.FileFilter;
import javax.swing.filechooser.FileNameExtensionFilter;

import java.awt.event.ActionListener;
import java.awt.event.ActionEvent;
import javax.swing.JLabel;
import javax.swing.JProgressBar;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;

public class Tela {

	private JFrame frame;
	private JTextField textField;
	private JTextField textField_1;
	private JTextField textField_2;
	private JTextField textField_3;
	private JButton button_1;
	private String dna;
	private String rna;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					Tela window = new Tela();
					window.frame.setVisible(true);
				} catch (Exception e) {
					e.printStackTrace();
				}
			}
		});
	}

	/**
	 * Create the application.
	 */
	public Tela() {
		initialize();
	}

	/**
	 * Initialize the contents of the frame.
	 */
	private void initialize() {

		// Classes criadas
		LerArquivo ar = new LerArquivo();

		frame = new JFrame();
		frame.setBounds(100, 100, 914, 563);
		frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

		// Instancia do botão inserir e load
		JButton btnNewButton = new JButton("Inserir");
		JButton button = new JButton("Load");

		// Botão Load desativado
		button.setEnabled(false);

		// Botão para abrir o arquivo
		JButton btnAbrirArquivo = new JButton("Abrir Arquivo");
		btnAbrirArquivo.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				JFileChooser open = new JFileChooser();

				// GGC.CGA.TTA.ATG.CTT.AAA.TGC.GGC.CTA.AAT.TAT

				// Para filtrar um tipo de arquivo
				FileNameExtensionFilter filter = new FileNameExtensionFilter("TEXT FILES", "txt", "text");
				open.setFileFilter(filter);
				
				open.setFileSelectionMode(JFileChooser.FILES_ONLY);
				open.showOpenDialog(frame);

				File arquivo = open.getSelectedFile();

				// Pega o caminho do arquivo escolhido
				String path = arquivo.getPath();

				// Vai abrir o arquivo e retornar o que tem dentro dele
				dna = ar.abrirArquivo(path);// Lançar erro caso não encontre o arquivo

				// Mostra no textFild o caminho do arquivo
				textField.setText(path);

				// Desativa o botão Inserir
				btnNewButton.setEnabled(false);
				// Botão Load ativado
				button.setEnabled(true);
				// Desativado o TextField
				textField_1.setEditable(false);

				textField_2.setText(dna);
			}
		});
		btnAbrirArquivo.setFont(new Font("Tahoma", Font.PLAIN, 15));

		textField = new JTextField("\t     Caminho do arquivo");
		// Impende que algo seja digitado no TextField
		textField.setEditable(false);
		textField.setFont(new Font("Tahoma", Font.PLAIN, 20));
		textField.setColumns(10);

		JLabel lblDna = new JLabel("DNA");
		lblDna.setFont(new Font("Tahoma", Font.PLAIN, 20));

		JLabel lblRnam = new JLabel("RNAm");
		lblRnam.setFont(new Font("Tahoma", Font.PLAIN, 20));

		textField_1 = new JTextField("                      Entrar com DNA manualmente");
		textField_1.addMouseListener(new MouseAdapter() {
			// Quando o mouse clica no TextField ele apaga as informações que tem nele
			@Override
			public void mousePressed(MouseEvent e) {
				textField_1.setText("");
			}
		});
		textField_1.setFont(new Font("Tahoma", Font.PLAIN, 20));
		textField_1.setColumns(10);

		// Botão inserir
		btnNewButton.setFont(new Font("Tahoma", Font.PLAIN, 15));
		btnNewButton.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {

				dna = textField_1.getText();

				// Desativar botão que carrega o arquivo
				btnAbrirArquivo.setEnabled(false);
				// Botão Load ativado
				button.setEnabled(true);
				// Desativado o TextField
				textField_1.setEditable(false);

				textField_2.setText(dna);
			}
		});

		// Botão load
		button.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				Transcricao tra = new Transcricao();

				rna = tra.transcricao(dna);
				textField_3.setText(rna);
			}
		});
		button.setFont(new Font("Tahoma", Font.PLAIN, 15));

		textField_2 = new JTextField();
		textField_2.setFont(new Font("Tahoma", Font.PLAIN, 15));
		textField_2.setEditable(false);
		textField_2.setColumns(10);

		textField_3 = new JTextField();
		textField_3.setFont(new Font("Tahoma", Font.PLAIN, 15));
		textField_3.setEditable(false);
		textField_3.setColumns(10);

		button_1 = new JButton("Reiniciar");
		button_1.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {

				// botão load
				button.setEnabled(false);
				btnNewButton.setEnabled(true);
				btnAbrirArquivo.setEnabled(true);

				textField_3.setText("");
				textField_2.setText("");
				textField_1.setEditable(true);
				textField_1.setText("                      Entrar com DNA manualmente");
				textField.setText("\t     Caminho do arquivo");
			}
		});

		GroupLayout groupLayout = new GroupLayout(frame.getContentPane());
		groupLayout.setHorizontalGroup(groupLayout.createParallelGroup(Alignment.LEADING).addGroup(groupLayout
				.createSequentialGroup()
				.addGroup(groupLayout.createParallelGroup(Alignment.LEADING).addGroup(groupLayout
						.createSequentialGroup().addGap(19)
						.addGroup(groupLayout.createParallelGroup(Alignment.TRAILING).addGroup(groupLayout
								.createSequentialGroup()
								.addGroup(groupLayout.createParallelGroup(Alignment.TRAILING)
										.addComponent(btnNewButton, GroupLayout.PREFERRED_SIZE, 126,
												GroupLayout.PREFERRED_SIZE)
										.addComponent(btnAbrirArquivo, GroupLayout.PREFERRED_SIZE, 127,
												GroupLayout.PREFERRED_SIZE))
								.addGap(29))
								.addGroup(groupLayout.createSequentialGroup()
										.addGroup(groupLayout.createParallelGroup(Alignment.LEADING)
												.addComponent(lblRnam, GroupLayout.PREFERRED_SIZE, 71,
														GroupLayout.PREFERRED_SIZE)
												.addComponent(lblDna, GroupLayout.PREFERRED_SIZE, 83,
														GroupLayout.PREFERRED_SIZE))
										.addPreferredGap(ComponentPlacement.UNRELATED)))
						.addGroup(groupLayout.createParallelGroup(Alignment.LEADING, false)
								.addComponent(textField_1, GroupLayout.PREFERRED_SIZE, 535, GroupLayout.PREFERRED_SIZE)
								.addComponent(textField, GroupLayout.PREFERRED_SIZE, 537, GroupLayout.PREFERRED_SIZE)
								.addComponent(textField_2, GroupLayout.DEFAULT_SIZE, 555, Short.MAX_VALUE)
								.addComponent(textField_3)))
						.addGroup(groupLayout.createSequentialGroup().addGap(286).addComponent(button,
								GroupLayout.PREFERRED_SIZE, 245, GroupLayout.PREFERRED_SIZE))
						.addGroup(groupLayout.createSequentialGroup().addGap(305).addComponent(button_1,
								GroupLayout.PREFERRED_SIZE, 259, GroupLayout.PREFERRED_SIZE)))
				.addContainerGap(170, Short.MAX_VALUE)));
		groupLayout.setVerticalGroup(groupLayout.createParallelGroup(Alignment.LEADING).addGroup(groupLayout
				.createSequentialGroup().addGap(36)
				.addGroup(groupLayout.createParallelGroup(Alignment.TRAILING, false)
						.addComponent(btnAbrirArquivo, Alignment.LEADING, GroupLayout.DEFAULT_SIZE,
								GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
						.addComponent(textField, Alignment.LEADING, GroupLayout.DEFAULT_SIZE, 36, Short.MAX_VALUE))
				.addGap(26)
				.addGroup(groupLayout.createParallelGroup(Alignment.BASELINE)
						.addComponent(btnNewButton, GroupLayout.PREFERRED_SIZE, 35, GroupLayout.PREFERRED_SIZE)
						.addComponent(textField_1, GroupLayout.PREFERRED_SIZE, 35, GroupLayout.PREFERRED_SIZE))
				.addGap(29)
				.addGroup(groupLayout.createParallelGroup(Alignment.TRAILING)
						.addGroup(groupLayout.createSequentialGroup()
								.addComponent(button, GroupLayout.PREFERRED_SIZE, 40, GroupLayout.PREFERRED_SIZE)
								.addGap(35)
								.addComponent(textField_2, GroupLayout.PREFERRED_SIZE, 41, GroupLayout.PREFERRED_SIZE))
						.addComponent(lblDna, GroupLayout.PREFERRED_SIZE, 40, GroupLayout.PREFERRED_SIZE))
				.addGap(35)
				.addGroup(groupLayout.createParallelGroup(Alignment.TRAILING).addComponent(lblRnam)
						.addComponent(textField_3, GroupLayout.PREFERRED_SIZE, 40, GroupLayout.PREFERRED_SIZE))
				.addPreferredGap(ComponentPlacement.RELATED, 70, Short.MAX_VALUE)
				.addComponent(button_1, GroupLayout.PREFERRED_SIZE, 60, GroupLayout.PREFERRED_SIZE).addGap(41)));
		frame.getContentPane().setLayout(groupLayout);
	}
}
