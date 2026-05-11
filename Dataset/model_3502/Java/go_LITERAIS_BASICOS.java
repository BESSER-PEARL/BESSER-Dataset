





import java.util.List;
import java.util.ArrayList;

public class go_LITERAIS_BASICOS  {

    private String numero;
    private String string;





    private go_BINARY_EXP go_binary_exp;


    public go_LITERAIS_BASICOS(
        String numero,        String string    ) {
        this.numero = numero;
        this.string = string;
    }


    public String getNumero() {
        return numero;
    }

    public void setNumero(String numero) {
        this.numero = numero;
    }
    public String getString() {
        return string;
    }

    public void setString(String string) {
        this.string = string;
    }

    public go_BINARY_EXP getGo_binary_exp() {
        return go_binary_exp;
    }

    public void setGo_binary_exp(go_BINARY_EXP go_binary_exp) {
        this.go_binary_exp = go_binary_exp;
    }

}