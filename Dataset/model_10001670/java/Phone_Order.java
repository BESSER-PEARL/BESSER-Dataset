





import java.util.List;
import java.util.ArrayList;

public class Phone_Order  {

    private String Date;





    private Customer customer;




    private List<Items> itemss;


    public Phone_Order(
        String Date    ) {
        this.Date = Date;
        this.itemss = new ArrayList<>();
    }

    public Phone_Order(
        String Date        ArrayList<Items> itemss    ) {
        this.Date = Date;
        this.itemss = itemss;
    }

    public String getDate() {
        return Date;
    }

    public void setDate(String Date) {
        this.Date = Date;
    }

    public Customer getCustomer() {
        return customer;
    }

    public void setCustomer(Customer customer) {
        this.customer = customer;
    }
    public List<Items> getItemss() {
        return itemss;
    }

    public void addItems(Items items) {
        this.itemss.add(items);
    }

}