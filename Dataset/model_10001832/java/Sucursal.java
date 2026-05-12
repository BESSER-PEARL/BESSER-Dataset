





import java.util.List;
import java.util.ArrayList;

public class Sucursal  {

    private int id;
    private String nombre;





    private List<Asesor> asesors;


    public Sucursal(
        int id,        String nombre    ) {
        this.id = id;
        this.nombre = nombre;
        this.asesors = new ArrayList<>();
    }

    public Sucursal(
        int id,        String nombre        ArrayList<Asesor> asesors    ) {
        this.id = id;
        this.nombre = nombre;
        this.asesors = asesors;
    }

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public List<Asesor> getAsesors() {
        return asesors;
    }

    public void addAsesor(Asesor asesor) {
        this.asesors.add(asesor);
    }

}