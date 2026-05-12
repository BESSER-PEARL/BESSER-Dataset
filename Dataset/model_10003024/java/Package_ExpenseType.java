





import java.util.List;
import java.util.ArrayList;

public class Package_ExpenseType  {

    private String price;
    private String name;
    private String id;





    private Package_Bill package_bill;


    public Package_ExpenseType(
        String price,        String name,        String id    ) {
        this.price = price;
        this.name = name;
        this.id = id;
    }


    public String getPrice() {
        return price;
    }

    public void setPrice(String price) {
        this.price = price;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public Package_Bill getPackage_bill() {
        return package_bill;
    }

    public void setPackage_bill(Package_Bill package_bill) {
        this.package_bill = package_bill;
    }

}