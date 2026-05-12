





import java.util.List;
import java.util.ArrayList;

public class poker_Game  {

    private int tryagain;
    private int hand_size;



    public poker_Game(
        int tryagain,        int hand_size    ) {
        this.tryagain = tryagain;
        this.hand_size = hand_size;
    }


    public int getTryagain() {
        return tryagain;
    }

    public void setTryagain(int tryagain) {
        this.tryagain = tryagain;
    }
    public int getHand_size() {
        return hand_size;
    }

    public void setHand_size(int hand_size) {
        this.hand_size = hand_size;
    }


}