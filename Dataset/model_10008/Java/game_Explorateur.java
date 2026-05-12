





import java.util.List;
import java.util.ArrayList;

public class game_Explorateur  {

    private int tailleInventaire;
    private String name;





    private List<game_Connaissance> game_connaissances;




    private game_Game game_game;




    private List<game_PackObjets> game_packobjetss;


    public game_Explorateur(
        int tailleInventaire,        String name    ) {
        this.tailleInventaire = tailleInventaire;
        this.name = name;
        this.game_connaissances = new ArrayList<>();
        this.game_packobjetss = new ArrayList<>();
    }

    public game_Explorateur(
        int tailleInventaire,        String name        ArrayList<game_Connaissance> game_connaissances,        ArrayList<game_PackObjets> game_packobjetss    ) {
        this.tailleInventaire = tailleInventaire;
        this.name = name;
        this.game_connaissances = game_connaissances;
        this.game_packobjetss = game_packobjetss;
    }

    public int getTailleinventaire() {
        return tailleInventaire;
    }

    public void setTailleinventaire(int tailleInventaire) {
        this.tailleInventaire = tailleInventaire;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<game_Connaissance> getGame_connaissances() {
        return game_connaissances;
    }

    public void addGame_connaissance(Game_connaissance game_connaissance) {
        this.game_connaissances.add(game_connaissance);
    }
    public game_Game getGame_game() {
        return game_game;
    }

    public void setGame_game(game_Game game_game) {
        this.game_game = game_game;
    }
    public List<game_PackObjets> getGame_packobjetss() {
        return game_packobjetss;
    }

    public void addGame_packobjets(Game_packobjets game_packobjets) {
        this.game_packobjetss.add(game_packobjets);
    }

}