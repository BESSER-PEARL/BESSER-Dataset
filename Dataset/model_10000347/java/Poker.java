





import java.util.List;
import java.util.ArrayList;

public class Poker  {

    private None player2;
    private None dealer;
    private None player1;



    public Poker(
        None player2,        None dealer,        None player1    ) {
        this.player2 = player2;
        this.dealer = dealer;
        this.player1 = player1;
    }


    public None getPlayer2() {
        return player2;
    }

    public void setPlayer2(None player2) {
        this.player2 = player2;
    }
    public None getDealer() {
        return dealer;
    }

    public void setDealer(None dealer) {
        this.dealer = dealer;
    }
    public None getPlayer1() {
        return player1;
    }

    public void setPlayer1(None player1) {
        this.player1 = player1;
    }


}