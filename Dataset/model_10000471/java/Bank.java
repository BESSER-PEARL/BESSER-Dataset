





import java.util.List;
import java.util.ArrayList;

public class Bank  {

    private String total;





    private Player player;


    public Bank(
        String total    ) {
        this.total = total;
    }


    public String getTotal() {
        return total;
    }

    public void setTotal(String total) {
        this.total = total;
    }

    public Player getPlayer() {
        return player;
    }

    public void setPlayer(Player player) {
        this.player = player;
    }

}