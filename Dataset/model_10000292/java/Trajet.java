





import java.util.List;
import java.util.ArrayList;

public class Trajet  {

    private int prix;
    private String description;
    private String date;
    private int placesRestantes;
    private None depart;
    private None destination;





    private Utilisateur utilisateur;


    public Trajet(
        int prix,        String description,        String date,        int placesRestantes,        None depart,        None destination    ) {
        this.prix = prix;
        this.description = description;
        this.date = date;
        this.placesRestantes = placesRestantes;
        this.depart = depart;
        this.destination = destination;
    }


    public int getPrix() {
        return prix;
    }

    public void setPrix(int prix) {
        this.prix = prix;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public String getDate() {
        return date;
    }

    public void setDate(String date) {
        this.date = date;
    }
    public int getPlacesrestantes() {
        return placesRestantes;
    }

    public void setPlacesrestantes(int placesRestantes) {
        this.placesRestantes = placesRestantes;
    }
    public None getDepart() {
        return depart;
    }

    public void setDepart(None depart) {
        this.depart = depart;
    }
    public None getDestination() {
        return destination;
    }

    public void setDestination(None destination) {
        this.destination = destination;
    }

    public Utilisateur getUtilisateur() {
        return utilisateur;
    }

    public void setUtilisateur(Utilisateur utilisateur) {
        this.utilisateur = utilisateur;
    }

}