





import java.util.List;
import java.util.ArrayList;

public class clinicasaudeperfeita_Paciente  {

    private String nome;
    private String cpf;
    private String cSus;
    private int idade;



    public clinicasaudeperfeita_Paciente(
        String nome,        String cpf,        String cSus,        int idade    ) {
        this.nome = nome;
        this.cpf = cpf;
        this.cSus = cSus;
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
    public String getCsus() {
        return cSus;
    }

    public void setCsus(String cSus) {
        this.cSus = cSus;
    }
    public int getIdade() {
        return idade;
    }

    public void setIdade(int idade) {
        this.idade = idade;
    }


}