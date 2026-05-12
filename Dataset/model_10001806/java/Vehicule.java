





import java.util.List;
import java.util.ArrayList;

public class Vehicule  {

    private String standing;
    private int rang;





    private Chauffeur chauffeur;




    private Reservation reservation;


    public Vehicule(
        String standing,        int rang    ) {
        this.standing = standing;
        this.rang = rang;
    }


    public String getStanding() {
        return standing;
    }

    public void setStanding(String standing) {
        this.standing = standing;
    }
    public int getRang() {
        return rang;
    }

    public void setRang(int rang) {
        this.rang = rang;
    }

    public Chauffeur getChauffeur() {
        return chauffeur;
    }

    public void setChauffeur(Chauffeur chauffeur) {
        this.chauffeur = chauffeur;
    }
    public Reservation getReservation() {
        return reservation;
    }

    public void setReservation(Reservation reservation) {
        this.reservation = reservation;
    }

}