





import java.util.List;
import java.util.ArrayList;

public class RDBMS_Table  {

    private String name;
    private String tipo;



    public RDBMS_Table(
        String name,        String tipo    ) {
        this.name = name;
        this.tipo = tipo;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getTipo() {
        return tipo;
    }

    public void setTipo(String tipo) {
        this.tipo = tipo;
    }


}