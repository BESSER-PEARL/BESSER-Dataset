





import java.util.List;
import java.util.ArrayList;

public class Medecin  {

    private String prenomMedecin;
    private String dateNaissance;
    private String nomMedecin;
    private String specialite;



    public Medecin(
        String prenomMedecin,        String dateNaissance,        String nomMedecin,        String specialite    ) {
        this.prenomMedecin = prenomMedecin;
        this.dateNaissance = dateNaissance;
        this.nomMedecin = nomMedecin;
        this.specialite = specialite;
    }


    public String getPrenommedecin() {
        return prenomMedecin;
    }

    public void setPrenommedecin(String prenomMedecin) {
        this.prenomMedecin = prenomMedecin;
    }
    public String getDatenaissance() {
        return dateNaissance;
    }

    public void setDatenaissance(String dateNaissance) {
        this.dateNaissance = dateNaissance;
    }
    public String getNommedecin() {
        return nomMedecin;
    }

    public void setNommedecin(String nomMedecin) {
        this.nomMedecin = nomMedecin;
    }
    public String getSpecialite() {
        return specialite;
    }

    public void setSpecialite(String specialite) {
        this.specialite = specialite;
    }


}