





import java.util.List;
import java.util.ArrayList;

public class Money  {

    private int money;





    private Player player;


    public Money(
        int money    ) {
        this.money = money;
    }


    public int getMoney() {
        return money;
    }

    public void setMoney(int money) {
        this.money = money;
    }

    public Player getPlayer() {
        return player;
    }

    public void setPlayer(Player player) {
        this.player = player;
    }

}