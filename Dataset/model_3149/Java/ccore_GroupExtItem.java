





import java.util.List;
import java.util.ArrayList;

public class ccore_GroupExtItem  {






    private ccore_Item ccore_item;




    private List<ccore_Item> ccore_items;


    public ccore_GroupExtItem(
    ) {
        this.ccore_items = new ArrayList<>();
    }

    public ccore_GroupExtItem(
        ArrayList<ccore_Item> ccore_items    ) {
        this.ccore_items = ccore_items;
    }


    public ccore_Item getCcore_item() {
        return ccore_item;
    }

    public void setCcore_item(ccore_Item ccore_item) {
        this.ccore_item = ccore_item;
    }
    public List<ccore_Item> getCcore_items() {
        return ccore_items;
    }

    public void addCcore_item(Ccore_item ccore_item) {
        this.ccore_items.add(ccore_item);
    }

}