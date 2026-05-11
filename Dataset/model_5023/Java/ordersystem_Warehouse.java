





import java.util.List;
import java.util.ArrayList;

public class ordersystem_Warehouse  {

    private String name;





    private ordersystem_InventoryItem ordersystem_inventoryitem;




    private ordersystem_OrderSystem ordersystem_ordersystem;




    private List<ordersystem_InventoryItem> ordersystem_inventoryitems;




    private ordersystem_Address ordersystem_address;




    private ordersystem_OrderSystem ordersystem_ordersystem;


    public ordersystem_Warehouse(
        String name    ) {
        this.name = name;
        this.ordersystem_inventoryitems = new ArrayList<>();
    }

    public ordersystem_Warehouse(
        String name        ArrayList<ordersystem_InventoryItem> ordersystem_inventoryitems    ) {
        this.name = name;
        this.ordersystem_inventoryitems = ordersystem_inventoryitems;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public ordersystem_InventoryItem getOrdersystem_inventoryitem() {
        return ordersystem_inventoryitem;
    }

    public void setOrdersystem_inventoryitem(ordersystem_InventoryItem ordersystem_inventoryitem) {
        this.ordersystem_inventoryitem = ordersystem_inventoryitem;
    }
    public ordersystem_OrderSystem getOrdersystem_ordersystem() {
        return ordersystem_ordersystem;
    }

    public void setOrdersystem_ordersystem(ordersystem_OrderSystem ordersystem_ordersystem) {
        this.ordersystem_ordersystem = ordersystem_ordersystem;
    }
    public List<ordersystem_InventoryItem> getOrdersystem_inventoryitems() {
        return ordersystem_inventoryitems;
    }

    public void addOrdersystem_inventoryitem(Ordersystem_inventoryitem ordersystem_inventoryitem) {
        this.ordersystem_inventoryitems.add(ordersystem_inventoryitem);
    }
    public ordersystem_Address getOrdersystem_address() {
        return ordersystem_address;
    }

    public void setOrdersystem_address(ordersystem_Address ordersystem_address) {
        this.ordersystem_address = ordersystem_address;
    }
    public ordersystem_OrderSystem getOrdersystem_ordersystem() {
        return ordersystem_ordersystem;
    }

    public void setOrdersystem_ordersystem(ordersystem_OrderSystem ordersystem_ordersystem) {
        this.ordersystem_ordersystem = ordersystem_ordersystem;
    }

}