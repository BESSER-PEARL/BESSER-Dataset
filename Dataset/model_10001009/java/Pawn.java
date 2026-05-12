





import java.util.List;
import java.util.ArrayList;

public class Pawn  {

    private None color;
    private int position;





    private Player player;


    public Pawn(
        None color,        int position    ) {
        this.color = color;
        this.position = position;
    }


    public None getColor() {
        return color;
    }

    public void setColor(None color) {
        this.color = color;
    }
    public int getPosition() {
        return position;
    }

    public void setPosition(int position) {
        this.position = position;
    }

    public Player getPlayer() {
        return player;
    }

    public void setPlayer(Player player) {
        this.player = player;
    }

}