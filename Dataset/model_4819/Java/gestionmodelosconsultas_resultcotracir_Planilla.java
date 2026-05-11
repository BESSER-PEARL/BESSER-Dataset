





import java.util.List;
import java.util.ArrayList;

public class gestionmodelosconsultas_resultcotracir_Planilla extends ElementoModeloResultado {

    private String TOTAL_RECAUDO_BRUTO;
    private String ID;
    private String TOTAL_GASTOS;
    private String TOTAL_DEPOSITO;
    private String NUMERO_MOVIL;
    private String LIQUIDADO;
    private String CEDULA_CONDUCTOR;
    private String CONDUCTOR;
    private String USUARIO;
    private String TOTAL;
    private String HORA_MODIFICACION;
    private String APELLIDO;
    private String CEDULA;
    private String TOTAL_RECAUDO_NETO;
    private String NOMBRE_PERSONA;
    private String FECHA;



    public gestionmodelosconsultas_resultcotracir_Planilla(
        String TOTAL_RECAUDO_BRUTO,        String ID,        String TOTAL_GASTOS,        String TOTAL_DEPOSITO,        String NUMERO_MOVIL,        String LIQUIDADO,        String CEDULA_CONDUCTOR,        String CONDUCTOR,        String USUARIO,        String TOTAL,        String HORA_MODIFICACION,        String APELLIDO,        String CEDULA,        String TOTAL_RECAUDO_NETO,        String NOMBRE_PERSONA,        String FECHA    ) {
        super(
        );
        this.TOTAL_RECAUDO_BRUTO = TOTAL_RECAUDO_BRUTO;
        this.ID = ID;
        this.TOTAL_GASTOS = TOTAL_GASTOS;
        this.TOTAL_DEPOSITO = TOTAL_DEPOSITO;
        this.NUMERO_MOVIL = NUMERO_MOVIL;
        this.LIQUIDADO = LIQUIDADO;
        this.CEDULA_CONDUCTOR = CEDULA_CONDUCTOR;
        this.CONDUCTOR = CONDUCTOR;
        this.USUARIO = USUARIO;
        this.TOTAL = TOTAL;
        this.HORA_MODIFICACION = HORA_MODIFICACION;
        this.APELLIDO = APELLIDO;
        this.CEDULA = CEDULA;
        this.TOTAL_RECAUDO_NETO = TOTAL_RECAUDO_NETO;
        this.NOMBRE_PERSONA = NOMBRE_PERSONA;
        this.FECHA = FECHA;
    }


    public String getTotal_recaudo_bruto() {
        return TOTAL_RECAUDO_BRUTO;
    }

    public void setTotal_recaudo_bruto(String TOTAL_RECAUDO_BRUTO) {
        this.TOTAL_RECAUDO_BRUTO = TOTAL_RECAUDO_BRUTO;
    }
    public String getId() {
        return ID;
    }

    public void setId(String ID) {
        this.ID = ID;
    }
    public String getTotal_gastos() {
        return TOTAL_GASTOS;
    }

    public void setTotal_gastos(String TOTAL_GASTOS) {
        this.TOTAL_GASTOS = TOTAL_GASTOS;
    }
    public String getTotal_deposito() {
        return TOTAL_DEPOSITO;
    }

    public void setTotal_deposito(String TOTAL_DEPOSITO) {
        this.TOTAL_DEPOSITO = TOTAL_DEPOSITO;
    }
    public String getNumero_movil() {
        return NUMERO_MOVIL;
    }

    public void setNumero_movil(String NUMERO_MOVIL) {
        this.NUMERO_MOVIL = NUMERO_MOVIL;
    }
    public String getLiquidado() {
        return LIQUIDADO;
    }

    public void setLiquidado(String LIQUIDADO) {
        this.LIQUIDADO = LIQUIDADO;
    }
    public String getCedula_conductor() {
        return CEDULA_CONDUCTOR;
    }

    public void setCedula_conductor(String CEDULA_CONDUCTOR) {
        this.CEDULA_CONDUCTOR = CEDULA_CONDUCTOR;
    }
    public String getConductor() {
        return CONDUCTOR;
    }

    public void setConductor(String CONDUCTOR) {
        this.CONDUCTOR = CONDUCTOR;
    }
    public String getUsuario() {
        return USUARIO;
    }

    public void setUsuario(String USUARIO) {
        this.USUARIO = USUARIO;
    }
    public String getTotal() {
        return TOTAL;
    }

    public void setTotal(String TOTAL) {
        this.TOTAL = TOTAL;
    }
    public String getHora_modificacion() {
        return HORA_MODIFICACION;
    }

    public void setHora_modificacion(String HORA_MODIFICACION) {
        this.HORA_MODIFICACION = HORA_MODIFICACION;
    }
    public String getApellido() {
        return APELLIDO;
    }

    public void setApellido(String APELLIDO) {
        this.APELLIDO = APELLIDO;
    }
    public String getCedula() {
        return CEDULA;
    }

    public void setCedula(String CEDULA) {
        this.CEDULA = CEDULA;
    }
    public String getTotal_recaudo_neto() {
        return TOTAL_RECAUDO_NETO;
    }

    public void setTotal_recaudo_neto(String TOTAL_RECAUDO_NETO) {
        this.TOTAL_RECAUDO_NETO = TOTAL_RECAUDO_NETO;
    }
    public String getNombre_persona() {
        return NOMBRE_PERSONA;
    }

    public void setNombre_persona(String NOMBRE_PERSONA) {
        this.NOMBRE_PERSONA = NOMBRE_PERSONA;
    }
    public String getFecha() {
        return FECHA;
    }

    public void setFecha(String FECHA) {
        this.FECHA = FECHA;
    }


}