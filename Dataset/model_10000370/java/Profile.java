





import java.util.List;
import java.util.ArrayList;

public class Profile  {

    private String username;
    private int money;





    private LoginView loginview;




    private BlackjackGame blackjackgame;




    private Player player;


    public Profile(
        String username,        int money    ) {
        this.username = username;
        this.money = money;
    }


    public String getUsername() {
        return username;
    }

    public void setUsername(String username) {
        this.username = username;
    }
    public int getMoney() {
        return money;
    }

    public void setMoney(int money) {
        this.money = money;
    }

    public LoginView getLoginview() {
        return loginview;
    }

    public void setLoginview(LoginView loginview) {
        this.loginview = loginview;
    }
    public BlackjackGame getBlackjackgame() {
        return blackjackgame;
    }

    public void setBlackjackgame(BlackjackGame blackjackgame) {
        this.blackjackgame = blackjackgame;
    }
    public Player getPlayer() {
        return player;
    }

    public void setPlayer(Player player) {
        this.player = player;
    }

}