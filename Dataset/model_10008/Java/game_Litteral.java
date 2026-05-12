





import java.util.List;
import java.util.ArrayList;

public class game_Litteral  {

    private int quantite;
    private String operateur;





    private game_Connaissance game_connaissance;




    private game_Objet game_objet;


    public game_Litteral(
        int quantite,        String operateur    ) {
        this.quantite = quantite;
        this.operateur = operateur;
    }


    public int getQuantite() {
        return quantite;
    }

    public void setQuantite(int quantite) {
        this.quantite = quantite;
    }
    public String getOperateur() {
        return operateur;
    }

    public void setOperateur(String operateur) {
        this.operateur = operateur;
    }

    public game_Connaissance getGame_connaissance() {
        return game_connaissance;
    }

    public void setGame_connaissance(game_Connaissance game_connaissance) {
        this.game_connaissance = game_connaissance;
    }
    public game_Objet getGame_objet() {
        return game_objet;
    }

    public void setGame_objet(game_Objet game_objet) {
        this.game_objet = game_objet;
    }

}