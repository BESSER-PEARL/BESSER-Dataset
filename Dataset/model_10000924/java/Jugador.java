





import java.util.List;
import java.util.ArrayList;

public class Jugador  {

    private String Dorsal;
    private String Titulos;
    private String Peso;
    private String Cod_persona;
    private String Cod_jugador;
    private String Posicion;
    private String Altura;
    private String Cod_equipo;





    private Equipo equipo;




    private List<Lesion> lesions;




    private Persona persona;


    public Jugador(
        String Dorsal,        String Titulos,        String Peso,        String Cod_persona,        String Cod_jugador,        String Posicion,        String Altura,        String Cod_equipo    ) {
        this.Dorsal = Dorsal;
        this.Titulos = Titulos;
        this.Peso = Peso;
        this.Cod_persona = Cod_persona;
        this.Cod_jugador = Cod_jugador;
        this.Posicion = Posicion;
        this.Altura = Altura;
        this.Cod_equipo = Cod_equipo;
        this.lesions = new ArrayList<>();
    }

    public Jugador(
        String Dorsal,        String Titulos,        String Peso,        String Cod_persona,        String Cod_jugador,        String Posicion,        String Altura,        String Cod_equipo        ArrayList<Lesion> lesions    ) {
        this.Dorsal = Dorsal;
        this.Titulos = Titulos;
        this.Peso = Peso;
        this.Cod_persona = Cod_persona;
        this.Cod_jugador = Cod_jugador;
        this.Posicion = Posicion;
        this.Altura = Altura;
        this.Cod_equipo = Cod_equipo;
        this.lesions = lesions;
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
    public String getPeso() {
        return Peso;
    }

    public void setPeso(String Peso) {
        this.Peso = Peso;
    }
    public String getCod_persona() {
        return Cod_persona;
    }

    public void setCod_persona(String Cod_persona) {
        this.Cod_persona = Cod_persona;
    }
    public String getCod_jugador() {
        return Cod_jugador;
    }

    public void setCod_jugador(String Cod_jugador) {
        this.Cod_jugador = Cod_jugador;
    }
    public String getPosicion() {
        return Posicion;
    }

    public void setPosicion(String Posicion) {
        this.Posicion = Posicion;
    }
    public String getAltura() {
        return Altura;
    }

    public void setAltura(String Altura) {
        this.Altura = Altura;
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
    public List<Lesion> getLesions() {
        return lesions;
    }

    public void addLesion(Lesion lesion) {
        this.lesions.add(lesion);
    }
    public Persona getPersona() {
        return persona;
    }

    public void setPersona(Persona persona) {
        this.persona = persona;
    }

}