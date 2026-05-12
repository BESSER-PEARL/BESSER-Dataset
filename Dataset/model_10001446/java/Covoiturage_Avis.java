





import java.util.List;
import java.util.ArrayList;

public class Covoiturage_Avis  {

    private int id;
    private String commentaire;
    private int note;





    private Covoiturage_Passager covoiturage_passager;




    private Covoiturage_Trajet covoiturage_trajet;


    public Covoiturage_Avis(
        int id,        String commentaire,        int note    ) {
        this.id = id;
        this.commentaire = commentaire;
        this.note = note;
    }


    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    public String getCommentaire() {
        return commentaire;
    }

    public void setCommentaire(String commentaire) {
        this.commentaire = commentaire;
    }
    public int getNote() {
        return note;
    }

    public void setNote(int note) {
        this.note = note;
    }

    public Covoiturage_Passager getCovoiturage_passager() {
        return covoiturage_passager;
    }

    public void setCovoiturage_passager(Covoiturage_Passager covoiturage_passager) {
        this.covoiturage_passager = covoiturage_passager;
    }
    public Covoiturage_Trajet getCovoiturage_trajet() {
        return covoiturage_trajet;
    }

    public void setCovoiturage_trajet(Covoiturage_Trajet covoiturage_trajet) {
        this.covoiturage_trajet = covoiturage_trajet;
    }

}