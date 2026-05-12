




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class Covoiturage_Trajet  {

    private None destination;
    private int prix;
    private None depart;
    private boolean etat;
    private LocalDate date;
    private int id;





    private Covoiturage_Voiture covoiturage_voiture;




    private List<Covoiturage_Passager> covoiturage_passagers;


    public Covoiturage_Trajet(
        None destination,        int prix,        None depart,        boolean etat,        LocalDate date,        int id    ) {
        this.destination = destination;
        this.prix = prix;
        this.depart = depart;
        this.etat = etat;
        this.date = date;
        this.id = id;
        this.covoiturage_passagers = new ArrayList<>();
    }

    public Covoiturage_Trajet(
        None destination,        int prix,        None depart,        boolean etat,        LocalDate date,        int id        ArrayList<Covoiturage_Passager> covoiturage_passagers    ) {
        this.destination = destination;
        this.prix = prix;
        this.depart = depart;
        this.etat = etat;
        this.date = date;
        this.id = id;
        this.covoiturage_passagers = covoiturage_passagers;
    }

    public None getDestination() {
        return destination;
    }

    public void setDestination(None destination) {
        this.destination = destination;
    }
    public int getPrix() {
        return prix;
    }

    public void setPrix(int prix) {
        this.prix = prix;
    }
    public None getDepart() {
        return depart;
    }

    public void setDepart(None depart) {
        this.depart = depart;
    }
    public boolean getEtat() {
        return etat;
    }

    public void setEtat(boolean etat) {
        this.etat = etat;
    }
    public LocalDate getDate() {
        return date;
    }

    public void setDate(LocalDate date) {
        this.date = date;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public Covoiturage_Voiture getCovoiturage_voiture() {
        return covoiturage_voiture;
    }

    public void setCovoiturage_voiture(Covoiturage_Voiture covoiturage_voiture) {
        this.covoiturage_voiture = covoiturage_voiture;
    }
    public List<Covoiturage_Passager> getCovoiturage_passagers() {
        return covoiturage_passagers;
    }

    public void addCovoiturage_passager(Covoiturage_passager covoiturage_passager) {
        this.covoiturage_passagers.add(covoiturage_passager);
    }

}