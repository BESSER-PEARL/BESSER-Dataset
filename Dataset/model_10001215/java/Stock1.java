





import java.util.List;
import java.util.ArrayList;

public class Stock1  {

    private None items__;





    private List<Item1> item1s;


    public Stock1(
        None items__    ) {
        this.items__ = items__;
        this.item1s = new ArrayList<>();
    }

    public Stock1(
        None items__        ArrayList<Item1> item1s    ) {
        this.items__ = items__;
        this.item1s = item1s;
    }

    public None getItems__() {
        return items__;
    }

    public void setItems__(None items__) {
        this.items__ = items__;
    }

    public List<Item1> getItem1s() {
        return item1s;
    }

    public void addItem1(Item1 item1) {
        this.item1s.add(item1);
    }

}