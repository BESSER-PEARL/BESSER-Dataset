





import java.util.List;
import java.util.ArrayList;

public class players_Player  {

    private None hand;
    private boolean hasFolded;
    private int curentChips;



    public players_Player(
        None hand,        boolean hasFolded,        int curentChips    ) {
        this.hand = hand;
        this.hasFolded = hasFolded;
        this.curentChips = curentChips;
    }


    public None getHand() {
        return hand;
    }

    public void setHand(None hand) {
        this.hand = hand;
    }
    public boolean getHasfolded() {
        return hasFolded;
    }

    public void setHasfolded(boolean hasFolded) {
        this.hasFolded = hasFolded;
    }
    public int getCurentchips() {
        return curentChips;
    }

    public void setCurentchips(int curentChips) {
        this.curentChips = curentChips;
    }


}