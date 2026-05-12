





import java.util.List;
import java.util.ArrayList;

public class Persona  {

    private String NombreCorto;
    private String Apellido;
    private String Nacionalidad;
    private String Cod_persona;
    private String Nombre;
    private String FechaNacimiento;





    private List<Jugador> jugadors;




    private List<Arbitro> arbitros;




    private List<Entrenador> entrenadors;


    public Persona(
        String NombreCorto,        String Apellido,        String Nacionalidad,        String Cod_persona,        String Nombre,        String FechaNacimiento    ) {
        this.NombreCorto = NombreCorto;
        this.Apellido = Apellido;
        this.Nacionalidad = Nacionalidad;
        this.Cod_persona = Cod_persona;
        this.Nombre = Nombre;
        this.FechaNacimiento = FechaNacimiento;
        this.jugadors = new ArrayList<>();
        this.arbitros = new ArrayList<>();
        this.entrenadors = new ArrayList<>();
    }

    public Persona(
        String NombreCorto,        String Apellido,        String Nacionalidad,        String Cod_persona,        String Nombre,        String FechaNacimiento        ArrayList<Jugador> jugadors,        ArrayList<Arbitro> arbitros,        ArrayList<Entrenador> entrenadors    ) {
        this.NombreCorto = NombreCorto;
        this.Apellido = Apellido;
        this.Nacionalidad = Nacionalidad;
        this.Cod_persona = Cod_persona;
        this.Nombre = Nombre;
        this.FechaNacimiento = FechaNacimiento;
        this.jugadors = jugadors;
        this.arbitros = arbitros;
        this.entrenadors = entrenadors;
    }

    public String getNombrecorto() {
        return NombreCorto;
    }

    public void setNombrecorto(String NombreCorto) {
        this.NombreCorto = NombreCorto;
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

    public List<Jugador> getJugadors() {
        return jugadors;
    }

    public void addJugador(Jugador jugador) {
        this.jugadors.add(jugador);
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

}