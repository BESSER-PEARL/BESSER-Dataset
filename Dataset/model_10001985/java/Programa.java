





import java.util.List;
import java.util.ArrayList;

public class Programa  {

    private int Codigo;
    private String Nombre;





    private Pemsum_Universitario pemsum_universitario;


    public Programa(
        int Codigo,        String Nombre    ) {
        this.Codigo = Codigo;
        this.Nombre = Nombre;
    }


    public int getCodigo() {
        return Codigo;
    }

    public void setCodigo(int Codigo) {
        this.Codigo = Codigo;
    }
    public String getNombre() {
        return Nombre;
    }

    public void setNombre(String Nombre) {
        this.Nombre = Nombre;
    }

    public Pemsum_Universitario getPemsum_universitario() {
        return pemsum_universitario;
    }

    public void setPemsum_universitario(Pemsum_Universitario pemsum_universitario) {
        this.pemsum_universitario = pemsum_universitario;
    }

}