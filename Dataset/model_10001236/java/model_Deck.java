





import java.util.List;
import java.util.ArrayList;

public class model_Deck  {






    private List<model_Card> model_cards;




    private model_Dealer model_dealer;


    public model_Deck(
    ) {
        this.model_cards = new ArrayList<>();
    }

    public model_Deck(
        ArrayList<model_Card> model_cards    ) {
        this.model_cards = model_cards;
    }


    public List<model_Card> getModel_cards() {
        return model_cards;
    }

    public void addModel_card(Model_card model_card) {
        this.model_cards.add(model_card);
    }
    public model_Dealer getModel_dealer() {
        return model_dealer;
    }

    public void setModel_dealer(model_Dealer model_dealer) {
        this.model_dealer = model_dealer;
    }

}