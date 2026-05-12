





import java.util.List;
import java.util.ArrayList;

public class Croupier  {

    private String main;





    private Blackjack blackjack;


    public Croupier(
        String main    ) {
        this.main = main;
    }


    public String getMain() {
        return main;
    }

    public void setMain(String main) {
        this.main = main;
    }

    public Blackjack getBlackjack() {
        return blackjack;
    }

    public void setBlackjack(Blackjack blackjack) {
        this.blackjack = blackjack;
    }

}