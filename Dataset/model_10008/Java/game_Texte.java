





import java.util.List;
import java.util.ArrayList;

public class game_Texte  {

    private String contenu;





    private game_Condition game_condition;




    private game_Description game_description;


    public game_Texte(
        String contenu    ) {
        this.contenu = contenu;
    }


    public String getContenu() {
        return contenu;
    }

    public void setContenu(String contenu) {
        this.contenu = contenu;
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

}