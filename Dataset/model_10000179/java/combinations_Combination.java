





import java.util.List;
import java.util.ArrayList;

public class combinations_Combination  {

    private int value;
    private String name;





    private List<classes_Card> classes_cards;


    public combinations_Combination(
        int value,        String name    ) {
        this.value = value;
        this.name = name;
        this.classes_cards = new ArrayList<>();
    }

    public combinations_Combination(
        int value,        String name        ArrayList<classes_Card> classes_cards    ) {
        this.value = value;
        this.name = name;
        this.classes_cards = classes_cards;
    }

    public int getValue() {
        return value;
    }

    public void setValue(int value) {
        this.value = value;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<classes_Card> getClasses_cards() {
        return classes_cards;
    }

    public void addClasses_card(Classes_card classes_card) {
        this.classes_cards.add(classes_card);
    }

}