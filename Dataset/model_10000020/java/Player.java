





import java.util.List;
import java.util.ArrayList;

public class Player  {

    private String name;
    private int score;
    private None hand;
    private int number;





    private Hand hand;


    public Player(
        String name,        int score,        None hand,        int number    ) {
        this.name = name;
        this.score = score;
        this.hand = hand;
        this.number = number;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public int getScore() {
        return score;
    }

    public void setScore(int score) {
        this.score = score;
    }
    public None getHand() {
        return hand;
    }

    public void setHand(None hand) {
        this.hand = hand;
    }
    public int getNumber() {
        return number;
    }

    public void setNumber(int number) {
        this.number = number;
    }

    public Hand getHand() {
        return hand;
    }

    public void setHand(Hand hand) {
        this.hand = hand;
    }

}