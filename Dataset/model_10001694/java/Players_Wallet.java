





import java.util.List;
import java.util.ArrayList;

public class Players_Wallet  {

    private int balance;





    private Players_Player players_player;


    public Players_Wallet(
        int balance    ) {
        this.balance = balance;
    }


    public int getBalance() {
        return balance;
    }

    public void setBalance(int balance) {
        this.balance = balance;
    }

    public Players_Player getPlayers_player() {
        return players_player;
    }

    public void setPlayers_player(Players_Player players_player) {
        this.players_player = players_player;
    }

}