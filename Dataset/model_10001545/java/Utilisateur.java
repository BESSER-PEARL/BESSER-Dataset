





import java.util.List;
import java.util.ArrayList;

public class Utilisateur  {

    private String nom;
    private String photoDeProfil;
    private int nbAvis;
    private String score;



    public Utilisateur(
        String nom,        String photoDeProfil,        int nbAvis,        String score    ) {
        this.nom = nom;
        this.photoDeProfil = photoDeProfil;
        this.nbAvis = nbAvis;
        this.score = score;
    }


    public String getNom() {
        return nom;
    }

    public void setNom(String nom) {
        this.nom = nom;
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
    public String getScore() {
        return score;
    }

    public void setScore(String score) {
        this.score = score;
    }


}