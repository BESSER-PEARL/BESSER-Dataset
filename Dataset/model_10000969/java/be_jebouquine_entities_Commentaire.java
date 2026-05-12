




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class be_jebouquine_entities_Commentaire  {

    private int idClient;
    private String textCommentaire;
    private int idLivre;
    private LocalDate dateCommentaire;
    private int idCommentaire;





    private be_jebouquine_entities_Client be_jebouquine_entities_client;




    private be_jebouquine_entities_Livre be_jebouquine_entities_livre;


    public be_jebouquine_entities_Commentaire(
        int idClient,        String textCommentaire,        int idLivre,        LocalDate dateCommentaire,        int idCommentaire    ) {
        this.idClient = idClient;
        this.textCommentaire = textCommentaire;
        this.idLivre = idLivre;
        this.dateCommentaire = dateCommentaire;
        this.idCommentaire = idCommentaire;
    }


    public int getIdclient() {
        return idClient;
    }

    public void setIdclient(int idClient) {
        this.idClient = idClient;
    }
    public String getTextcommentaire() {
        return textCommentaire;
    }

    public void setTextcommentaire(String textCommentaire) {
        this.textCommentaire = textCommentaire;
    }
    public int getIdlivre() {
        return idLivre;
    }

    public void setIdlivre(int idLivre) {
        this.idLivre = idLivre;
    }
    public LocalDate getDatecommentaire() {
        return dateCommentaire;
    }

    public void setDatecommentaire(LocalDate dateCommentaire) {
        this.dateCommentaire = dateCommentaire;
    }
    public int getIdcommentaire() {
        return idCommentaire;
    }

    public void setIdcommentaire(int idCommentaire) {
        this.idCommentaire = idCommentaire;
    }

    public be_jebouquine_entities_Client getBe_jebouquine_entities_client() {
        return be_jebouquine_entities_client;
    }

    public void setBe_jebouquine_entities_client(be_jebouquine_entities_Client be_jebouquine_entities_client) {
        this.be_jebouquine_entities_client = be_jebouquine_entities_client;
    }
    public be_jebouquine_entities_Livre getBe_jebouquine_entities_livre() {
        return be_jebouquine_entities_livre;
    }

    public void setBe_jebouquine_entities_livre(be_jebouquine_entities_Livre be_jebouquine_entities_livre) {
        this.be_jebouquine_entities_livre = be_jebouquine_entities_livre;
    }

}