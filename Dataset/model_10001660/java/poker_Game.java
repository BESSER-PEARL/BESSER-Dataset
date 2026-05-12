





import java.util.List;
import java.util.ArrayList;

public class poker_Game  {

    private int hand_size;
    private int tryagain;



    public poker_Game(
        int hand_size,        int tryagain    ) {
        this.hand_size = hand_size;
        this.tryagain = tryagain;
    }


    public int getHand_size() {
        return hand_size;
    }

    public void setHand_size(int hand_size) {
        this.hand_size = hand_size;
    }
    public int getTryagain() {
        return tryagain;
    }

    public void setTryagain(int tryagain) {
        this.tryagain = tryagain;
    }


}