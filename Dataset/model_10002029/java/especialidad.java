





import java.util.List;
import java.util.ArrayList;

public class especialidad  {

    private String nombre;
    private int especialidadID;





    private List<doctor> doctors;


    public especialidad(
        String nombre,        int especialidadID    ) {
        this.nombre = nombre;
        this.especialidadID = especialidadID;
        this.doctors = new ArrayList<>();
    }

    public especialidad(
        String nombre,        int especialidadID        ArrayList<doctor> doctors    ) {
        this.nombre = nombre;
        this.especialidadID = especialidadID;
        this.doctors = doctors;
    }

    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }
    public int getEspecialidadid() {
        return especialidadID;
    }

    public void setEspecialidadid(int especialidadID) {
        this.especialidadID = especialidadID;
    }

    public List<doctor> getDoctors() {
        return doctors;
    }

    public void addDoctor(Doctor doctor) {
        this.doctors.add(doctor);
    }

}