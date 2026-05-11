





import java.util.List;
import java.util.ArrayList;

public class SimpleRDBMS_Table  {

    private String tipo;
    private String name;



    public SimpleRDBMS_Table(
        String tipo,        String name    ) {
        this.tipo = tipo;
        this.name = name;
    }


    public String getTipo() {
        return tipo;
    }

    public void setTipo(String tipo) {
        this.tipo = tipo;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}