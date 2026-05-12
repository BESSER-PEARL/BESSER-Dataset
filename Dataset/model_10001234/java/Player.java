





import java.util.List;
import java.util.ArrayList;

public class Player  {

    private None type;
    private None color;





    private GameState gamestate;




    private Dice dice;


    public Player(
        None type,        None color    ) {
        this.type = type;
        this.color = color;
    }


    public None getType() {
        return type;
    }

    public void setType(None type) {
        this.type = type;
    }
    public None getColor() {
        return color;
    }

    public void setColor(None color) {
        this.color = color;
    }

    public GameState getGamestate() {
        return gamestate;
    }

    public void setGamestate(GameState gamestate) {
        this.gamestate = gamestate;
    }
    public Dice getDice() {
        return dice;
    }

    public void setDice(Dice dice) {
        this.dice = dice;
    }

}