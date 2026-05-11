





import java.util.List;
import java.util.ArrayList;

public class gestionmodelosconsultas_resultcotracir_Detallado extends ElementoModeloResultado {

    private String REGISTRO;
    private String REGISTRO_RECAUDO;
    private String NOMBRE;
    private String COSTO_TARIFA;
    private String ID;
    private String TOTAL_RECAUDO_TARIFA;



    public gestionmodelosconsultas_resultcotracir_Detallado(
        String REGISTRO,        String REGISTRO_RECAUDO,        String NOMBRE,        String COSTO_TARIFA,        String ID,        String TOTAL_RECAUDO_TARIFA    ) {
        super(
        );
        this.REGISTRO = REGISTRO;
        this.REGISTRO_RECAUDO = REGISTRO_RECAUDO;
        this.NOMBRE = NOMBRE;
        this.COSTO_TARIFA = COSTO_TARIFA;
        this.ID = ID;
        this.TOTAL_RECAUDO_TARIFA = TOTAL_RECAUDO_TARIFA;
    }


    public String getRegistro() {
        return REGISTRO;
    }

    public void setRegistro(String REGISTRO) {
        this.REGISTRO = REGISTRO;
    }
    public String getRegistro_recaudo() {
        return REGISTRO_RECAUDO;
    }

    public void setRegistro_recaudo(String REGISTRO_RECAUDO) {
        this.REGISTRO_RECAUDO = REGISTRO_RECAUDO;
    }
    public String getNombre() {
        return NOMBRE;
    }

    public void setNombre(String NOMBRE) {
        this.NOMBRE = NOMBRE;
    }
    public String getCosto_tarifa() {
        return COSTO_TARIFA;
    }

    public void setCosto_tarifa(String COSTO_TARIFA) {
        this.COSTO_TARIFA = COSTO_TARIFA;
    }
    public String getId() {
        return ID;
    }

    public void setId(String ID) {
        this.ID = ID;
    }
    public String getTotal_recaudo_tarifa() {
        return TOTAL_RECAUDO_TARIFA;
    }

    public void setTotal_recaudo_tarifa(String TOTAL_RECAUDO_TARIFA) {
        this.TOTAL_RECAUDO_TARIFA = TOTAL_RECAUDO_TARIFA;
    }


}