





import java.util.List;
import java.util.ArrayList;

public class USUARIO  {

    private String Contrase_a;
    private String ID;
    private String Nombre;





    private List<CUENTA> cuentas;


    public USUARIO(
        String Contrase_a,        String ID,        String Nombre    ) {
        this.Contrase_a = Contrase_a;
        this.ID = ID;
        this.Nombre = Nombre;
        this.cuentas = new ArrayList<>();
    }

    public USUARIO(
        String Contrase_a,        String ID,        String Nombre        ArrayList<CUENTA> cuentas    ) {
        this.Contrase_a = Contrase_a;
        this.ID = ID;
        this.Nombre = Nombre;
        this.cuentas = cuentas;
    }

    public String getContrase_a() {
        return Contrase_a;
    }

    public void setContrase_a(String Contrase_a) {
        this.Contrase_a = Contrase_a;
    }
    public String getId() {
        return ID;
    }

    public void setId(String ID) {
        this.ID = ID;
    }
    public String getNombre() {
        return Nombre;
    }

    public void setNombre(String Nombre) {
        this.Nombre = Nombre;
    }

    public List<CUENTA> getCuentas() {
        return cuentas;
    }

    public void addCuenta(Cuenta cuenta) {
        this.cuentas.add(cuenta);
    }

}