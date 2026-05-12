





import java.util.List;
import java.util.ArrayList;

public class Cliente  {

    private String Asunto;
    private String Ciudad;
    private String Nombre;



    public Cliente(
        String Asunto,        String Ciudad,        String Nombre    ) {
        this.Asunto = Asunto;
        this.Ciudad = Ciudad;
        this.Nombre = Nombre;
    }


    public String getAsunto() {
        return Asunto;
    }

    public void setAsunto(String Asunto) {
        this.Asunto = Asunto;
    }
    public String getCiudad() {
        return Ciudad;
    }

    public void setCiudad(String Ciudad) {
        this.Ciudad = Ciudad;
    }
    public String getNombre() {
        return Nombre;
    }

    public void setNombre(String Nombre) {
        this.Nombre = Nombre;
    }


}