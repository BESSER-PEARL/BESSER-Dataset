





import java.util.List;
import java.util.ArrayList;

public class game_Chemin extends GameElement {






    private game_Lieu game_lieu;




    private List<game_PackObjets> game_packobjetss;




    private game_Lieu game_lieu;




    private game_Lieu game_lieu;


    public game_Chemin(
    ) {
        super(
        );
        this.game_packobjetss = new ArrayList<>();
    }

    public game_Chemin(
        ArrayList<game_PackObjets> game_packobjetss    ) {
        this.game_packobjetss = game_packobjetss;
    }


    public game_Lieu getGame_lieu() {
        return game_lieu;
    }

    public void setGame_lieu(game_Lieu game_lieu) {
        this.game_lieu = game_lieu;
    }
    public List<game_PackObjets> getGame_packobjetss() {
        return game_packobjetss;
    }

    public void addGame_packobjets(Game_packobjets game_packobjets) {
        this.game_packobjetss.add(game_packobjets);
    }
    public game_Lieu getGame_lieu() {
        return game_lieu;
    }

    public void setGame_lieu(game_Lieu game_lieu) {
        this.game_lieu = game_lieu;
    }
    public game_Lieu getGame_lieu() {
        return game_lieu;
    }

    public void setGame_lieu(game_Lieu game_lieu) {
        this.game_lieu = game_lieu;
    }

}