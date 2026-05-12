





import java.util.List;
import java.util.ArrayList;

public class GameLauncher  {

    private None login;
    private None blackjack;



    public GameLauncher(
        None login,        None blackjack    ) {
        this.login = login;
        this.blackjack = blackjack;
    }


    public None getLogin() {
        return login;
    }

    public void setLogin(None login) {
        this.login = login;
    }
    public None getBlackjack() {
        return blackjack;
    }

    public void setBlackjack(None blackjack) {
        this.blackjack = blackjack;
    }


}