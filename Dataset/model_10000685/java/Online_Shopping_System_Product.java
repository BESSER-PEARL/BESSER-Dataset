





import java.util.List;
import java.util.ArrayList;

public class Online_Shopping_System_Product  {

    private String Supplier;
    private String ID;
    private String Name;





    private List<Online_Shopping_System_Line_item> online_shopping_system_line_items;


    public Online_Shopping_System_Product(
        String Supplier,        String ID,        String Name    ) {
        this.Supplier = Supplier;
        this.ID = ID;
        this.Name = Name;
        this.online_shopping_system_line_items = new ArrayList<>();
    }

    public Online_Shopping_System_Product(
        String Supplier,        String ID,        String Name        ArrayList<Online_Shopping_System_Line_item> online_shopping_system_line_items    ) {
        this.Supplier = Supplier;
        this.ID = ID;
        this.Name = Name;
        this.online_shopping_system_line_items = online_shopping_system_line_items;
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
    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }

    public List<Online_Shopping_System_Line_item> getOnline_shopping_system_line_items() {
        return online_shopping_system_line_items;
    }

    public void addOnline_shopping_system_line_item(Online_shopping_system_line_item online_shopping_system_line_item) {
        this.online_shopping_system_line_items.add(online_shopping_system_line_item);
    }

}