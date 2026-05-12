





import java.util.List;
import java.util.ArrayList;

public class Commentaire  {

    private String commentaire;
    private None auteur;





    private AvisGlobal avisglobal;


    public Commentaire(
        String commentaire,        None auteur    ) {
        this.commentaire = commentaire;
        this.auteur = auteur;
    }


    public String getCommentaire() {
        return commentaire;
    }

    public void setCommentaire(String commentaire) {
        this.commentaire = commentaire;
    }
    public None getAuteur() {
        return auteur;
    }

    public void setAuteur(None auteur) {
        this.auteur = auteur;
    }

    public AvisGlobal getAvisglobal() {
        return avisglobal;
    }

    public void setAvisglobal(AvisGlobal avisglobal) {
        this.avisglobal = avisglobal;
    }

}