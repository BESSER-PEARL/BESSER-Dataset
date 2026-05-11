





import java.util.List;
import java.util.ArrayList;

public class game_ComponentData  {

    private String name;





    private game_Type game_type;




    private game_Game game_game;


    public game_ComponentData(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public game_Type getGame_type() {
        return game_type;
    }

    public void setGame_type(game_Type game_type) {
        this.game_type = game_type;
    }
    public game_Game getGame_game() {
        return game_game;
    }

    public void setGame_game(game_Game game_game) {
        this.game_game = game_game;
    }

}