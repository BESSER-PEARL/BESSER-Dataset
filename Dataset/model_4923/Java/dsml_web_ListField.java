





import java.util.List;
import java.util.ArrayList;

public class dsml_web_ListField extends FormElement {






    private List<Item> items;


    public dsml_web_ListField(
    ) {
        super(
        );
        this.items = new ArrayList<>();
    }

    public dsml_web_ListField(
        ArrayList<Item> items    ) {
        this.items = items;
    }


    public List<Item> getItems() {
        return items;
    }

    public void addItem(Item item) {
        this.items.add(item);
    }

}