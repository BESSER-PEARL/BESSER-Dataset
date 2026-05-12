





import java.util.List;
import java.util.ArrayList;

public class administrateur  {






    private trajet trajet;




    private List<paiement> paiements;




    private reservation reservation;


    public administrateur(
    ) {
        this.paiements = new ArrayList<>();
    }

    public administrateur(
        ArrayList<paiement> paiements    ) {
        this.paiements = paiements;
    }


    public trajet getTrajet() {
        return trajet;
    }

    public void setTrajet(trajet trajet) {
        this.trajet = trajet;
    }
    public List<paiement> getPaiements() {
        return paiements;
    }

    public void addPaiement(Paiement paiement) {
        this.paiements.add(paiement);
    }
    public reservation getReservation() {
        return reservation;
    }

    public void setReservation(reservation reservation) {
        this.reservation = reservation;
    }

}