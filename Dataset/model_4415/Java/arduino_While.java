





import java.util.List;
import java.util.ArrayList;

public class arduino_While extends Bloques {

    private String operando;
    private String valor;
    private String referencia;



    public arduino_While(
        String operando,        String valor,        String referencia    ) {
        super(
        );
        this.operando = operando;
        this.valor = valor;
        this.referencia = referencia;
    }


    public String getOperando() {
        return operando;
    }

    public void setOperando(String operando) {
        this.operando = operando;
    }
    public String getValor() {
        return valor;
    }

    public void setValor(String valor) {
        this.valor = valor;
    }
    public String getReferencia() {
        return referencia;
    }

    public void setReferencia(String referencia) {
        this.referencia = referencia;
    }


}