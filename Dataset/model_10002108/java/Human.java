





import java.util.List;
import java.util.ArrayList;

public class Human  {

    private None hand;
    private String name;



    public Human(
        None hand,        String name    ) {
        this.hand = hand;
        this.name = name;
    }


    public None getHand() {
        return hand;
    }

    public void setHand(None hand) {
        this.hand = hand;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}