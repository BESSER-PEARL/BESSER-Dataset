





import java.util.List;
import java.util.ArrayList;

public class Inventory  {

    private int StoreID;
    private float Quantity;
    private int ItemID;





    private List<Items> itemss;




    private List<Store> stores;


    public Inventory(
        int StoreID,        float Quantity,        int ItemID    ) {
        this.StoreID = StoreID;
        this.Quantity = Quantity;
        this.ItemID = ItemID;
        this.itemss = new ArrayList<>();
        this.stores = new ArrayList<>();
    }

    public Inventory(
        int StoreID,        float Quantity,        int ItemID        ArrayList<Items> itemss,        ArrayList<Store> stores    ) {
        this.StoreID = StoreID;
        this.Quantity = Quantity;
        this.ItemID = ItemID;
        this.itemss = itemss;
        this.stores = stores;
    }

    public int getStoreid() {
        return StoreID;
    }

    public void setStoreid(int StoreID) {
        this.StoreID = StoreID;
    }
    public float getQuantity() {
        return Quantity;
    }

    public void setQuantity(float Quantity) {
        this.Quantity = Quantity;
    }
    public int getItemid() {
        return ItemID;
    }

    public void setItemid(int ItemID) {
        this.ItemID = ItemID;
    }

    public List<Items> getItemss() {
        return itemss;
    }

    public void addItems(Items items) {
        this.itemss.add(items);
    }
    public List<Store> getStores() {
        return stores;
    }

    public void addStore(Store store) {
        this.stores.add(store);
    }

}