





import java.util.List;
import java.util.ArrayList;

public class arduino_Sketch  {

    private String Nombre;



    public arduino_Sketch(
        String Nombre    ) {
        this.Nombre = Nombre;
    }


    public String getNombre() {
        return Nombre;
    }

    public void setNombre(String Nombre) {
        this.Nombre = Nombre;
    }


}