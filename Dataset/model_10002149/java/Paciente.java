





import java.util.List;
import java.util.ArrayList;

public class Paciente  {

    private String id;
    private String numeroSus;
    private None responsavel;



    public Paciente(
        String id,        String numeroSus,        None responsavel    ) {
        this.id = id;
        this.numeroSus = numeroSus;
        this.responsavel = responsavel;
    }


    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getNumerosus() {
        return numeroSus;
    }

    public void setNumerosus(String numeroSus) {
        this.numeroSus = numeroSus;
    }
    public None getResponsavel() {
        return responsavel;
    }

    public void setResponsavel(None responsavel) {
        this.responsavel = responsavel;
    }


}