





import java.util.List;
import java.util.ArrayList;

public class gestionmodelosconsultas_resultcotracir_Transaccion extends ElementoModeloResultado {

    private String ESTADO_TRANSACCION;
    private String ID;
    private String HORA;
    private String VALOR;
    private String CATEGORIA;
    private String DESCRIPCION;
    private String TIPO;



    public gestionmodelosconsultas_resultcotracir_Transaccion(
        String ESTADO_TRANSACCION,        String ID,        String HORA,        String VALOR,        String CATEGORIA,        String DESCRIPCION,        String TIPO    ) {
        super(
        );
        this.ESTADO_TRANSACCION = ESTADO_TRANSACCION;
        this.ID = ID;
        this.HORA = HORA;
        this.VALOR = VALOR;
        this.CATEGORIA = CATEGORIA;
        this.DESCRIPCION = DESCRIPCION;
        this.TIPO = TIPO;
    }


    public String getEstado_transaccion() {
        return ESTADO_TRANSACCION;
    }

    public void setEstado_transaccion(String ESTADO_TRANSACCION) {
        this.ESTADO_TRANSACCION = ESTADO_TRANSACCION;
    }
    public String getId() {
        return ID;
    }

    public void setId(String ID) {
        this.ID = ID;
    }
    public String getHora() {
        return HORA;
    }

    public void setHora(String HORA) {
        this.HORA = HORA;
    }
    public String getValor() {
        return VALOR;
    }

    public void setValor(String VALOR) {
        this.VALOR = VALOR;
    }
    public String getCategoria() {
        return CATEGORIA;
    }

    public void setCategoria(String CATEGORIA) {
        this.CATEGORIA = CATEGORIA;
    }
    public String getDescripcion() {
        return DESCRIPCION;
    }

    public void setDescripcion(String DESCRIPCION) {
        this.DESCRIPCION = DESCRIPCION;
    }
    public String getTipo() {
        return TIPO;
    }

    public void setTipo(String TIPO) {
        this.TIPO = TIPO;
    }


}