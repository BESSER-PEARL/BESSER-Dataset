





import java.util.List;
import java.util.ArrayList;

public class ordersystem_Product  {

    private float price;
    private String sku;
    private String name;





    private ordersystem_LineItem ordersystem_lineitem;




    private ordersystem_InventoryItem ordersystem_inventoryitem;


    public ordersystem_Product(
        float price,        String sku,        String name    ) {
        this.price = price;
        this.sku = sku;
        this.name = name;
    }


    public float getPrice() {
        return price;
    }

    public void setPrice(float price) {
        this.price = price;
    }
    public String getSku() {
        return sku;
    }

    public void setSku(String sku) {
        this.sku = sku;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public ordersystem_LineItem getOrdersystem_lineitem() {
        return ordersystem_lineitem;
    }

    public void setOrdersystem_lineitem(ordersystem_LineItem ordersystem_lineitem) {
        this.ordersystem_lineitem = ordersystem_lineitem;
    }
    public ordersystem_InventoryItem getOrdersystem_inventoryitem() {
        return ordersystem_inventoryitem;
    }

    public void setOrdersystem_inventoryitem(ordersystem_InventoryItem ordersystem_inventoryitem) {
        this.ordersystem_inventoryitem = ordersystem_inventoryitem;
    }

}