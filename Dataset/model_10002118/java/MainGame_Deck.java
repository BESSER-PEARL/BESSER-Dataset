





import java.util.List;
import java.util.ArrayList;

public class MainGame_Deck  {

    private String Cards;





    private List<Cards_Card> cards_cards;




    private MainGame_Main maingame_main;


    public MainGame_Deck(
        String Cards    ) {
        this.Cards = Cards;
        this.cards_cards = new ArrayList<>();
    }

    public MainGame_Deck(
        String Cards        ArrayList<Cards_Card> cards_cards    ) {
        this.Cards = Cards;
        this.cards_cards = cards_cards;
    }

    public String getCards() {
        return Cards;
    }

    public void setCards(String Cards) {
        this.Cards = Cards;
    }

    public List<Cards_Card> getCards_cards() {
        return cards_cards;
    }

    public void addCards_card(Cards_card cards_card) {
        this.cards_cards.add(cards_card);
    }
    public MainGame_Main getMaingame_main() {
        return maingame_main;
    }

    public void setMaingame_main(MainGame_Main maingame_main) {
        this.maingame_main = maingame_main;
    }

}