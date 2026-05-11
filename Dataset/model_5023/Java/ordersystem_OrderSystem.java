





import java.util.List;
import java.util.ArrayList;

public class ordersystem_OrderSystem  {

    private int version;





    private List<ordersystem_Product> ordersystem_products;




    private List<ordersystem_Customer> ordersystem_customers;




    private ordersystem_Customer ordersystem_customer;




    private ordersystem_Product ordersystem_product;


    public ordersystem_OrderSystem(
        int version    ) {
        this.version = version;
        this.ordersystem_products = new ArrayList<>();
        this.ordersystem_customers = new ArrayList<>();
    }

    public ordersystem_OrderSystem(
        int version        ArrayList<ordersystem_Product> ordersystem_products,        ArrayList<ordersystem_Customer> ordersystem_customers    ) {
        this.version = version;
        this.ordersystem_products = ordersystem_products;
        this.ordersystem_customers = ordersystem_customers;
    }

    public int getVersion() {
        return version;
    }

    public void setVersion(int version) {
        this.version = version;
    }

    public List<ordersystem_Product> getOrdersystem_products() {
        return ordersystem_products;
    }

    public void addOrdersystem_product(Ordersystem_product ordersystem_product) {
        this.ordersystem_products.add(ordersystem_product);
    }
    public List<ordersystem_Customer> getOrdersystem_customers() {
        return ordersystem_customers;
    }

    public void addOrdersystem_customer(Ordersystem_customer ordersystem_customer) {
        this.ordersystem_customers.add(ordersystem_customer);
    }
    public ordersystem_Customer getOrdersystem_customer() {
        return ordersystem_customer;
    }

    public void setOrdersystem_customer(ordersystem_Customer ordersystem_customer) {
        this.ordersystem_customer = ordersystem_customer;
    }
    public ordersystem_Product getOrdersystem_product() {
        return ordersystem_product;
    }

    public void setOrdersystem_product(ordersystem_Product ordersystem_product) {
        this.ordersystem_product = ordersystem_product;
    }

}