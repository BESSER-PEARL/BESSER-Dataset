





import java.util.List;
import java.util.ArrayList;

public class Especialidade  {

    private String descricao;





    private Medico medico;


    public Especialidade(
        String descricao    ) {
        this.descricao = descricao;
    }


    public String getDescricao() {
        return descricao;
    }

    public void setDescricao(String descricao) {
        this.descricao = descricao;
    }

    public Medico getMedico() {
        return medico;
    }

    public void setMedico(Medico medico) {
        this.medico = medico;
    }

}