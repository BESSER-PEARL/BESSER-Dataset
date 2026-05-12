





import java.util.List;
import java.util.ArrayList;

public class itculiacan_Aula  {

    private int capacidad;
    private int clave;





    private itculiacan_Grupo itculiacan_grupo;




    private List<itculiacan_Grupo> itculiacan_grupos;


    public itculiacan_Aula(
        int capacidad,        int clave    ) {
        this.capacidad = capacidad;
        this.clave = clave;
        this.itculiacan_grupos = new ArrayList<>();
    }

    public itculiacan_Aula(
        int capacidad,        int clave        ArrayList<itculiacan_Grupo> itculiacan_grupos    ) {
        this.capacidad = capacidad;
        this.clave = clave;
        this.itculiacan_grupos = itculiacan_grupos;
    }

    public int getCapacidad() {
        return capacidad;
    }

    public void setCapacidad(int capacidad) {
        this.capacidad = capacidad;
    }
    public int getClave() {
        return clave;
    }

    public void setClave(int clave) {
        this.clave = clave;
    }

    public itculiacan_Grupo getItculiacan_grupo() {
        return itculiacan_grupo;
    }

    public void setItculiacan_grupo(itculiacan_Grupo itculiacan_grupo) {
        this.itculiacan_grupo = itculiacan_grupo;
    }
    public List<itculiacan_Grupo> getItculiacan_grupos() {
        return itculiacan_grupos;
    }

    public void addItculiacan_grupo(Itculiacan_grupo itculiacan_grupo) {
        this.itculiacan_grupos.add(itculiacan_grupo);
    }

}