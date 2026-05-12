





import java.util.List;
import java.util.ArrayList;

public class Medecin  {

    private String specialite;
    private int numeroMedecin;
    private String prenomMedecin;
    private String dateNaissance;
    private String nomMedecin;





    private Rendez_Vous rendez_vous;


    public Medecin(
        String specialite,        int numeroMedecin,        String prenomMedecin,        String dateNaissance,        String nomMedecin    ) {
        this.specialite = specialite;
        this.numeroMedecin = numeroMedecin;
        this.prenomMedecin = prenomMedecin;
        this.dateNaissance = dateNaissance;
        this.nomMedecin = nomMedecin;
    }


    public String getSpecialite() {
        return specialite;
    }

    public void setSpecialite(String specialite) {
        this.specialite = specialite;
    }
    public int getNumeromedecin() {
        return numeroMedecin;
    }

    public void setNumeromedecin(int numeroMedecin) {
        this.numeroMedecin = numeroMedecin;
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

    public Rendez_Vous getRendez_vous() {
        return rendez_vous;
    }

    public void setRendez_vous(Rendez_Vous rendez_vous) {
        this.rendez_vous = rendez_vous;
    }

}