




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class domain_Trajet  {

    private int id;
    private None destination;
    private int prix;
    private None depart;
    private LocalDate date;





    private List<domain_Profil> domain_profils;


    public domain_Trajet(
        int id,        None destination,        int prix,        None depart,        LocalDate date    ) {
        this.id = id;
        this.destination = destination;
        this.prix = prix;
        this.depart = depart;
        this.date = date;
        this.domain_profils = new ArrayList<>();
    }

    public domain_Trajet(
        int id,        None destination,        int prix,        None depart,        LocalDate date        ArrayList<domain_Profil> domain_profils    ) {
        this.id = id;
        this.destination = destination;
        this.prix = prix;
        this.depart = depart;
        this.date = date;
        this.domain_profils = domain_profils;
    }

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
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
    public LocalDate getDate() {
        return date;
    }

    public void setDate(LocalDate date) {
        this.date = date;
    }

    public List<domain_Profil> getDomain_profils() {
        return domain_profils;
    }

    public void addDomain_profil(Domain_profil domain_profil) {
        this.domain_profils.add(domain_profil);
    }

}