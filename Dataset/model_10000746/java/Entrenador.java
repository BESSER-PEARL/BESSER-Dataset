





import java.util.List;
import java.util.ArrayList;

public class Entrenador  {

    private String Cod_Entrenador;
    private String Titulos;
    private String Cod_persona;





    private Equipo equipo;


    public Entrenador(
        String Cod_Entrenador,        String Titulos,        String Cod_persona    ) {
        this.Cod_Entrenador = Cod_Entrenador;
        this.Titulos = Titulos;
        this.Cod_persona = Cod_persona;
    }


    public String getCod_entrenador() {
        return Cod_Entrenador;
    }

    public void setCod_entrenador(String Cod_Entrenador) {
        this.Cod_Entrenador = Cod_Entrenador;
    }
    public String getTitulos() {
        return Titulos;
    }

    public void setTitulos(String Titulos) {
        this.Titulos = Titulos;
    }
    public String getCod_persona() {
        return Cod_persona;
    }

    public void setCod_persona(String Cod_persona) {
        this.Cod_persona = Cod_persona;
    }

    public Equipo getEquipo() {
        return equipo;
    }

    public void setEquipo(Equipo equipo) {
        this.equipo = equipo;
    }

}