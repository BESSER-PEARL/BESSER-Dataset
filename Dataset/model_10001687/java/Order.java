





import java.util.List;
import java.util.ArrayList;

public class Order  {

    private String Product;
    private String Service;





    private Transactions transactions;


    public Order(
        String Product,        String Service    ) {
        this.Product = Product;
        this.Service = Service;
    }


    public String getProduct() {
        return Product;
    }

    public void setProduct(String Product) {
        this.Product = Product;
    }
    public String getService() {
        return Service;
    }

    public void setService(String Service) {
        this.Service = Service;
    }

    public Transactions getTransactions() {
        return transactions;
    }

    public void setTransactions(Transactions transactions) {
        this.transactions = transactions;
    }

}