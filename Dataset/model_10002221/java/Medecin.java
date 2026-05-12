





import java.util.List;
import java.util.ArrayList;

public class Medecin  {

    private int numeroMedecin;
    private String nomMedecin;
    private String specialite;
    private String dateNaissance;
    private String prenomMedecin;





    private Rendez_Vous rendez_vous;


    public Medecin(
        int numeroMedecin,        String nomMedecin,        String specialite,        String dateNaissance,        String prenomMedecin    ) {
        this.numeroMedecin = numeroMedecin;
        this.nomMedecin = nomMedecin;
        this.specialite = specialite;
        this.dateNaissance = dateNaissance;
        this.prenomMedecin = prenomMedecin;
    }


    public int getNumeromedecin() {
        return numeroMedecin;
    }

    public void setNumeromedecin(int numeroMedecin) {
        this.numeroMedecin = numeroMedecin;
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

    public Rendez_Vous getRendez_vous() {
        return rendez_vous;
    }

    public void setRendez_vous(Rendez_Vous rendez_vous) {
        this.rendez_vous = rendez_vous;
    }

}