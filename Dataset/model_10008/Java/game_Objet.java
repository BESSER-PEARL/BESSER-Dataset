





import java.util.List;
import java.util.ArrayList;

public class game_Objet extends GameElement {

    private int taille;





    private game_PackObjets game_packobjets;


    public game_Objet(
        int taille    ) {
        super(
        );
        this.taille = taille;
    }


    public int getTaille() {
        return taille;
    }

    public void setTaille(int taille) {
        this.taille = taille;
    }

    public game_PackObjets getGame_packobjets() {
        return game_packobjets;
    }

    public void setGame_packobjets(game_PackObjets game_packobjets) {
        this.game_packobjets = game_packobjets;
    }

}