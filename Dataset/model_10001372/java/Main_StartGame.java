





import java.util.List;
import java.util.ArrayList;

public class Main_StartGame  {

    private String hand;
    private String deck;
    private String scanner;
    private String player;
    private int handsize;



    public Main_StartGame(
        String hand,        String deck,        String scanner,        String player,        int handsize    ) {
        this.hand = hand;
        this.deck = deck;
        this.scanner = scanner;
        this.player = player;
        this.handsize = handsize;
    }


    public String getHand() {
        return hand;
    }

    public void setHand(String hand) {
        this.hand = hand;
    }
    public String getDeck() {
        return deck;
    }

    public void setDeck(String deck) {
        this.deck = deck;
    }
    public String getScanner() {
        return scanner;
    }

    public void setScanner(String scanner) {
        this.scanner = scanner;
    }
    public String getPlayer() {
        return player;
    }

    public void setPlayer(String player) {
        this.player = player;
    }
    public int getHandsize() {
        return handsize;
    }

    public void setHandsize(int handsize) {
        this.handsize = handsize;
    }


}