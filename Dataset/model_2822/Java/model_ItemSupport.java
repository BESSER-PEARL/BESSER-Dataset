





import java.util.List;
import java.util.ArrayList;

public class model_ItemSupport  {






    private List<model_Item> model_items;


    public model_ItemSupport(
    ) {
        this.model_items = new ArrayList<>();
    }

    public model_ItemSupport(
        ArrayList<model_Item> model_items    ) {
        this.model_items = model_items;
    }


    public List<model_Item> getModel_items() {
        return model_items;
    }

    public void addModel_item(Model_item model_item) {
        this.model_items.add(model_item);
    }

}