





import java.util.List;
import java.util.ArrayList;

public class Gato  {

    private String Color;
    private String Nombre;
    private String Raza;



    public Gato(
        String Color,        String Nombre,        String Raza    ) {
        this.Color = Color;
        this.Nombre = Nombre;
        this.Raza = Raza;
    }


    public String getColor() {
        return Color;
    }

    public void setColor(String Color) {
        this.Color = Color;
    }
    public String getNombre() {
        return Nombre;
    }

    public void setNombre(String Nombre) {
        this.Nombre = Nombre;
    }
    public String getRaza() {
        return Raza;
    }

    public void setRaza(String Raza) {
        this.Raza = Raza;
    }


}