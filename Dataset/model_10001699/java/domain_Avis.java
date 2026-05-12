





import java.util.List;
import java.util.ArrayList;

public class domain_Avis  {

    private String commentaire;
    private int id;
    private int note;





    private domain_Profil domain_profil;




    private domain_Trajet domain_trajet;


    public domain_Avis(
        String commentaire,        int id,        int note    ) {
        this.commentaire = commentaire;
        this.id = id;
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
    public int getNote() {
        return note;
    }

    public void setNote(int note) {
        this.note = note;
    }

    public domain_Profil getDomain_profil() {
        return domain_profil;
    }

    public void setDomain_profil(domain_Profil domain_profil) {
        this.domain_profil = domain_profil;
    }
    public domain_Trajet getDomain_trajet() {
        return domain_trajet;
    }

    public void setDomain_trajet(domain_Trajet domain_trajet) {
        this.domain_trajet = domain_trajet;
    }

}