





import java.util.List;
import java.util.ArrayList;

public class Alimento  {

    private String alimento_Id;
    private boolean refrigeraci_n;
    private String nombre;
    private String precio;





    private List<Orden> ordens;


    public Alimento(
        String alimento_Id,        boolean refrigeraci_n,        String nombre,        String precio    ) {
        this.alimento_Id = alimento_Id;
        this.refrigeraci_n = refrigeraci_n;
        this.nombre = nombre;
        this.precio = precio;
        this.ordens = new ArrayList<>();
    }

    public Alimento(
        String alimento_Id,        boolean refrigeraci_n,        String nombre,        String precio        ArrayList<Orden> ordens    ) {
        this.alimento_Id = alimento_Id;
        this.refrigeraci_n = refrigeraci_n;
        this.nombre = nombre;
        this.precio = precio;
        this.ordens = ordens;
    }

    public String getAlimento_id() {
        return alimento_Id;
    }

    public void setAlimento_id(String alimento_Id) {
        this.alimento_Id = alimento_Id;
    }
    public boolean getRefrigeraci_n() {
        return refrigeraci_n;
    }

    public void setRefrigeraci_n(boolean refrigeraci_n) {
        this.refrigeraci_n = refrigeraci_n;
    }
    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }
    public String getPrecio() {
        return precio;
    }

    public void setPrecio(String precio) {
        this.precio = precio;
    }

    public List<Orden> getOrdens() {
        return ordens;
    }

    public void addOrden(Orden orden) {
        this.ordens.add(orden);
    }

}