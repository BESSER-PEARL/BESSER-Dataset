





import java.util.List;
import java.util.ArrayList;

public class itculiacan_Profesor  {

    private String nombramiento;
    private String nombre;
    private int numeroMaterias;
    private int clave;





    private List<itculiacan_Grupo> itculiacan_grupos;




    private itculiacan_Grupo itculiacan_grupo;


    public itculiacan_Profesor(
        String nombramiento,        String nombre,        int numeroMaterias,        int clave    ) {
        this.nombramiento = nombramiento;
        this.nombre = nombre;
        this.numeroMaterias = numeroMaterias;
        this.clave = clave;
        this.itculiacan_grupos = new ArrayList<>();
    }

    public itculiacan_Profesor(
        String nombramiento,        String nombre,        int numeroMaterias,        int clave        ArrayList<itculiacan_Grupo> itculiacan_grupos    ) {
        this.nombramiento = nombramiento;
        this.nombre = nombre;
        this.numeroMaterias = numeroMaterias;
        this.clave = clave;
        this.itculiacan_grupos = itculiacan_grupos;
    }

    public String getNombramiento() {
        return nombramiento;
    }

    public void setNombramiento(String nombramiento) {
        this.nombramiento = nombramiento;
    }
    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }
    public int getNumeromaterias() {
        return numeroMaterias;
    }

    public void setNumeromaterias(int numeroMaterias) {
        this.numeroMaterias = numeroMaterias;
    }
    public int getClave() {
        return clave;
    }

    public void setClave(int clave) {
        this.clave = clave;
    }

    public List<itculiacan_Grupo> getItculiacan_grupos() {
        return itculiacan_grupos;
    }

    public void addItculiacan_grupo(Itculiacan_grupo itculiacan_grupo) {
        this.itculiacan_grupos.add(itculiacan_grupo);
    }
    public itculiacan_Grupo getItculiacan_grupo() {
        return itculiacan_grupo;
    }

    public void setItculiacan_grupo(itculiacan_Grupo itculiacan_grupo) {
        this.itculiacan_grupo = itculiacan_grupo;
    }

}