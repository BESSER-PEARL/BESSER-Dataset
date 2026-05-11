





import java.util.List;
import java.util.ArrayList;

public class SimpleClass_Class extends Classifier {

    private String is_persistent;
    private String tipo;



    public SimpleClass_Class(
        String is_persistent,        String tipo    ) {
        super(
        );
        this.is_persistent = is_persistent;
        this.tipo = tipo;
    }


    public String getIs_persistent() {
        return is_persistent;
    }

    public void setIs_persistent(String is_persistent) {
        this.is_persistent = is_persistent;
    }
    public String getTipo() {
        return tipo;
    }

    public void setTipo(String tipo) {
        this.tipo = tipo;
    }


}