





import java.util.List;
import java.util.ArrayList;

public class ExpenseType  {

    private String id;
    private String name;
    private String price;





    private Bill bill;


    public ExpenseType(
        String id,        String name,        String price    ) {
        this.id = id;
        this.name = name;
        this.price = price;
    }


    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getPrice() {
        return price;
    }

    public void setPrice(String price) {
        this.price = price;
    }

    public Bill getBill() {
        return bill;
    }

    public void setBill(Bill bill) {
        this.bill = bill;
    }

}