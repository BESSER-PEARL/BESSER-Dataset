





import java.util.List;
import java.util.ArrayList;

public class Persona  {

    private String Apellido;
    private String Nacionalidad;
    private String Cod_persona;
    private String NombreCorto;
    private String Nombre;
    private String FechaNacimiento;





    private List<Arbitro> arbitros;




    private List<Entrenador> entrenadors;




    private List<Jugador> jugadors;


    public Persona(
        String Apellido,        String Nacionalidad,        String Cod_persona,        String NombreCorto,        String Nombre,        String FechaNacimiento    ) {
        this.Apellido = Apellido;
        this.Nacionalidad = Nacionalidad;
        this.Cod_persona = Cod_persona;
        this.NombreCorto = NombreCorto;
        this.Nombre = Nombre;
        this.FechaNacimiento = FechaNacimiento;
        this.arbitros = new ArrayList<>();
        this.entrenadors = new ArrayList<>();
        this.jugadors = new ArrayList<>();
    }

    public Persona(
        String Apellido,        String Nacionalidad,        String Cod_persona,        String NombreCorto,        String Nombre,        String FechaNacimiento        ArrayList<Arbitro> arbitros,        ArrayList<Entrenador> entrenadors,        ArrayList<Jugador> jugadors    ) {
        this.Apellido = Apellido;
        this.Nacionalidad = Nacionalidad;
        this.Cod_persona = Cod_persona;
        this.NombreCorto = NombreCorto;
        this.Nombre = Nombre;
        this.FechaNacimiento = FechaNacimiento;
        this.arbitros = arbitros;
        this.entrenadors = entrenadors;
        this.jugadors = jugadors;
    }

    public String getApellido() {
        return Apellido;
    }

    public void setApellido(String Apellido) {
        this.Apellido = Apellido;
    }
    public String getNacionalidad() {
        return Nacionalidad;
    }

    public void setNacionalidad(String Nacionalidad) {
        this.Nacionalidad = Nacionalidad;
    }
    public String getCod_persona() {
        return Cod_persona;
    }

    public void setCod_persona(String Cod_persona) {
        this.Cod_persona = Cod_persona;
    }
    public String getNombrecorto() {
        return NombreCorto;
    }

    public void setNombrecorto(String NombreCorto) {
        this.NombreCorto = NombreCorto;
    }
    public String getNombre() {
        return Nombre;
    }

    public void setNombre(String Nombre) {
        this.Nombre = Nombre;
    }
    public String getFechanacimiento() {
        return FechaNacimiento;
    }

    public void setFechanacimiento(String FechaNacimiento) {
        this.FechaNacimiento = FechaNacimiento;
    }

    public List<Arbitro> getArbitros() {
        return arbitros;
    }

    public void addArbitro(Arbitro arbitro) {
        this.arbitros.add(arbitro);
    }
    public List<Entrenador> getEntrenadors() {
        return entrenadors;
    }

    public void addEntrenador(Entrenador entrenador) {
        this.entrenadors.add(entrenador);
    }
    public List<Jugador> getJugadors() {
        return jugadors;
    }

    public void addJugador(Jugador jugador) {
        this.jugadors.add(jugador);
    }

}