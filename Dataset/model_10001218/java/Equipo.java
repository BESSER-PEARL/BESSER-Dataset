





import java.util.List;
import java.util.ArrayList;

public class Equipo  {

    private String Nombre;
    private String Titulos;
    private String F_fundacion;
    private String Cod_Entrenador;
    private String Ciudad;
    private String Cod_equipo;



    public Equipo(
        String Nombre,        String Titulos,        String F_fundacion,        String Cod_Entrenador,        String Ciudad,        String Cod_equipo    ) {
        this.Nombre = Nombre;
        this.Titulos = Titulos;
        this.F_fundacion = F_fundacion;
        this.Cod_Entrenador = Cod_Entrenador;
        this.Ciudad = Ciudad;
        this.Cod_equipo = Cod_equipo;
    }


    public String getNombre() {
        return Nombre;
    }

    public void setNombre(String Nombre) {
        this.Nombre = Nombre;
    }
    public String getTitulos() {
        return Titulos;
    }

    public void setTitulos(String Titulos) {
        this.Titulos = Titulos;
    }
    public String getF_fundacion() {
        return F_fundacion;
    }

    public void setF_fundacion(String F_fundacion) {
        this.F_fundacion = F_fundacion;
    }
    public String getCod_entrenador() {
        return Cod_Entrenador;
    }

    public void setCod_entrenador(String Cod_Entrenador) {
        this.Cod_Entrenador = Cod_Entrenador;
    }
    public String getCiudad() {
        return Ciudad;
    }

    public void setCiudad(String Ciudad) {
        this.Ciudad = Ciudad;
    }
    public String getCod_equipo() {
        return Cod_equipo;
    }

    public void setCod_equipo(String Cod_equipo) {
        this.Cod_equipo = Cod_equipo;
    }


}