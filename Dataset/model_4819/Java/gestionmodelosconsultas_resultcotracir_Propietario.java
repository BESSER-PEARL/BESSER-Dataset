





import java.util.List;
import java.util.ArrayList;

public class gestionmodelosconsultas_resultcotracir_Propietario extends ElementoModeloResultado {

    private String ID;
    private String CEDULA;
    private String NOMBRE;



    public gestionmodelosconsultas_resultcotracir_Propietario(
        String ID,        String CEDULA,        String NOMBRE    ) {
        super(
        );
        this.ID = ID;
        this.CEDULA = CEDULA;
        this.NOMBRE = NOMBRE;
    }


    public String getId() {
        return ID;
    }

    public void setId(String ID) {
        this.ID = ID;
    }
    public String getCedula() {
        return CEDULA;
    }

    public void setCedula(String CEDULA) {
        this.CEDULA = CEDULA;
    }
    public String getNombre() {
        return NOMBRE;
    }

    public void setNombre(String NOMBRE) {
        this.NOMBRE = NOMBRE;
    }


}