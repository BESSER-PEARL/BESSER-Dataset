





import java.util.List;
import java.util.ArrayList;

public class V_hicule1  {

    private int nbPlaces;
    private None propri_taire;
    private String imatriculation;
    private String modele;
    private String marque;



    public V_hicule1(
        int nbPlaces,        None propri_taire,        String imatriculation,        String modele,        String marque    ) {
        this.nbPlaces = nbPlaces;
        this.propri_taire = propri_taire;
        this.imatriculation = imatriculation;
        this.modele = modele;
        this.marque = marque;
    }


    public int getNbplaces() {
        return nbPlaces;
    }

    public void setNbplaces(int nbPlaces) {
        this.nbPlaces = nbPlaces;
    }
    public None getPropri_taire() {
        return propri_taire;
    }

    public void setPropri_taire(None propri_taire) {
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
    public String getMarque() {
        return marque;
    }

    public void setMarque(String marque) {
        this.marque = marque;
    }


}