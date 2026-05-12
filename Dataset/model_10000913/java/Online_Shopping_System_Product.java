





import java.util.List;
import java.util.ArrayList;

public class Online_Shopping_System_Product  {

    private String Name;
    private String Supplier;
    private String ID;





    private List<Online_Shopping_System_Line_item> online_shopping_system_line_items;


    public Online_Shopping_System_Product(
        String Name,        String Supplier,        String ID    ) {
        this.Name = Name;
        this.Supplier = Supplier;
        this.ID = ID;
        this.online_shopping_system_line_items = new ArrayList<>();
    }

    public Online_Shopping_System_Product(
        String Name,        String Supplier,        String ID        ArrayList<Online_Shopping_System_Line_item> online_shopping_system_line_items    ) {
        this.Name = Name;
        this.Supplier = Supplier;
        this.ID = ID;
        this.online_shopping_system_line_items = online_shopping_system_line_items;
    }

    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }
    public String getSupplier() {
        return Supplier;
    }

    public void setSupplier(String Supplier) {
        this.Supplier = Supplier;
    }
    public String getId() {
        return ID;
    }

    public void setId(String ID) {
        this.ID = ID;
    }

    public List<Online_Shopping_System_Line_item> getOnline_shopping_system_line_items() {
        return online_shopping_system_line_items;
    }

    public void addOnline_shopping_system_line_item(Online_shopping_system_line_item online_shopping_system_line_item) {
        this.online_shopping_system_line_items.add(online_shopping_system_line_item);
    }

}