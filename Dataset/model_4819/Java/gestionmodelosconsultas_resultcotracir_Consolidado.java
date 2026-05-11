





import java.util.List;
import java.util.ArrayList;

public class gestionmodelosconsultas_resultcotracir_Consolidado extends ElementoModeloResultado {

    private String TOTAL_RECAUDO_BRUTO;
    private String RUTA_DESPACHO;
    private String ESTADO_CONSOLIDADO;
    private String ID;
    private String ESTADO_IMPRESION;
    private String TOTAL_RECAUDO_DESPACHO;
    private String HORA_DESPACHO;
    private String REGISTRO_CONSOLIDADO;



    public gestionmodelosconsultas_resultcotracir_Consolidado(
        String TOTAL_RECAUDO_BRUTO,        String RUTA_DESPACHO,        String ESTADO_CONSOLIDADO,        String ID,        String ESTADO_IMPRESION,        String TOTAL_RECAUDO_DESPACHO,        String HORA_DESPACHO,        String REGISTRO_CONSOLIDADO    ) {
        super(
        );
        this.TOTAL_RECAUDO_BRUTO = TOTAL_RECAUDO_BRUTO;
        this.RUTA_DESPACHO = RUTA_DESPACHO;
        this.ESTADO_CONSOLIDADO = ESTADO_CONSOLIDADO;
        this.ID = ID;
        this.ESTADO_IMPRESION = ESTADO_IMPRESION;
        this.TOTAL_RECAUDO_DESPACHO = TOTAL_RECAUDO_DESPACHO;
        this.HORA_DESPACHO = HORA_DESPACHO;
        this.REGISTRO_CONSOLIDADO = REGISTRO_CONSOLIDADO;
    }


    public String getTotal_recaudo_bruto() {
        return TOTAL_RECAUDO_BRUTO;
    }

    public void setTotal_recaudo_bruto(String TOTAL_RECAUDO_BRUTO) {
        this.TOTAL_RECAUDO_BRUTO = TOTAL_RECAUDO_BRUTO;
    }
    public String getRuta_despacho() {
        return RUTA_DESPACHO;
    }

    public void setRuta_despacho(String RUTA_DESPACHO) {
        this.RUTA_DESPACHO = RUTA_DESPACHO;
    }
    public String getEstado_consolidado() {
        return ESTADO_CONSOLIDADO;
    }

    public void setEstado_consolidado(String ESTADO_CONSOLIDADO) {
        this.ESTADO_CONSOLIDADO = ESTADO_CONSOLIDADO;
    }
    public String getId() {
        return ID;
    }

    public void setId(String ID) {
        this.ID = ID;
    }
    public String getEstado_impresion() {
        return ESTADO_IMPRESION;
    }

    public void setEstado_impresion(String ESTADO_IMPRESION) {
        this.ESTADO_IMPRESION = ESTADO_IMPRESION;
    }
    public String getTotal_recaudo_despacho() {
        return TOTAL_RECAUDO_DESPACHO;
    }

    public void setTotal_recaudo_despacho(String TOTAL_RECAUDO_DESPACHO) {
        this.TOTAL_RECAUDO_DESPACHO = TOTAL_RECAUDO_DESPACHO;
    }
    public String getHora_despacho() {
        return HORA_DESPACHO;
    }

    public void setHora_despacho(String HORA_DESPACHO) {
        this.HORA_DESPACHO = HORA_DESPACHO;
    }
    public String getRegistro_consolidado() {
        return REGISTRO_CONSOLIDADO;
    }

    public void setRegistro_consolidado(String REGISTRO_CONSOLIDADO) {
        this.REGISTRO_CONSOLIDADO = REGISTRO_CONSOLIDADO;
    }


}