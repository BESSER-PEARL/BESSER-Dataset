





import java.util.List;
import java.util.ArrayList;

public class game_Ranker  {

    private int highValue;
    private None hand;



    public game_Ranker(
        int highValue,        None hand    ) {
        this.highValue = highValue;
        this.hand = hand;
    }


    public int getHighvalue() {
        return highValue;
    }

    public void setHighvalue(int highValue) {
        this.highValue = highValue;
    }
    public None getHand() {
        return hand;
    }

    public void setHand(None hand) {
        this.hand = hand;
    }


}