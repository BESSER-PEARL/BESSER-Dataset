





import java.util.List;
import java.util.ArrayList;

public class Jugador  {

    private String Posicion;
    private String Peso;
    private String Altura;
    private String Cod_jugador;
    private String Cod_persona;
    private String Titulos;
    private String Dorsal;
    private String Cod_equipo;





    private Equipo equipo;


    public Jugador(
        String Posicion,        String Peso,        String Altura,        String Cod_jugador,        String Cod_persona,        String Titulos,        String Dorsal,        String Cod_equipo    ) {
        this.Posicion = Posicion;
        this.Peso = Peso;
        this.Altura = Altura;
        this.Cod_jugador = Cod_jugador;
        this.Cod_persona = Cod_persona;
        this.Titulos = Titulos;
        this.Dorsal = Dorsal;
        this.Cod_equipo = Cod_equipo;
    }


    public String getPosicion() {
        return Posicion;
    }

    public void setPosicion(String Posicion) {
        this.Posicion = Posicion;
    }
    public String getPeso() {
        return Peso;
    }

    public void setPeso(String Peso) {
        this.Peso = Peso;
    }
    public String getAltura() {
        return Altura;
    }

    public void setAltura(String Altura) {
        this.Altura = Altura;
    }
    public String getCod_jugador() {
        return Cod_jugador;
    }

    public void setCod_jugador(String Cod_jugador) {
        this.Cod_jugador = Cod_jugador;
    }
    public String getCod_persona() {
        return Cod_persona;
    }

    public void setCod_persona(String Cod_persona) {
        this.Cod_persona = Cod_persona;
    }
    public String getTitulos() {
        return Titulos;
    }

    public void setTitulos(String Titulos) {
        this.Titulos = Titulos;
    }
    public String getDorsal() {
        return Dorsal;
    }

    public void setDorsal(String Dorsal) {
        this.Dorsal = Dorsal;
    }
    public String getCod_equipo() {
        return Cod_equipo;
    }

    public void setCod_equipo(String Cod_equipo) {
        this.Cod_equipo = Cod_equipo;
    }

    public Equipo getEquipo() {
        return equipo;
    }

    public void setEquipo(Equipo equipo) {
        this.equipo = equipo;
    }

}