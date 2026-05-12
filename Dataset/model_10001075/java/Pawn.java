





import java.util.List;
import java.util.ArrayList;

public class Pawn  {

    private int position;
    private None color;





    private Player player;


    public Pawn(
        int position,        None color    ) {
        this.position = position;
        this.color = color;
    }


    public int getPosition() {
        return position;
    }

    public void setPosition(int position) {
        this.position = position;
    }
    public None getColor() {
        return color;
    }

    public void setColor(None color) {
        this.color = color;
    }

    public Player getPlayer() {
        return player;
    }

    public void setPlayer(Player player) {
        this.player = player;
    }

}