





import java.util.List;
import java.util.ArrayList;

public class Medico  {

    private String crm;
    private String setor;
    private String especialidade;



    public Medico(
        String crm,        String setor,        String especialidade    ) {
        this.crm = crm;
        this.setor = setor;
        this.especialidade = especialidade;
    }


    public String getCrm() {
        return crm;
    }

    public void setCrm(String crm) {
        this.crm = crm;
    }
    public String getSetor() {
        return setor;
    }

    public void setSetor(String setor) {
        this.setor = setor;
    }
    public String getEspecialidade() {
        return especialidade;
    }

    public void setEspecialidade(String especialidade) {
        this.especialidade = especialidade;
    }


}