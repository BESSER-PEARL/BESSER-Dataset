





import java.util.List;
import java.util.ArrayList;

public class Game  {

    private None deck;
    private None board;
    private String scan;



    public Game(
        None deck,        None board,        String scan    ) {
        this.deck = deck;
        this.board = board;
        this.scan = scan;
    }


    public None getDeck() {
        return deck;
    }

    public void setDeck(None deck) {
        this.deck = deck;
    }
    public None getBoard() {
        return board;
    }

    public void setBoard(None board) {
        this.board = board;
    }
    public String getScan() {
        return scan;
    }

    public void setScan(String scan) {
        this.scan = scan;
    }


}