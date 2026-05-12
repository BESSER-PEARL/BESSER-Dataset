





import java.util.List;
import java.util.ArrayList;

public class game_GameElement  {

    private String name;





    private game_Game game_game;


    public game_GameElement(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public game_Game getGame_game() {
        return game_game;
    }

    public void setGame_game(game_Game game_game) {
        this.game_game = game_game;
    }

}