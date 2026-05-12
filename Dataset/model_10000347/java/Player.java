





import java.util.List;
import java.util.ArrayList;

public class Player  {

    private None hand;
    private String name;
    private None bank;





    private Hand hand;




    private Poker poker;


    public Player(
        None hand,        String name,        None bank    ) {
        this.hand = hand;
        this.name = name;
        this.bank = bank;
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
    public None getBank() {
        return bank;
    }

    public void setBank(None bank) {
        this.bank = bank;
    }

    public Hand getHand() {
        return hand;
    }

    public void setHand(Hand hand) {
        this.hand = hand;
    }
    public Poker getPoker() {
        return poker;
    }

    public void setPoker(Poker poker) {
        this.poker = poker;
    }

}