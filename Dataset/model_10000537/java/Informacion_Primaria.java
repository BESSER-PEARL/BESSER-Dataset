





import java.util.List;
import java.util.ArrayList;

public class Informacion_Primaria  {

    private String Type_of_wash;
    private String Type_of_car;





    private Usuario usuario;


    public Informacion_Primaria(
        String Type_of_wash,        String Type_of_car    ) {
        this.Type_of_wash = Type_of_wash;
        this.Type_of_car = Type_of_car;
    }


    public String getType_of_wash() {
        return Type_of_wash;
    }

    public void setType_of_wash(String Type_of_wash) {
        this.Type_of_wash = Type_of_wash;
    }
    public String getType_of_car() {
        return Type_of_car;
    }

    public void setType_of_car(String Type_of_car) {
        this.Type_of_car = Type_of_car;
    }

    public Usuario getUsuario() {
        return usuario;
    }

    public void setUsuario(Usuario usuario) {
        this.usuario = usuario;
    }

}