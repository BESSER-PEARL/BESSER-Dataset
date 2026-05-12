





import java.util.List;
import java.util.ArrayList;

public class Products  {

    private String SKU_Code;
    private String Product_Name;





    private List<Customer> customers;


    public Products(
        String SKU_Code,        String Product_Name    ) {
        this.SKU_Code = SKU_Code;
        this.Product_Name = Product_Name;
        this.customers = new ArrayList<>();
    }

    public Products(
        String SKU_Code,        String Product_Name        ArrayList<Customer> customers    ) {
        this.SKU_Code = SKU_Code;
        this.Product_Name = Product_Name;
        this.customers = customers;
    }

    public String getSku_code() {
        return SKU_Code;
    }

    public void setSku_code(String SKU_Code) {
        this.SKU_Code = SKU_Code;
    }
    public String getProduct_name() {
        return Product_Name;
    }

    public void setProduct_name(String Product_Name) {
        this.Product_Name = Product_Name;
    }

    public List<Customer> getCustomers() {
        return customers;
    }

    public void addCustomer(Customer customer) {
        this.customers.add(customer);
    }

}