





import java.util.List;
import java.util.ArrayList;

public class game_Personne  {

    private String name;





    private game_Interaction game_interaction;




    private game_EntiteLieu game_entitelieu;


    public game_Personne(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public game_Interaction getGame_interaction() {
        return game_interaction;
    }

    public void setGame_interaction(game_Interaction game_interaction) {
        this.game_interaction = game_interaction;
    }
    public game_EntiteLieu getGame_entitelieu() {
        return game_entitelieu;
    }

    public void setGame_entitelieu(game_EntiteLieu game_entitelieu) {
        this.game_entitelieu = game_entitelieu;
    }

}