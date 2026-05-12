





import java.util.List;
import java.util.ArrayList;

public class TELEFONO  {

    private String CODIGO_DE__AREA;
    private int PREFIJO;
    private int NUMBER;





    private CONTACTO contacto;


    public TELEFONO(
        String CODIGO_DE__AREA,        int PREFIJO,        int NUMBER    ) {
        this.CODIGO_DE__AREA = CODIGO_DE__AREA;
        this.PREFIJO = PREFIJO;
        this.NUMBER = NUMBER;
    }


    public String getCodigo_de__area() {
        return CODIGO_DE__AREA;
    }

    public void setCodigo_de__area(String CODIGO_DE__AREA) {
        this.CODIGO_DE__AREA = CODIGO_DE__AREA;
    }
    public int getPrefijo() {
        return PREFIJO;
    }

    public void setPrefijo(int PREFIJO) {
        this.PREFIJO = PREFIJO;
    }
    public int getNumber() {
        return NUMBER;
    }

    public void setNumber(int NUMBER) {
        this.NUMBER = NUMBER;
    }

    public CONTACTO getContacto() {
        return contacto;
    }

    public void setContacto(CONTACTO contacto) {
        this.contacto = contacto;
    }

}