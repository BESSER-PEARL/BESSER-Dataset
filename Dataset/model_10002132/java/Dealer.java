





import java.util.List;
import java.util.ArrayList;

public class Dealer  {

    private String firstName;





    private BlackJack blackjack;


    public Dealer(
        String firstName    ) {
        this.firstName = firstName;
    }


    public String getFirstname() {
        return firstName;
    }

    public void setFirstname(String firstName) {
        this.firstName = firstName;
    }

    public BlackJack getBlackjack() {
        return blackjack;
    }

    public void setBlackjack(BlackJack blackjack) {
        this.blackjack = blackjack;
    }

}