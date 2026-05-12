





import java.util.List;
import java.util.ArrayList;

public class Jugador  {

    private String Dorsal;
    private String Titulos;
    private String Posicion;
    private String Cod_persona;
    private String Cod_equipo;
    private String Altura;
    private String Peso;
    private String Cod_jugador;





    private Equipo equipo;


    public Jugador(
        String Dorsal,        String Titulos,        String Posicion,        String Cod_persona,        String Cod_equipo,        String Altura,        String Peso,        String Cod_jugador    ) {
        this.Dorsal = Dorsal;
        this.Titulos = Titulos;
        this.Posicion = Posicion;
        this.Cod_persona = Cod_persona;
        this.Cod_equipo = Cod_equipo;
        this.Altura = Altura;
        this.Peso = Peso;
        this.Cod_jugador = Cod_jugador;
    }


    public String getDorsal() {
        return Dorsal;
    }

    public void setDorsal(String Dorsal) {
        this.Dorsal = Dorsal;
    }
    public String getTitulos() {
        return Titulos;
    }

    public void setTitulos(String Titulos) {
        this.Titulos = Titulos;
    }
    public String getPosicion() {
        return Posicion;
    }

    public void setPosicion(String Posicion) {
        this.Posicion = Posicion;
    }
    public String getCod_persona() {
        return Cod_persona;
    }

    public void setCod_persona(String Cod_persona) {
        this.Cod_persona = Cod_persona;
    }
    public String getCod_equipo() {
        return Cod_equipo;
    }

    public void setCod_equipo(String Cod_equipo) {
        this.Cod_equipo = Cod_equipo;
    }
    public String getAltura() {
        return Altura;
    }

    public void setAltura(String Altura) {
        this.Altura = Altura;
    }
    public String getPeso() {
        return Peso;
    }

    public void setPeso(String Peso) {
        this.Peso = Peso;
    }
    public String getCod_jugador() {
        return Cod_jugador;
    }

    public void setCod_jugador(String Cod_jugador) {
        this.Cod_jugador = Cod_jugador;
    }

    public Equipo getEquipo() {
        return equipo;
    }

    public void setEquipo(Equipo equipo) {
        this.equipo = equipo;
    }

}