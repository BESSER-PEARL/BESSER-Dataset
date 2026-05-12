





import java.util.List;
import java.util.ArrayList;

public class Utilisateur  {

    private int nbAvis;
    private String photoDeProfil;
    private String score;
    private String nom;



    public Utilisateur(
        int nbAvis,        String photoDeProfil,        String score,        String nom    ) {
        this.nbAvis = nbAvis;
        this.photoDeProfil = photoDeProfil;
        this.score = score;
        this.nom = nom;
    }


    public int getNbavis() {
        return nbAvis;
    }

    public void setNbavis(int nbAvis) {
        this.nbAvis = nbAvis;
    }
    public String getPhotodeprofil() {
        return photoDeProfil;
    }

    public void setPhotodeprofil(String photoDeProfil) {
        this.photoDeProfil = photoDeProfil;
    }
    public String getScore() {
        return score;
    }

    public void setScore(String score) {
        this.score = score;
    }
    public String getNom() {
        return nom;
    }

    public void setNom(String nom) {
        this.nom = nom;
    }


}