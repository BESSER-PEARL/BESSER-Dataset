





import java.util.List;
import java.util.ArrayList;

public class Consulta  {

    private String Especialista;
    private String TipoConsulta;
    private String Medico;
    private String Sede;



    public Consulta(
        String Especialista,        String TipoConsulta,        String Medico,        String Sede    ) {
        this.Especialista = Especialista;
        this.TipoConsulta = TipoConsulta;
        this.Medico = Medico;
        this.Sede = Sede;
    }


    public String getEspecialista() {
        return Especialista;
    }

    public void setEspecialista(String Especialista) {
        this.Especialista = Especialista;
    }
    public String getTipoconsulta() {
        return TipoConsulta;
    }

    public void setTipoconsulta(String TipoConsulta) {
        this.TipoConsulta = TipoConsulta;
    }
    public String getMedico() {
        return Medico;
    }

    public void setMedico(String Medico) {
        this.Medico = Medico;
    }
    public String getSede() {
        return Sede;
    }

    public void setSede(String Sede) {
        this.Sede = Sede;
    }


}