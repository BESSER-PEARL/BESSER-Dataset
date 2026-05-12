





import java.util.List;
import java.util.ArrayList;

public class Medecin  {

    private String specialite;
    private String nomMedecin;
    private String dateNaissance;
    private String prenomMedecin;



    public Medecin(
        String specialite,        String nomMedecin,        String dateNaissance,        String prenomMedecin    ) {
        this.specialite = specialite;
        this.nomMedecin = nomMedecin;
        this.dateNaissance = dateNaissance;
        this.prenomMedecin = prenomMedecin;
    }


    public String getSpecialite() {
        return specialite;
    }

    public void setSpecialite(String specialite) {
        this.specialite = specialite;
    }
    public String getNommedecin() {
        return nomMedecin;
    }

    public void setNommedecin(String nomMedecin) {
        this.nomMedecin = nomMedecin;
    }
    public String getDatenaissance() {
        return dateNaissance;
    }

    public void setDatenaissance(String dateNaissance) {
        this.dateNaissance = dateNaissance;
    }
    public String getPrenommedecin() {
        return prenomMedecin;
    }

    public void setPrenommedecin(String prenomMedecin) {
        this.prenomMedecin = prenomMedecin;
    }


}