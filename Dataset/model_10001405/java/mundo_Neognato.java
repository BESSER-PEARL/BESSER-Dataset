





import java.util.List;
import java.util.ArrayList;

public class mundo_Neognato  {

    private String longitudTercerDedo;
    private String numeroHuesosPata;



    public mundo_Neognato(
        String longitudTercerDedo,        String numeroHuesosPata    ) {
        this.longitudTercerDedo = longitudTercerDedo;
        this.numeroHuesosPata = numeroHuesosPata;
    }


    public String getLongitudtercerdedo() {
        return longitudTercerDedo;
    }

    public void setLongitudtercerdedo(String longitudTercerDedo) {
        this.longitudTercerDedo = longitudTercerDedo;
    }
    public String getNumerohuesospata() {
        return numeroHuesosPata;
    }

    public void setNumerohuesospata(String numeroHuesosPata) {
        this.numeroHuesosPata = numeroHuesosPata;
    }


}