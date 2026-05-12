





import java.util.List;
import java.util.ArrayList;

public class V_hicule1  {

    private String imatriculation;
    private String modele;
    private int nbPlaces;
    private String marque;
    private None propri_taire;



    public V_hicule1(
        String imatriculation,        String modele,        int nbPlaces,        String marque,        None propri_taire    ) {
        this.imatriculation = imatriculation;
        this.modele = modele;
        this.nbPlaces = nbPlaces;
        this.marque = marque;
        this.propri_taire = propri_taire;
    }


    public String getImatriculation() {
        return imatriculation;
    }

    public void setImatriculation(String imatriculation) {
        this.imatriculation = imatriculation;
    }
    public String getModele() {
        return modele;
    }

    public void setModele(String modele) {
        this.modele = modele;
    }
    public int getNbplaces() {
        return nbPlaces;
    }

    public void setNbplaces(int nbPlaces) {
        this.nbPlaces = nbPlaces;
    }
    public String getMarque() {
        return marque;
    }

    public void setMarque(String marque) {
        this.marque = marque;
    }
    public None getPropri_taire() {
        return propri_taire;
    }

    public void setPropri_taire(None propri_taire) {
        this.propri_taire = propri_taire;
    }


}