





import java.util.List;
import java.util.ArrayList;

public class historico  {

    private String sintoma;
    private String diagnostico;
    private int historicoID;
    private String observacion;
    private String tratamiento;
    private int consultaID;





    private consulta consulta;


    public historico(
        String sintoma,        String diagnostico,        int historicoID,        String observacion,        String tratamiento,        int consultaID    ) {
        this.sintoma = sintoma;
        this.diagnostico = diagnostico;
        this.historicoID = historicoID;
        this.observacion = observacion;
        this.tratamiento = tratamiento;
        this.consultaID = consultaID;
    }


    public String getSintoma() {
        return sintoma;
    }

    public void setSintoma(String sintoma) {
        this.sintoma = sintoma;
    }
    public String getDiagnostico() {
        return diagnostico;
    }

    public void setDiagnostico(String diagnostico) {
        this.diagnostico = diagnostico;
    }
    public int getHistoricoid() {
        return historicoID;
    }

    public void setHistoricoid(int historicoID) {
        this.historicoID = historicoID;
    }
    public String getObservacion() {
        return observacion;
    }

    public void setObservacion(String observacion) {
        this.observacion = observacion;
    }
    public String getTratamiento() {
        return tratamiento;
    }

    public void setTratamiento(String tratamiento) {
        this.tratamiento = tratamiento;
    }
    public int getConsultaid() {
        return consultaID;
    }

    public void setConsultaid(int consultaID) {
        this.consultaID = consultaID;
    }

    public consulta getConsulta() {
        return consulta;
    }

    public void setConsulta(consulta consulta) {
        this.consulta = consulta;
    }

}