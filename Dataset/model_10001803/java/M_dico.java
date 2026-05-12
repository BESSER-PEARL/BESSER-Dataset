





import java.util.List;
import java.util.ArrayList;

public class M_dico  {

    private String Especialidade;
    private int CPF;
    private String Nome;



    public M_dico(
        String Especialidade,        int CPF,        String Nome    ) {
        this.Especialidade = Especialidade;
        this.CPF = CPF;
        this.Nome = Nome;
    }


    public String getEspecialidade() {
        return Especialidade;
    }

    public void setEspecialidade(String Especialidade) {
        this.Especialidade = Especialidade;
    }
    public int getCpf() {
        return CPF;
    }

    public void setCpf(int CPF) {
        this.CPF = CPF;
    }
    public String getNome() {
        return Nome;
    }

    public void setNome(String Nome) {
        this.Nome = Nome;
    }


}