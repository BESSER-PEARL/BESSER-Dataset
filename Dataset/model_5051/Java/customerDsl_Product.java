





import java.util.List;
import java.util.ArrayList;

public class customerDsl_Product  {

    private String name;
    private int price;





    private customerDsl_CustomerDb customerdsl_customerdb;


    public customerDsl_Product(
        String name,        int price    ) {
        this.name = name;
        this.price = price;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public int getPrice() {
        return price;
    }

    public void setPrice(int price) {
        this.price = price;
    }

    public customerDsl_CustomerDb getCustomerdsl_customerdb() {
        return customerdsl_customerdb;
    }

    public void setCustomerdsl_customerdb(customerDsl_CustomerDb customerdsl_customerdb) {
        this.customerdsl_customerdb = customerdsl_customerdb;
    }

}