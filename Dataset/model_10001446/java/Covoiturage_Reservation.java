




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class Covoiturage_Reservation  {

    private boolean etat;
    private int id2;
    private int id;
    private LocalDate dateReservation;





    private List<Covoiturage_Passager> covoiturage_passagers;




    private Covoiturage_Trajet covoiturage_trajet;


    public Covoiturage_Reservation(
        boolean etat,        int id2,        int id,        LocalDate dateReservation    ) {
        this.etat = etat;
        this.id2 = id2;
        this.id = id;
        this.dateReservation = dateReservation;
        this.covoiturage_passagers = new ArrayList<>();
    }

    public Covoiturage_Reservation(
        boolean etat,        int id2,        int id,        LocalDate dateReservation        ArrayList<Covoiturage_Passager> covoiturage_passagers    ) {
        this.etat = etat;
        this.id2 = id2;
        this.id = id;
        this.dateReservation = dateReservation;
        this.covoiturage_passagers = covoiturage_passagers;
    }

    public boolean getEtat() {
        return etat;
    }

    public void setEtat(boolean etat) {
        this.etat = etat;
    }
    public int getId2() {
        return id2;
    }

    public void setId2(int id2) {
        this.id2 = id2;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    public LocalDate getDatereservation() {
        return dateReservation;
    }

    public void setDatereservation(LocalDate dateReservation) {
        this.dateReservation = dateReservation;
    }

    public List<Covoiturage_Passager> getCovoiturage_passagers() {
        return covoiturage_passagers;
    }

    public void addCovoiturage_passager(Covoiturage_passager covoiturage_passager) {
        this.covoiturage_passagers.add(covoiturage_passager);
    }
    public Covoiturage_Trajet getCovoiturage_trajet() {
        return covoiturage_trajet;
    }

    public void setCovoiturage_trajet(Covoiturage_Trajet covoiturage_trajet) {
        this.covoiturage_trajet = covoiturage_trajet;
    }

}