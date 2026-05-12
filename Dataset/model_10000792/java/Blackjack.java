





import java.util.List;
import java.util.ArrayList;

public class Blackjack  {

    private None hand__;
    private int players;
    private int count;
    private String playerName;



    public Blackjack(
        None hand__,        int players,        int count,        String playerName    ) {
        this.hand__ = hand__;
        this.players = players;
        this.count = count;
        this.playerName = playerName;
    }


    public None getHand__() {
        return hand__;
    }

    public void setHand__(None hand__) {
        this.hand__ = hand__;
    }
    public int getPlayers() {
        return players;
    }

    public void setPlayers(int players) {
        this.players = players;
    }
    public int getCount() {
        return count;
    }

    public void setCount(int count) {
        this.count = count;
    }
    public String getPlayername() {
        return playerName;
    }

    public void setPlayername(String playerName) {
        this.playerName = playerName;
    }


}