





import java.util.List;
import java.util.ArrayList;

public class Profile  {

    private int money;
    private String username;





    private Player player;




    private BlackjackGame blackjackgame;


    public Profile(
        int money,        String username    ) {
        this.money = money;
        this.username = username;
    }


    public int getMoney() {
        return money;
    }

    public void setMoney(int money) {
        this.money = money;
    }
    public String getUsername() {
        return username;
    }

    public void setUsername(String username) {
        this.username = username;
    }

    public Player getPlayer() {
        return player;
    }

    public void setPlayer(Player player) {
        this.player = player;
    }
    public BlackjackGame getBlackjackgame() {
        return blackjackgame;
    }

    public void setBlackjackgame(BlackjackGame blackjackgame) {
        this.blackjackgame = blackjackgame;
    }

}