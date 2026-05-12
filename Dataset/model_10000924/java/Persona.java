





import java.util.List;
import java.util.ArrayList;

public class Persona  {

    private String NombreCorto;
    private String Apellido;
    private String Cod_persona;
    private String Nacionalidad;
    private String Nombre;
    private String FechaNacimiento;



    public Persona(
        String NombreCorto,        String Apellido,        String Cod_persona,        String Nacionalidad,        String Nombre,        String FechaNacimiento    ) {
        this.NombreCorto = NombreCorto;
        this.Apellido = Apellido;
        this.Cod_persona = Cod_persona;
        this.Nacionalidad = Nacionalidad;
        this.Nombre = Nombre;
        this.FechaNacimiento = FechaNacimiento;
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


}