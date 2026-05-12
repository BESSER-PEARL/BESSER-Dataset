





import java.util.List;
import java.util.ArrayList;

public class voiture  {

    private int nombre_de_si_ges;
    private String type_de_voiture;



    public voiture(
        int nombre_de_si_ges,        String type_de_voiture    ) {
        this.nombre_de_si_ges = nombre_de_si_ges;
        this.type_de_voiture = type_de_voiture;
    }


    public int getNombre_de_si_ges() {
        return nombre_de_si_ges;
    }

    public void setNombre_de_si_ges(int nombre_de_si_ges) {
        this.nombre_de_si_ges = nombre_de_si_ges;
    }
    public String getType_de_voiture() {
        return type_de_voiture;
    }

    public void setType_de_voiture(String type_de_voiture) {
        this.type_de_voiture = type_de_voiture;
    }


}