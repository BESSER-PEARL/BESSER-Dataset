





import java.util.List;
import java.util.ArrayList;

public class Dice  {

    private int value;





    private Player player;


    public Dice(
        int value    ) {
        this.value = value;
    }


    public int getValue() {
        return value;
    }

    public void setValue(int value) {
        this.value = value;
    }

    public Player getPlayer() {
        return player;
    }

    public void setPlayer(Player player) {
        this.player = player;
    }

}