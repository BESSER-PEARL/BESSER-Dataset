




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class covoiturage_Reservations  {

    private int id;
    private int prix;
    private LocalDate date;
    private String lieuDeDepose;





    private List<covoiturage_Personne> covoiturage_personnes;


    public covoiturage_Reservations(
        int id,        int prix,        LocalDate date,        String lieuDeDepose    ) {
        this.id = id;
        this.prix = prix;
        this.date = date;
        this.lieuDeDepose = lieuDeDepose;
        this.covoiturage_personnes = new ArrayList<>();
    }

    public covoiturage_Reservations(
        int id,        int prix,        LocalDate date,        String lieuDeDepose        ArrayList<covoiturage_Personne> covoiturage_personnes    ) {
        this.id = id;
        this.prix = prix;
        this.date = date;
        this.lieuDeDepose = lieuDeDepose;
        this.covoiturage_personnes = covoiturage_personnes;
    }

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    public int getPrix() {
        return prix;
    }

    public void setPrix(int prix) {
        this.prix = prix;
    }
    public LocalDate getDate() {
        return date;
    }

    public void setDate(LocalDate date) {
        this.date = date;
    }
    public String getLieudedepose() {
        return lieuDeDepose;
    }

    public void setLieudedepose(String lieuDeDepose) {
        this.lieuDeDepose = lieuDeDepose;
    }

    public List<covoiturage_Personne> getCovoiturage_personnes() {
        return covoiturage_personnes;
    }

    public void addCovoiturage_personne(Covoiturage_personne covoiturage_personne) {
        this.covoiturage_personnes.add(covoiturage_personne);
    }

}