





import java.util.List;
import java.util.ArrayList;

public class collection_ItemsCollection  {






    private collection_DataSet collection_dataset;




    private List<collection_Item> collection_items;


    public collection_ItemsCollection(
    ) {
        this.collection_items = new ArrayList<>();
    }

    public collection_ItemsCollection(
        ArrayList<collection_Item> collection_items    ) {
        this.collection_items = collection_items;
    }


    public collection_DataSet getCollection_dataset() {
        return collection_dataset;
    }

    public void setCollection_dataset(collection_DataSet collection_dataset) {
        this.collection_dataset = collection_dataset;
    }
    public List<collection_Item> getCollection_items() {
        return collection_items;
    }

    public void addCollection_item(Collection_item collection_item) {
        this.collection_items.add(collection_item);
    }

}