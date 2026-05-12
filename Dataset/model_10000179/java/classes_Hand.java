





import java.util.List;
import java.util.ArrayList;

public class classes_Hand  {






    private List<classes_Card> classes_cards;


    public classes_Hand(
    ) {
        this.classes_cards = new ArrayList<>();
    }

    public classes_Hand(
        ArrayList<classes_Card> classes_cards    ) {
        this.classes_cards = classes_cards;
    }


    public List<classes_Card> getClasses_cards() {
        return classes_cards;
    }

    public void addClasses_card(Classes_card classes_card) {
        this.classes_cards.add(classes_card);
    }

}