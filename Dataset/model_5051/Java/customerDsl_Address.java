





import java.util.List;
import java.util.ArrayList;

public class customerDsl_Address  {

    private String zip;
    private String name;





    private customerDsl_Customer customerdsl_customer;




    private customerDsl_Order customerdsl_order;


    public customerDsl_Address(
        String zip,        String name    ) {
        this.zip = zip;
        this.name = name;
    }


    public String getZip() {
        return zip;
    }

    public void setZip(String zip) {
        this.zip = zip;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public customerDsl_Customer getCustomerdsl_customer() {
        return customerdsl_customer;
    }

    public void setCustomerdsl_customer(customerDsl_Customer customerdsl_customer) {
        this.customerdsl_customer = customerdsl_customer;
    }
    public customerDsl_Order getCustomerdsl_order() {
        return customerdsl_order;
    }

    public void setCustomerdsl_order(customerDsl_Order customerdsl_order) {
        this.customerdsl_order = customerdsl_order;
    }

}