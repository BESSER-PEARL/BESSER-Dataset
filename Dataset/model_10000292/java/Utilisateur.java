





import java.util.List;
import java.util.ArrayList;

public class Utilisateur  {

    private String score;
    private String photoDeProfil;
    private int nbAvis;
    private String nom;



    public Utilisateur(
        String score,        String photoDeProfil,        int nbAvis,        String nom    ) {
        this.score = score;
        this.photoDeProfil = photoDeProfil;
        this.nbAvis = nbAvis;
        this.nom = nom;
    }


    public String getScore() {
        return score;
    }

    public void setScore(String score) {
        this.score = score;
    }
    public String getPhotodeprofil() {
        return photoDeProfil;
    }

    public void setPhotodeprofil(String photoDeProfil) {
        this.photoDeProfil = photoDeProfil;
    }
    public int getNbavis() {
        return nbAvis;
    }

    public void setNbavis(int nbAvis) {
        this.nbAvis = nbAvis;
    }
    public String getNom() {
        return nom;
    }

    public void setNom(String nom) {
        this.nom = nom;
    }


}