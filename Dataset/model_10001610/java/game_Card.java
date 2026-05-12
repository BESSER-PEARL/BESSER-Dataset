





import java.util.List;
import java.util.ArrayList;

public class game_Card  {

    private String name;
    private String suit;





    private game_Deck game_deck;


    public game_Card(
        String name,        String suit    ) {
        this.name = name;
        this.suit = suit;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getSuit() {
        return suit;
    }

    public void setSuit(String suit) {
        this.suit = suit;
    }

    public game_Deck getGame_deck() {
        return game_deck;
    }

    public void setGame_deck(game_Deck game_deck) {
        this.game_deck = game_deck;
    }

}