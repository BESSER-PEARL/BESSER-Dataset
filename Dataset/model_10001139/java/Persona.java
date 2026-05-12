





import java.util.List;
import java.util.ArrayList;

public class Persona  {

    private String FechaNacimiento;
    private String Apellido;
    private String Nombre;
    private String NombreCorto;
    private String Cod_persona;
    private String Nacionalidad;





    private List<Entrenador> entrenadors;




    private List<Arbitro> arbitros;




    private List<Jugador> jugadors;


    public Persona(
        String FechaNacimiento,        String Apellido,        String Nombre,        String NombreCorto,        String Cod_persona,        String Nacionalidad    ) {
        this.FechaNacimiento = FechaNacimiento;
        this.Apellido = Apellido;
        this.Nombre = Nombre;
        this.NombreCorto = NombreCorto;
        this.Cod_persona = Cod_persona;
        this.Nacionalidad = Nacionalidad;
        this.entrenadors = new ArrayList<>();
        this.arbitros = new ArrayList<>();
        this.jugadors = new ArrayList<>();
    }

    public Persona(
        String FechaNacimiento,        String Apellido,        String Nombre,        String NombreCorto,        String Cod_persona,        String Nacionalidad        ArrayList<Entrenador> entrenadors,        ArrayList<Arbitro> arbitros,        ArrayList<Jugador> jugadors    ) {
        this.FechaNacimiento = FechaNacimiento;
        this.Apellido = Apellido;
        this.Nombre = Nombre;
        this.NombreCorto = NombreCorto;
        this.Cod_persona = Cod_persona;
        this.Nacionalidad = Nacionalidad;
        this.entrenadors = entrenadors;
        this.arbitros = arbitros;
        this.jugadors = jugadors;
    }

    public String getFechanacimiento() {
        return FechaNacimiento;
    }

    public void setFechanacimiento(String FechaNacimiento) {
        this.FechaNacimiento = FechaNacimiento;
    }
    public String getApellido() {
        return Apellido;
    }

    public void setApellido(String Apellido) {
        this.Apellido = Apellido;
    }
    public String getNombre() {
        return Nombre;
    }

    public void setNombre(String Nombre) {
        this.Nombre = Nombre;
    }
    public String getNombrecorto() {
        return NombreCorto;
    }

    public void setNombrecorto(String NombreCorto) {
        this.NombreCorto = NombreCorto;
    }
    public String getCod_persona() {
        return Cod_persona;
    }

    public void setCod_persona(String Cod_persona) {
        this.Cod_persona = Cod_persona;
    }
    public String getNacionalidad() {
        return Nacionalidad;
    }

    public void setNacionalidad(String Nacionalidad) {
        this.Nacionalidad = Nacionalidad;
    }

    public List<Entrenador> getEntrenadors() {
        return entrenadors;
    }

    public void addEntrenador(Entrenador entrenador) {
        this.entrenadors.add(entrenador);
    }
    public List<Arbitro> getArbitros() {
        return arbitros;
    }

    public void addArbitro(Arbitro arbitro) {
        this.arbitros.add(arbitro);
    }
    public List<Jugador> getJugadors() {
        return jugadors;
    }

    public void addJugador(Jugador jugador) {
        this.jugadors.add(jugador);
    }

}