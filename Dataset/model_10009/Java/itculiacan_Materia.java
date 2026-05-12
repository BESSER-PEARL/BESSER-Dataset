





import java.util.List;
import java.util.ArrayList;

public class itculiacan_Materia  {

    private int clave;
    private String nombre;





    private itculiacan_PlanEstudio itculiacan_planestudio;




    private List<itculiacan_Grupo> itculiacan_grupos;




    private List<itculiacan_PlanEstudio> itculiacan_planestudios;




    private itculiacan_Grupo itculiacan_grupo;


    public itculiacan_Materia(
        int clave,        String nombre    ) {
        this.clave = clave;
        this.nombre = nombre;
        this.itculiacan_grupos = new ArrayList<>();
        this.itculiacan_planestudios = new ArrayList<>();
    }

    public itculiacan_Materia(
        int clave,        String nombre        ArrayList<itculiacan_Grupo> itculiacan_grupos,        ArrayList<itculiacan_PlanEstudio> itculiacan_planestudios    ) {
        this.clave = clave;
        this.nombre = nombre;
        this.itculiacan_grupos = itculiacan_grupos;
        this.itculiacan_planestudios = itculiacan_planestudios;
    }

    public int getClave() {
        return clave;
    }

    public void setClave(int clave) {
        this.clave = clave;
    }
    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public itculiacan_PlanEstudio getItculiacan_planestudio() {
        return itculiacan_planestudio;
    }

    public void setItculiacan_planestudio(itculiacan_PlanEstudio itculiacan_planestudio) {
        this.itculiacan_planestudio = itculiacan_planestudio;
    }
    public List<itculiacan_Grupo> getItculiacan_grupos() {
        return itculiacan_grupos;
    }

    public void addItculiacan_grupo(Itculiacan_grupo itculiacan_grupo) {
        this.itculiacan_grupos.add(itculiacan_grupo);
    }
    public List<itculiacan_PlanEstudio> getItculiacan_planestudios() {
        return itculiacan_planestudios;
    }

    public void addItculiacan_planestudio(Itculiacan_planestudio itculiacan_planestudio) {
        this.itculiacan_planestudios.add(itculiacan_planestudio);
    }
    public itculiacan_Grupo getItculiacan_grupo() {
        return itculiacan_grupo;
    }

    public void setItculiacan_grupo(itculiacan_Grupo itculiacan_grupo) {
        this.itculiacan_grupo = itculiacan_grupo;
    }

}