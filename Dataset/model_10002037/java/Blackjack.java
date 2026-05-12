





import java.util.List;
import java.util.ArrayList;

public class Blackjack  {

    private String playerName;
    private int players;
    private int count;
    private None hand__;



    public Blackjack(
        String playerName,        int players,        int count,        None hand__    ) {
        this.playerName = playerName;
        this.players = players;
        this.count = count;
        this.hand__ = hand__;
    }


    public String getPlayername() {
        return playerName;
    }

    public void setPlayername(String playerName) {
        this.playerName = playerName;
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
    public None getHand__() {
        return hand__;
    }

    public void setHand__(None hand__) {
        this.hand__ = hand__;
    }


}