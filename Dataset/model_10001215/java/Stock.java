





import java.util.List;
import java.util.ArrayList;

public class Stock  {

    private None items__;





    private List<Item> items;


    public Stock(
        None items__    ) {
        this.items__ = items__;
        this.items = new ArrayList<>();
    }

    public Stock(
        None items__        ArrayList<Item> items    ) {
        this.items__ = items__;
        this.items = items;
    }

    public None getItems__() {
        return items__;
    }

    public void setItems__(None items__) {
        this.items__ = items__;
    }

    public List<Item> getItems() {
        return items;
    }

    public void addItem(Item item) {
        this.items.add(item);
    }

}