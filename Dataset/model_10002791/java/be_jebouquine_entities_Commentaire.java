




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class be_jebouquine_entities_Commentaire  {

    private LocalDate dateCommentaire;
    private String textCommentaire;
    private int idClient;
    private int idCommentaire;
    private int idLivre;



    public be_jebouquine_entities_Commentaire(
        LocalDate dateCommentaire,        String textCommentaire,        int idClient,        int idCommentaire,        int idLivre    ) {
        this.dateCommentaire = dateCommentaire;
        this.textCommentaire = textCommentaire;
        this.idClient = idClient;
        this.idCommentaire = idCommentaire;
        this.idLivre = idLivre;
    }


    public LocalDate getDatecommentaire() {
        return dateCommentaire;
    }

    public void setDatecommentaire(LocalDate dateCommentaire) {
        this.dateCommentaire = dateCommentaire;
    }
    public String getTextcommentaire() {
        return textCommentaire;
    }

    public void setTextcommentaire(String textCommentaire) {
        this.textCommentaire = textCommentaire;
    }
    public int getIdclient() {
        return idClient;
    }

    public void setIdclient(int idClient) {
        this.idClient = idClient;
    }
    public int getIdcommentaire() {
        return idCommentaire;
    }

    public void setIdcommentaire(int idCommentaire) {
        this.idCommentaire = idCommentaire;
    }
    public int getIdlivre() {
        return idLivre;
    }

    public void setIdlivre(int idLivre) {
        this.idLivre = idLivre;
    }


}