





import java.util.List;
import java.util.ArrayList;

public class Consulta  {

    private String diagnostico;
    private String medicamentos;
    private String codigoDiagnostico;
    private boolean atestado;
    private None triagem;
    private None medico;





    private Medico medico;




    private Triagem triagem;


    public Consulta(
        String diagnostico,        String medicamentos,        String codigoDiagnostico,        boolean atestado,        None triagem,        None medico    ) {
        this.diagnostico = diagnostico;
        this.medicamentos = medicamentos;
        this.codigoDiagnostico = codigoDiagnostico;
        this.atestado = atestado;
        this.triagem = triagem;
        this.medico = medico;
    }


    public String getDiagnostico() {
        return diagnostico;
    }

    public void setDiagnostico(String diagnostico) {
        this.diagnostico = diagnostico;
    }
    public String getMedicamentos() {
        return medicamentos;
    }

    public void setMedicamentos(String medicamentos) {
        this.medicamentos = medicamentos;
    }
    public String getCodigodiagnostico() {
        return codigoDiagnostico;
    }

    public void setCodigodiagnostico(String codigoDiagnostico) {
        this.codigoDiagnostico = codigoDiagnostico;
    }
    public boolean getAtestado() {
        return atestado;
    }

    public void setAtestado(boolean atestado) {
        this.atestado = atestado;
    }
    public None getTriagem() {
        return triagem;
    }

    public void setTriagem(None triagem) {
        this.triagem = triagem;
    }
    public None getMedico() {
        return medico;
    }

    public void setMedico(None medico) {
        this.medico = medico;
    }

    public Medico getMedico() {
        return medico;
    }

    public void setMedico(Medico medico) {
        this.medico = medico;
    }
    public Triagem getTriagem() {
        return triagem;
    }

    public void setTriagem(Triagem triagem) {
        this.triagem = triagem;
    }

}