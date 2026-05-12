





import java.util.List;
import java.util.ArrayList;

public class Player  {

    private String firstName;





    private Hand hand;




    private BlackJack blackjack;


    public Player(
        String firstName    ) {
        this.firstName = firstName;
    }


    public String getFirstname() {
        return firstName;
    }

    public void setFirstname(String firstName) {
        this.firstName = firstName;
    }

    public Hand getHand() {
        return hand;
    }

    public void setHand(Hand hand) {
        this.hand = hand;
    }
    public BlackJack getBlackjack() {
        return blackjack;
    }

    public void setBlackjack(BlackJack blackjack) {
        this.blackjack = blackjack;
    }

}