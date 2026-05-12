





import java.util.List;
import java.util.ArrayList;

public class Player  {

    private None game;
    private String name;
    private int id;
    private None hand;
    private String cards;





    private Game game;


    public Player(
        None game,        String name,        int id,        None hand,        String cards    ) {
        this.game = game;
        this.name = name;
        this.id = id;
        this.hand = hand;
        this.cards = cards;
    }


    public None getGame() {
        return game;
    }

    public void setGame(None game) {
        this.game = game;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    public None getHand() {
        return hand;
    }

    public void setHand(None hand) {
        this.hand = hand;
    }
    public String getCards() {
        return cards;
    }

    public void setCards(String cards) {
        this.cards = cards;
    }

    public Game getGame() {
        return game;
    }

    public void setGame(Game game) {
        this.game = game;
    }

}