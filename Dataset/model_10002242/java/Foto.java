





import java.util.List;
import java.util.ArrayList;

public class Foto  {

    private int ancho;
    private int largo;





    private Contacto contacto;


    public Foto(
        int ancho,        int largo    ) {
        this.ancho = ancho;
        this.largo = largo;
    }


    public int getAncho() {
        return ancho;
    }

    public void setAncho(int ancho) {
        this.ancho = ancho;
    }
    public int getLargo() {
        return largo;
    }

    public void setLargo(int largo) {
        this.largo = largo;
    }

    public Contacto getContacto() {
        return contacto;
    }

    public void setContacto(Contacto contacto) {
        this.contacto = contacto;
    }

}