





import java.util.List;
import java.util.ArrayList;

public class model_Player  {






    private model_Game model_game;




    private model_Observer_Interface model_observer_interface;




    private List<model_Card> model_cards;


    public model_Player(
    ) {
        this.model_cards = new ArrayList<>();
    }

    public model_Player(
        ArrayList<model_Card> model_cards    ) {
        this.model_cards = model_cards;
    }


    public model_Game getModel_game() {
        return model_game;
    }

    public void setModel_game(model_Game model_game) {
        this.model_game = model_game;
    }
    public model_Observer_Interface getModel_observer_interface() {
        return model_observer_interface;
    }

    public void setModel_observer_interface(model_Observer_Interface model_observer_interface) {
        this.model_observer_interface = model_observer_interface;
    }
    public List<model_Card> getModel_cards() {
        return model_cards;
    }

    public void addModel_card(Model_card model_card) {
        this.model_cards.add(model_card);
    }

}