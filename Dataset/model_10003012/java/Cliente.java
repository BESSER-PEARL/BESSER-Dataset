





import java.util.List;
import java.util.ArrayList;

public class Cliente  {

    private String Nombre;
    private String Direcci_n;
    private String email;
    private int Contacto;





    private Carro_de_Compras carro_de_compras;


    public Cliente(
        String Nombre,        String Direcci_n,        String email,        int Contacto    ) {
        this.Nombre = Nombre;
        this.Direcci_n = Direcci_n;
        this.email = email;
        this.Contacto = Contacto;
    }


    public String getNombre() {
        return Nombre;
    }

    public void setNombre(String Nombre) {
        this.Nombre = Nombre;
    }
    public String getDirecci_n() {
        return Direcci_n;
    }

    public void setDirecci_n(String Direcci_n) {
        this.Direcci_n = Direcci_n;
    }
    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }
    public int getContacto() {
        return Contacto;
    }

    public void setContacto(int Contacto) {
        this.Contacto = Contacto;
    }

    public Carro_de_Compras getCarro_de_compras() {
        return carro_de_compras;
    }

    public void setCarro_de_compras(Carro_de_Compras carro_de_compras) {
        this.carro_de_compras = carro_de_compras;
    }

}