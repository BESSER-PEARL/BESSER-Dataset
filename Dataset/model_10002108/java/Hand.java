





import java.util.List;
import java.util.ArrayList;

public class Hand  {

    private String cards_6_;





    private Card_Interface card_interface;


    public Hand(
        String cards_6_    ) {
        this.cards_6_ = cards_6_;
    }


    public String getCards_6_() {
        return cards_6_;
    }

    public void setCards_6_(String cards_6_) {
        this.cards_6_ = cards_6_;
    }

    public Card_Interface getCard_interface() {
        return card_interface;
    }

    public void setCard_interface(Card_Interface card_interface) {
        this.card_interface = card_interface;
    }

}