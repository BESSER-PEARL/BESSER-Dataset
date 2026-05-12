





import java.util.List;
import java.util.ArrayList;

public class Materias  {

    private String Nombre;
    private String Tipo;
    private int Codigo;
    private int Creditos;





    private Pemsum_Universitario pemsum_universitario;


    public Materias(
        String Nombre,        String Tipo,        int Codigo,        int Creditos    ) {
        this.Nombre = Nombre;
        this.Tipo = Tipo;
        this.Codigo = Codigo;
        this.Creditos = Creditos;
    }


    public String getNombre() {
        return Nombre;
    }

    public void setNombre(String Nombre) {
        this.Nombre = Nombre;
    }
    public String getTipo() {
        return Tipo;
    }

    public void setTipo(String Tipo) {
        this.Tipo = Tipo;
    }
    public int getCodigo() {
        return Codigo;
    }

    public void setCodigo(int Codigo) {
        this.Codigo = Codigo;
    }
    public int getCreditos() {
        return Creditos;
    }

    public void setCreditos(int Creditos) {
        this.Creditos = Creditos;
    }

    public Pemsum_Universitario getPemsum_universitario() {
        return pemsum_universitario;
    }

    public void setPemsum_universitario(Pemsum_Universitario pemsum_universitario) {
        this.pemsum_universitario = pemsum_universitario;
    }

}