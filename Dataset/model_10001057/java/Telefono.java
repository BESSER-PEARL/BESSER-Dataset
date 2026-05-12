





import java.util.List;
import java.util.ArrayList;

public class Telefono  {

    private int codigo;
    private int numero;
    private int prefijo;





    private Contacto contacto;




    private Contacto contacto;


    public Telefono(
        int codigo,        int numero,        int prefijo    ) {
        this.codigo = codigo;
        this.numero = numero;
        this.prefijo = prefijo;
    }


    public int getCodigo() {
        return codigo;
    }

    public void setCodigo(int codigo) {
        this.codigo = codigo;
    }
    public int getNumero() {
        return numero;
    }

    public void setNumero(int numero) {
        this.numero = numero;
    }
    public int getPrefijo() {
        return prefijo;
    }

    public void setPrefijo(int prefijo) {
        this.prefijo = prefijo;
    }

    public Contacto getContacto() {
        return contacto;
    }

    public void setContacto(Contacto contacto) {
        this.contacto = contacto;
    }
    public Contacto getContacto() {
        return contacto;
    }

    public void setContacto(Contacto contacto) {
        this.contacto = contacto;
    }

}