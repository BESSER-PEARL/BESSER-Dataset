





import java.util.List;
import java.util.ArrayList;

public class Profesor  {

    private int ID;
    private String Apellido;
    private String Area;
    private String Nombre;





    private List<Materias> materiass;


    public Profesor(
        int ID,        String Apellido,        String Area,        String Nombre    ) {
        this.ID = ID;
        this.Apellido = Apellido;
        this.Area = Area;
        this.Nombre = Nombre;
        this.materiass = new ArrayList<>();
    }

    public Profesor(
        int ID,        String Apellido,        String Area,        String Nombre        ArrayList<Materias> materiass    ) {
        this.ID = ID;
        this.Apellido = Apellido;
        this.Area = Area;
        this.Nombre = Nombre;
        this.materiass = materiass;
    }

    public int getId() {
        return ID;
    }

    public void setId(int ID) {
        this.ID = ID;
    }
    public String getApellido() {
        return Apellido;
    }

    public void setApellido(String Apellido) {
        this.Apellido = Apellido;
    }
    public String getArea() {
        return Area;
    }

    public void setArea(String Area) {
        this.Area = Area;
    }
    public String getNombre() {
        return Nombre;
    }

    public void setNombre(String Nombre) {
        this.Nombre = Nombre;
    }

    public List<Materias> getMateriass() {
        return materiass;
    }

    public void addMaterias(Materias materias) {
        this.materiass.add(materias);
    }

}