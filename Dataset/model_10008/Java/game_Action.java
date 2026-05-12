





import java.util.List;
import java.util.ArrayList;

public class game_Action  {






    private game_Condition game_condition;




    private List<game_Recompense> game_recompenses;




    private game_Description game_description;




    private List<game_PackObjets> game_packobjetss;


    public game_Action(
    ) {
        this.game_recompenses = new ArrayList<>();
        this.game_packobjetss = new ArrayList<>();
    }

    public game_Action(
        ArrayList<game_Recompense> game_recompenses,        ArrayList<game_PackObjets> game_packobjetss    ) {
        this.game_recompenses = game_recompenses;
        this.game_packobjetss = game_packobjetss;
    }


    public game_Condition getGame_condition() {
        return game_condition;
    }

    public void setGame_condition(game_Condition game_condition) {
        this.game_condition = game_condition;
    }
    public List<game_Recompense> getGame_recompenses() {
        return game_recompenses;
    }

    public void addGame_recompense(Game_recompense game_recompense) {
        this.game_recompenses.add(game_recompense);
    }
    public game_Description getGame_description() {
        return game_description;
    }

    public void setGame_description(game_Description game_description) {
        this.game_description = game_description;
    }
    public List<game_PackObjets> getGame_packobjetss() {
        return game_packobjetss;
    }

    public void addGame_packobjets(Game_packobjets game_packobjets) {
        this.game_packobjetss.add(game_packobjets);
    }

}