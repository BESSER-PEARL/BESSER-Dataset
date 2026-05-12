





import java.util.List;
import java.util.ArrayList;

public class game_Choix  {

    private String name;





    private List<game_Action> game_actions;




    private game_Interaction game_interaction;




    private game_Interaction game_interaction;




    private game_Interaction game_interaction;




    private game_Condition game_condition;




    private game_Description game_description;




    private game_Action game_action;


    public game_Choix(
        String name    ) {
        this.name = name;
        this.game_actions = new ArrayList<>();
    }

    public game_Choix(
        String name        ArrayList<game_Action> game_actions    ) {
        this.name = name;
        this.game_actions = game_actions;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<game_Action> getGame_actions() {
        return game_actions;
    }

    public void addGame_action(Game_action game_action) {
        this.game_actions.add(game_action);
    }
    public game_Interaction getGame_interaction() {
        return game_interaction;
    }

    public void setGame_interaction(game_Interaction game_interaction) {
        this.game_interaction = game_interaction;
    }
    public game_Interaction getGame_interaction() {
        return game_interaction;
    }

    public void setGame_interaction(game_Interaction game_interaction) {
        this.game_interaction = game_interaction;
    }
    public game_Interaction getGame_interaction() {
        return game_interaction;
    }

    public void setGame_interaction(game_Interaction game_interaction) {
        this.game_interaction = game_interaction;
    }
    public game_Condition getGame_condition() {
        return game_condition;
    }

    public void setGame_condition(game_Condition game_condition) {
        this.game_condition = game_condition;
    }
    public game_Description getGame_description() {
        return game_description;
    }

    public void setGame_description(game_Description game_description) {
        this.game_description = game_description;
    }
    public game_Action getGame_action() {
        return game_action;
    }

    public void setGame_action(game_Action game_action) {
        this.game_action = game_action;
    }

}