





import java.util.List;
import java.util.ArrayList;

public class Store  {






    private List<Product> products;




    private Transactions transactions;




    private List<Service> services;


    public Store(
    ) {
        this.products = new ArrayList<>();
        this.services = new ArrayList<>();
    }

    public Store(
        ArrayList<Product> products,        ArrayList<Service> services    ) {
        this.products = products;
        this.services = services;
    }


    public List<Product> getProducts() {
        return products;
    }

    public void addProduct(Product product) {
        this.products.add(product);
    }
    public Transactions getTransactions() {
        return transactions;
    }

    public void setTransactions(Transactions transactions) {
        this.transactions = transactions;
    }
    public List<Service> getServices() {
        return services;
    }

    public void addService(Service service) {
        this.services.add(service);
    }

}