





import java.util.List;
import java.util.ArrayList;

public class V_hicule  {

    private String imatriculation;
    private None propri_taire;
    private String modele;
    private String marque;



    public V_hicule(
        String imatriculation,        None propri_taire,        String modele,        String marque    ) {
        this.imatriculation = imatriculation;
        this.propri_taire = propri_taire;
        this.modele = modele;
        this.marque = marque;
    }


    public String getImatriculation() {
        return imatriculation;
    }

    public void setImatriculation(String imatriculation) {
        this.imatriculation = imatriculation;
    }
    public None getPropri_taire() {
        return propri_taire;
    }

    public void setPropri_taire(None propri_taire) {
        this.propri_taire = propri_taire;
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