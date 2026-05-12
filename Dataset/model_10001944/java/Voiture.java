





import java.util.List;
import java.util.ArrayList;

public class Voiture  {

    private int id;
    private String modele;
    private String marque;
    private String immatriculation;



    public Voiture(
        int id,        String modele,        String marque,        String immatriculation    ) {
        this.id = id;
        this.modele = modele;
        this.marque = marque;
        this.immatriculation = immatriculation;
    }


    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    public String getModele() {
        return modele;
    }

    public void setModele(String modele) {
        this.modele = modele;
    }
    public String getMarque() {
        return marque;
    }

    public void setMarque(String marque) {
        this.marque = marque;
    }
    public String getImmatriculation() {
        return immatriculation;
    }

    public void setImmatriculation(String immatriculation) {
        this.immatriculation = immatriculation;
    }


}