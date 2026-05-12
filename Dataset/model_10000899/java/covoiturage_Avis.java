





import java.util.List;
import java.util.ArrayList;

public class covoiturage_Avis  {

    private int note;
    private String commentaire;
    private int id;





    private covoiturage_Reservations covoiturage_reservations;




    private covoiturage_Personne covoiturage_personne;


    public covoiturage_Avis(
        int note,        String commentaire,        int id    ) {
        this.note = note;
        this.commentaire = commentaire;
        this.id = id;
    }


    public int getNote() {
        return note;
    }

    public void setNote(int note) {
        this.note = note;
    }
    public String getCommentaire() {
        return commentaire;
    }

    public void setCommentaire(String commentaire) {
        this.commentaire = commentaire;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public covoiturage_Reservations getCovoiturage_reservations() {
        return covoiturage_reservations;
    }

    public void setCovoiturage_reservations(covoiturage_Reservations covoiturage_reservations) {
        this.covoiturage_reservations = covoiturage_reservations;
    }
    public covoiturage_Personne getCovoiturage_personne() {
        return covoiturage_personne;
    }

    public void setCovoiturage_personne(covoiturage_Personne covoiturage_personne) {
        this.covoiturage_personne = covoiturage_personne;
    }

}