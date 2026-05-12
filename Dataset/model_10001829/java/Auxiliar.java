





import java.util.List;
import java.util.ArrayList;

public class Auxiliar  {

    private String Id_auxiliar;
    private String Nombre_auxiliar;





    private List<Registro> registros;


    public Auxiliar(
        String Id_auxiliar,        String Nombre_auxiliar    ) {
        this.Id_auxiliar = Id_auxiliar;
        this.Nombre_auxiliar = Nombre_auxiliar;
        this.registros = new ArrayList<>();
    }

    public Auxiliar(
        String Id_auxiliar,        String Nombre_auxiliar        ArrayList<Registro> registros    ) {
        this.Id_auxiliar = Id_auxiliar;
        this.Nombre_auxiliar = Nombre_auxiliar;
        this.registros = registros;
    }

    public String getId_auxiliar() {
        return Id_auxiliar;
    }

    public void setId_auxiliar(String Id_auxiliar) {
        this.Id_auxiliar = Id_auxiliar;
    }
    public String getNombre_auxiliar() {
        return Nombre_auxiliar;
    }

    public void setNombre_auxiliar(String Nombre_auxiliar) {
        this.Nombre_auxiliar = Nombre_auxiliar;
    }

    public List<Registro> getRegistros() {
        return registros;
    }

    public void addRegistro(Registro registro) {
        this.registros.add(registro);
    }

}