





import java.util.List;
import java.util.ArrayList;

public class blackjack_CardSet  {






    private List<blackjack_Card> blackjack_cards;


    public blackjack_CardSet(
    ) {
        this.blackjack_cards = new ArrayList<>();
    }

    public blackjack_CardSet(
        ArrayList<blackjack_Card> blackjack_cards    ) {
        this.blackjack_cards = blackjack_cards;
    }


    public List<blackjack_Card> getBlackjack_cards() {
        return blackjack_cards;
    }

    public void addBlackjack_card(Blackjack_card blackjack_card) {
        this.blackjack_cards.add(blackjack_card);
    }

}