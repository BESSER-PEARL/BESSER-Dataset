





import java.util.List;
import java.util.ArrayList;

public class Foto  {

    private int ancho;
    private int alto;





    private Contacto contacto;


    public Foto(
        int ancho,        int alto    ) {
        this.ancho = ancho;
        this.alto = alto;
    }


    public int getAncho() {
        return ancho;
    }

    public void setAncho(int ancho) {
        this.ancho = ancho;
    }
    public int getAlto() {
        return alto;
    }

    public void setAlto(int alto) {
        this.alto = alto;
    }

    public Contacto getContacto() {
        return contacto;
    }

    public void setContacto(Contacto contacto) {
        this.contacto = contacto;
    }

}