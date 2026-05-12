





import java.util.List;
import java.util.ArrayList;

public class Exame  {

    private String Especialista;
    private String Medico;
    private String TipoExame;
    private String Sede;



    public Exame(
        String Especialista,        String Medico,        String TipoExame,        String Sede    ) {
        this.Especialista = Especialista;
        this.Medico = Medico;
        this.TipoExame = TipoExame;
        this.Sede = Sede;
    }


    public String getEspecialista() {
        return Especialista;
    }

    public void setEspecialista(String Especialista) {
        this.Especialista = Especialista;
    }
    public String getMedico() {
        return Medico;
    }

    public void setMedico(String Medico) {
        this.Medico = Medico;
    }
    public String getTipoexame() {
        return TipoExame;
    }

    public void setTipoexame(String TipoExame) {
        this.TipoExame = TipoExame;
    }
    public String getSede() {
        return Sede;
    }

    public void setSede(String Sede) {
        this.Sede = Sede;
    }


}