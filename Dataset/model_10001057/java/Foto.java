





import java.util.List;
import java.util.ArrayList;

public class Foto  {

    private int alto;
    private int ancho;





    private Contacto contacto;


    public Foto(
        int alto,        int ancho    ) {
        this.alto = alto;
        this.ancho = ancho;
    }


    public int getAlto() {
        return alto;
    }

    public void setAlto(int alto) {
        this.alto = alto;
    }
    public int getAncho() {
        return ancho;
    }

    public void setAncho(int ancho) {
        this.ancho = ancho;
    }

    public Contacto getContacto() {
        return contacto;
    }

    public void setContacto(Contacto contacto) {
        this.contacto = contacto;
    }

}