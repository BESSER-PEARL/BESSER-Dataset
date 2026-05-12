





import java.util.List;
import java.util.ArrayList;

public class Tel_fono  {

    private int numero;
    private int prefijo;
    private int Codigo_area;





    private Contacto contacto;


    public Tel_fono(
        int numero,        int prefijo,        int Codigo_area    ) {
        this.numero = numero;
        this.prefijo = prefijo;
        this.Codigo_area = Codigo_area;
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
    public int getCodigo_area() {
        return Codigo_area;
    }

    public void setCodigo_area(int Codigo_area) {
        this.Codigo_area = Codigo_area;
    }

    public Contacto getContacto() {
        return contacto;
    }

    public void setContacto(Contacto contacto) {
        this.contacto = contacto;
    }

}