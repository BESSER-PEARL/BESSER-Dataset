





import java.util.List;
import java.util.ArrayList;

public class Areas_del_Conocimiento  {

    private String Departamentos;
    private String NombreArea;





    private Pemsum_Universitario pemsum_universitario;




    private List<asignacion_de_creditos> asignacion_de_creditoss;


    public Areas_del_Conocimiento(
        String Departamentos,        String NombreArea    ) {
        this.Departamentos = Departamentos;
        this.NombreArea = NombreArea;
        this.asignacion_de_creditoss = new ArrayList<>();
    }

    public Areas_del_Conocimiento(
        String Departamentos,        String NombreArea        ArrayList<asignacion_de_creditos> asignacion_de_creditoss    ) {
        this.Departamentos = Departamentos;
        this.NombreArea = NombreArea;
        this.asignacion_de_creditoss = asignacion_de_creditoss;
    }

    public String getDepartamentos() {
        return Departamentos;
    }

    public void setDepartamentos(String Departamentos) {
        this.Departamentos = Departamentos;
    }
    public String getNombrearea() {
        return NombreArea;
    }

    public void setNombrearea(String NombreArea) {
        this.NombreArea = NombreArea;
    }

    public Pemsum_Universitario getPemsum_universitario() {
        return pemsum_universitario;
    }

    public void setPemsum_universitario(Pemsum_Universitario pemsum_universitario) {
        this.pemsum_universitario = pemsum_universitario;
    }
    public List<asignacion_de_creditos> getAsignacion_de_creditoss() {
        return asignacion_de_creditoss;
    }

    public void addAsignacion_de_creditos(Asignacion_de_creditos asignacion_de_creditos) {
        this.asignacion_de_creditoss.add(asignacion_de_creditos);
    }

}