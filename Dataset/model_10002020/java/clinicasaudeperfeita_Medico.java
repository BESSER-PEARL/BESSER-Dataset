





import java.util.List;
import java.util.ArrayList;

public class clinicasaudeperfeita_Medico  {

    private None agenda;
    private int idade;
    private String nome;
    private String cpf;





    private List<clinicasaudeperfeita_Consulta> clinicasaudeperfeita_consultas;




    private List<clinicasaudeperfeita_Compromisso> clinicasaudeperfeita_compromissos;


    public clinicasaudeperfeita_Medico(
        None agenda,        int idade,        String nome,        String cpf    ) {
        this.agenda = agenda;
        this.idade = idade;
        this.nome = nome;
        this.cpf = cpf;
        this.clinicasaudeperfeita_consultas = new ArrayList<>();
        this.clinicasaudeperfeita_compromissos = new ArrayList<>();
    }

    public clinicasaudeperfeita_Medico(
        None agenda,        int idade,        String nome,        String cpf        ArrayList<clinicasaudeperfeita_Consulta> clinicasaudeperfeita_consultas,        ArrayList<clinicasaudeperfeita_Compromisso> clinicasaudeperfeita_compromissos    ) {
        this.agenda = agenda;
        this.idade = idade;
        this.nome = nome;
        this.cpf = cpf;
        this.clinicasaudeperfeita_consultas = clinicasaudeperfeita_consultas;
        this.clinicasaudeperfeita_compromissos = clinicasaudeperfeita_compromissos;
    }

    public None getAgenda() {
        return agenda;
    }

    public void setAgenda(None agenda) {
        this.agenda = agenda;
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
    public List<clinicasaudeperfeita_Compromisso> getClinicasaudeperfeita_compromissos() {
        return clinicasaudeperfeita_compromissos;
    }

    public void addClinicasaudeperfeita_compromisso(Clinicasaudeperfeita_compromisso clinicasaudeperfeita_compromisso) {
        this.clinicasaudeperfeita_compromissos.add(clinicasaudeperfeita_compromisso);
    }

}