





import java.util.List;
import java.util.ArrayList;

public class Voiture  {

    private int places;





    private Utilisateur utilisateur;


    public Voiture(
        int places    ) {
        this.places = places;
    }


    public int getPlaces() {
        return places;
    }

    public void setPlaces(int places) {
        this.places = places;
    }

    public Utilisateur getUtilisateur() {
        return utilisateur;
    }

    public void setUtilisateur(Utilisateur utilisateur) {
        this.utilisateur = utilisateur;
    }

}