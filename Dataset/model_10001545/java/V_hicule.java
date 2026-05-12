





import java.util.List;
import java.util.ArrayList;

public class V_hicule  {

    private None propri_taire;
    private String imatriculation;
    private String marque;
    private String modele;



    public V_hicule(
        None propri_taire,        String imatriculation,        String marque,        String modele    ) {
        this.propri_taire = propri_taire;
        this.imatriculation = imatriculation;
        this.marque = marque;
        this.modele = modele;
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
    public String getMarque() {
        return marque;
    }

    public void setMarque(String marque) {
        this.marque = marque;
    }
    public String getModele() {
        return modele;
    }

    public void setModele(String modele) {
        this.modele = modele;
    }


}