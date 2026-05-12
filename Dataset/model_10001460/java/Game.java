





import java.util.List;
import java.util.ArrayList;

public class Game  {

    private None turn_state;





    private Player player;


    public Game(
        None turn_state    ) {
        this.turn_state = turn_state;
    }


    public None getTurn_state() {
        return turn_state;
    }

    public void setTurn_state(None turn_state) {
        this.turn_state = turn_state;
    }

    public Player getPlayer() {
        return player;
    }

    public void setPlayer(Player player) {
        this.player = player;
    }

}