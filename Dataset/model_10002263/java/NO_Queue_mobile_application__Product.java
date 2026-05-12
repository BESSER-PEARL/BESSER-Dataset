





import java.util.List;
import java.util.ArrayList;

public class NO_Queue_mobile_application__Product  {

    private String Supplier;
    private String Name;
    private String ID;





    private List<NO_Queue_mobile_application__Line_item> no_queue_mobile_application__line_items;


    public NO_Queue_mobile_application__Product(
        String Supplier,        String Name,        String ID    ) {
        this.Supplier = Supplier;
        this.Name = Name;
        this.ID = ID;
        this.no_queue_mobile_application__line_items = new ArrayList<>();
    }

    public NO_Queue_mobile_application__Product(
        String Supplier,        String Name,        String ID        ArrayList<NO_Queue_mobile_application__Line_item> no_queue_mobile_application__line_items    ) {
        this.Supplier = Supplier;
        this.Name = Name;
        this.ID = ID;
        this.no_queue_mobile_application__line_items = no_queue_mobile_application__line_items;
    }

    public String getSupplier() {
        return Supplier;
    }

    public void setSupplier(String Supplier) {
        this.Supplier = Supplier;
    }
    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }
    public String getId() {
        return ID;
    }

    public void setId(String ID) {
        this.ID = ID;
    }

    public List<NO_Queue_mobile_application__Line_item> getNo_queue_mobile_application__line_items() {
        return no_queue_mobile_application__line_items;
    }

    public void addNo_queue_mobile_application__line_item(No_queue_mobile_application__line_item no_queue_mobile_application__line_item) {
        this.no_queue_mobile_application__line_items.add(no_queue_mobile_application__line_item);
    }

}