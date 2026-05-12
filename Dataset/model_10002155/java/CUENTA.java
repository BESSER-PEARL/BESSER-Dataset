





import java.util.List;
import java.util.ArrayList;

public class CUENTA  {

    private String Nombre;
    private String Tipo_de_Cuenta;
    private int Balance;



    public CUENTA(
        String Nombre,        String Tipo_de_Cuenta,        int Balance    ) {
        this.Nombre = Nombre;
        this.Tipo_de_Cuenta = Tipo_de_Cuenta;
        this.Balance = Balance;
    }


    public String getNombre() {
        return Nombre;
    }

    public void setNombre(String Nombre) {
        this.Nombre = Nombre;
    }
    public String getTipo_de_cuenta() {
        return Tipo_de_Cuenta;
    }

    public void setTipo_de_cuenta(String Tipo_de_Cuenta) {
        this.Tipo_de_Cuenta = Tipo_de_Cuenta;
    }
    public int getBalance() {
        return Balance;
    }

    public void setBalance(int Balance) {
        this.Balance = Balance;
    }


}