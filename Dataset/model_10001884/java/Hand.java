





import java.util.List;
import java.util.ArrayList;

public class Hand  {

    private None player;
    private int id;
    private String cards;
    private None game;





    private Player player;


    public Hand(
        None player,        int id,        String cards,        None game    ) {
        this.player = player;
        this.id = id;
        this.cards = cards;
        this.game = game;
    }


    public None getPlayer() {
        return player;
    }

    public void setPlayer(None player) {
        this.player = player;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    public String getCards() {
        return cards;
    }

    public void setCards(String cards) {
        this.cards = cards;
    }
    public None getGame() {
        return game;
    }

    public void setGame(None game) {
        this.game = game;
    }

    public Player getPlayer() {
        return player;
    }

    public void setPlayer(Player player) {
        this.player = player;
    }

}