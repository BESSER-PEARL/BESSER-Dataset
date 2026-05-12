




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class domain_Reservation  {

    private int id;
    private LocalDate dateReservation;
    private int id2;





    private List<domain_Profil> domain_profils;




    private domain_Trajet domain_trajet;


    public domain_Reservation(
        int id,        LocalDate dateReservation,        int id2    ) {
        this.id = id;
        this.dateReservation = dateReservation;
        this.id2 = id2;
        this.domain_profils = new ArrayList<>();
    }

    public domain_Reservation(
        int id,        LocalDate dateReservation,        int id2        ArrayList<domain_Profil> domain_profils    ) {
        this.id = id;
        this.dateReservation = dateReservation;
        this.id2 = id2;
        this.domain_profils = domain_profils;
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
    public int getId2() {
        return id2;
    }

    public void setId2(int id2) {
        this.id2 = id2;
    }

    public List<domain_Profil> getDomain_profils() {
        return domain_profils;
    }

    public void addDomain_profil(Domain_profil domain_profil) {
        this.domain_profils.add(domain_profil);
    }
    public domain_Trajet getDomain_trajet() {
        return domain_trajet;
    }

    public void setDomain_trajet(domain_Trajet domain_trajet) {
        this.domain_trajet = domain_trajet;
    }

}