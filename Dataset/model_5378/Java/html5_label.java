





import java.util.List;
import java.util.ArrayList;

public class html5_label extends htmlElement {

    private String value;
    private String valor;



    public html5_label(
        String value,        String valor    ) {
        super(
        );
        this.value = value;
        this.valor = valor;
    }


    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }
    public String getValor() {
        return valor;
    }

    public void setValor(String valor) {
        this.valor = valor;
    }


}