





import java.util.List;
import java.util.ArrayList;

public class Player  {

    private String name;
    private int id;
    private None hand;



    public Player(
        String name,        int id,        None hand    ) {
        this.name = name;
        this.id = id;
        this.hand = hand;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    public None getHand() {
        return hand;
    }

    public void setHand(None hand) {
        this.hand = hand;
    }


}