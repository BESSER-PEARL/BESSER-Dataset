





import java.util.List;
import java.util.ArrayList;

public class Player  {

    private String name;
    private String hand;



    public Player(
        String name,        String hand    ) {
        this.name = name;
        this.hand = hand;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getHand() {
        return hand;
    }

    public void setHand(String hand) {
        this.hand = hand;
    }


}