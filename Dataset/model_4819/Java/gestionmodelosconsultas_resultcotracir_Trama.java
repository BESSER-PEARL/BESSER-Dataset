





import java.util.List;
import java.util.ArrayList;

public class gestionmodelosconsultas_resultcotracir_Trama extends ElementoModeloResultado {

    private String ID;
    private String CADENA_TRAMA;



    public gestionmodelosconsultas_resultcotracir_Trama(
        String ID,        String CADENA_TRAMA    ) {
        super(
        );
        this.ID = ID;
        this.CADENA_TRAMA = CADENA_TRAMA;
    }


    public String getId() {
        return ID;
    }

    public void setId(String ID) {
        this.ID = ID;
    }
    public String getCadena_trama() {
        return CADENA_TRAMA;
    }

    public void setCadena_trama(String CADENA_TRAMA) {
        this.CADENA_TRAMA = CADENA_TRAMA;
    }


}