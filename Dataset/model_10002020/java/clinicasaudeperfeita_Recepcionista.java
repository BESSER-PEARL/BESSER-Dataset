





import java.util.List;
import java.util.ArrayList;

public class clinicasaudeperfeita_Recepcionista  {

    private int idade;
    private String nome;
    private String cpf;





    private List<clinicasaudeperfeita_Consulta> clinicasaudeperfeita_consultas;


    public clinicasaudeperfeita_Recepcionista(
        int idade,        String nome,        String cpf    ) {
        this.idade = idade;
        this.nome = nome;
        this.cpf = cpf;
        this.clinicasaudeperfeita_consultas = new ArrayList<>();
    }

    public clinicasaudeperfeita_Recepcionista(
        int idade,        String nome,        String cpf        ArrayList<clinicasaudeperfeita_Consulta> clinicasaudeperfeita_consultas    ) {
        this.idade = idade;
        this.nome = nome;
        this.cpf = cpf;
        this.clinicasaudeperfeita_consultas = clinicasaudeperfeita_consultas;
    }

    public int getIdade() {
        return idade;
    }

    public void setIdade(int idade) {
        this.idade = idade;
    }
    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }
    public String getCpf() {
        return cpf;
    }

    public void setCpf(String cpf) {
        this.cpf = cpf;
    }

    public List<clinicasaudeperfeita_Consulta> getClinicasaudeperfeita_consultas() {
        return clinicasaudeperfeita_consultas;
    }

    public void addClinicasaudeperfeita_consulta(Clinicasaudeperfeita_consulta clinicasaudeperfeita_consulta) {
        this.clinicasaudeperfeita_consultas.add(clinicasaudeperfeita_consulta);
    }

}