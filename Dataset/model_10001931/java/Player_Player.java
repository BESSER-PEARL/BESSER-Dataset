





import java.util.List;
import java.util.ArrayList;

public class Player_Player  {

    private None status;
    private None chips;





    private List<Cards_Card> cards_cards;


    public Player_Player(
        None status,        None chips    ) {
        this.status = status;
        this.chips = chips;
        this.cards_cards = new ArrayList<>();
    }

    public Player_Player(
        None status,        None chips        ArrayList<Cards_Card> cards_cards    ) {
        this.status = status;
        this.chips = chips;
        this.cards_cards = cards_cards;
    }

    public None getStatus() {
        return status;
    }

    public void setStatus(None status) {
        this.status = status;
    }
    public None getChips() {
        return chips;
    }

    public void setChips(None chips) {
        this.chips = chips;
    }

    public List<Cards_Card> getCards_cards() {
        return cards_cards;
    }

    public void addCards_card(Cards_card cards_card) {
        this.cards_cards.add(cards_card);
    }

}