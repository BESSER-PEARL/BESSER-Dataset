





import java.util.List;
import java.util.ArrayList;

public class tipoSeguro  {

    private int tipoSeguraID;
    private String descripcion;





    private List<aseguradora> aseguradoras;


    public tipoSeguro(
        int tipoSeguraID,        String descripcion    ) {
        this.tipoSeguraID = tipoSeguraID;
        this.descripcion = descripcion;
        this.aseguradoras = new ArrayList<>();
    }

    public tipoSeguro(
        int tipoSeguraID,        String descripcion        ArrayList<aseguradora> aseguradoras    ) {
        this.tipoSeguraID = tipoSeguraID;
        this.descripcion = descripcion;
        this.aseguradoras = aseguradoras;
    }

    public int getTiposeguraid() {
        return tipoSeguraID;
    }

    public void setTiposeguraid(int tipoSeguraID) {
        this.tipoSeguraID = tipoSeguraID;
    }
    public String getDescripcion() {
        return descripcion;
    }

    public void setDescripcion(String descripcion) {
        this.descripcion = descripcion;
    }

    public List<aseguradora> getAseguradoras() {
        return aseguradoras;
    }

    public void addAseguradora(Aseguradora aseguradora) {
        this.aseguradoras.add(aseguradora);
    }

}