





import java.util.List;
import java.util.ArrayList;

public class GameState  {






    private Menu menu;




    private GameEngine gameengine;




    private Player player;


    public GameState(
    ) {
    }



    public Menu getMenu() {
        return menu;
    }

    public void setMenu(Menu menu) {
        this.menu = menu;
    }
    public GameEngine getGameengine() {
        return gameengine;
    }

    public void setGameengine(GameEngine gameengine) {
        this.gameengine = gameengine;
    }
    public Player getPlayer() {
        return player;
    }

    public void setPlayer(Player player) {
        this.player = player;
    }

}