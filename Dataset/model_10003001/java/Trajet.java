





import java.util.List;
import java.util.ArrayList;

public class Trajet  {

    private int placesRestantes;
    private String description;
    private int prix;
    private String date;
    private None destination;
    private None depart;





    private Utilisateur utilisateur;


    public Trajet(
        int placesRestantes,        String description,        int prix,        String date,        None destination,        None depart    ) {
        this.placesRestantes = placesRestantes;
        this.description = description;
        this.prix = prix;
        this.date = date;
        this.destination = destination;
        this.depart = depart;
    }


    public int getPlacesrestantes() {
        return placesRestantes;
    }

    public void setPlacesrestantes(int placesRestantes) {
        this.placesRestantes = placesRestantes;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public int getPrix() {
        return prix;
    }

    public void setPrix(int prix) {
        this.prix = prix;
    }
    public String getDate() {
        return date;
    }

    public void setDate(String date) {
        this.date = date;
    }
    public None getDestination() {
        return destination;
    }

    public void setDestination(None destination) {
        this.destination = destination;
    }
    public None getDepart() {
        return depart;
    }

    public void setDepart(None depart) {
        this.depart = depart;
    }

    public Utilisateur getUtilisateur() {
        return utilisateur;
    }

    public void setUtilisateur(Utilisateur utilisateur) {
        this.utilisateur = utilisateur;
    }

}