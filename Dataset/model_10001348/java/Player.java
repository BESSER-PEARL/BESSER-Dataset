





import java.util.List;
import java.util.ArrayList;

public class Player  {

    private None hand;
    private String name;
    private int number;
    private int score;





    private Hand hand;


    public Player(
        None hand,        String name,        int number,        int score    ) {
        this.hand = hand;
        this.name = name;
        this.number = number;
        this.score = score;
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
    public int getNumber() {
        return number;
    }

    public void setNumber(int number) {
        this.number = number;
    }
    public int getScore() {
        return score;
    }

    public void setScore(int score) {
        this.score = score;
    }

    public Hand getHand() {
        return hand;
    }

    public void setHand(Hand hand) {
        this.hand = hand;
    }

}