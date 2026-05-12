





import java.util.List;
import java.util.ArrayList;

public class Cirurgiao  {

    private String Nome;
    private String Especialidade;
    private int CirurgiaoId;



    public Cirurgiao(
        String Nome,        String Especialidade,        int CirurgiaoId    ) {
        this.Nome = Nome;
        this.Especialidade = Especialidade;
        this.CirurgiaoId = CirurgiaoId;
    }


    public String getNome() {
        return Nome;
    }

    public void setNome(String Nome) {
        this.Nome = Nome;
    }
    public String getEspecialidade() {
        return Especialidade;
    }

    public void setEspecialidade(String Especialidade) {
        this.Especialidade = Especialidade;
    }
    public int getCirurgiaoid() {
        return CirurgiaoId;
    }

    public void setCirurgiaoid(int CirurgiaoId) {
        this.CirurgiaoId = CirurgiaoId;
    }


}