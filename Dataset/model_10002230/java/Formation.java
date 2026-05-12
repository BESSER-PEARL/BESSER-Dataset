





import java.util.List;
import java.util.ArrayList;

public class Formation  {

    private String objectif;
    private String libelle;
    private int cout_unitaire;



    public Formation(
        String objectif,        String libelle,        int cout_unitaire    ) {
        this.objectif = objectif;
        this.libelle = libelle;
        this.cout_unitaire = cout_unitaire;
    }


    public String getObjectif() {
        return objectif;
    }

    public void setObjectif(String objectif) {
        this.objectif = objectif;
    }
    public String getLibelle() {
        return libelle;
    }

    public void setLibelle(String libelle) {
        this.libelle = libelle;
    }
    public int getCout_unitaire() {
        return cout_unitaire;
    }

    public void setCout_unitaire(int cout_unitaire) {
        this.cout_unitaire = cout_unitaire;
    }


}