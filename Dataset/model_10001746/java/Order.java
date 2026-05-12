





import java.util.List;
import java.util.ArrayList;

public class Order  {

    private String PaymentMethod;
    private String Date;
    private None HomeAddress;
    private None CustomerName;
    private int OrderNumber;
    private None Products;





    private List<ClientAccount> clientaccounts;


    public Order(
        String PaymentMethod,        String Date,        None HomeAddress,        None CustomerName,        int OrderNumber,        None Products    ) {
        this.PaymentMethod = PaymentMethod;
        this.Date = Date;
        this.HomeAddress = HomeAddress;
        this.CustomerName = CustomerName;
        this.OrderNumber = OrderNumber;
        this.Products = Products;
        this.clientaccounts = new ArrayList<>();
    }

    public Order(
        String PaymentMethod,        String Date,        None HomeAddress,        None CustomerName,        int OrderNumber,        None Products        ArrayList<ClientAccount> clientaccounts    ) {
        this.PaymentMethod = PaymentMethod;
        this.Date = Date;
        this.HomeAddress = HomeAddress;
        this.CustomerName = CustomerName;
        this.OrderNumber = OrderNumber;
        this.Products = Products;
        this.clientaccounts = clientaccounts;
    }

    public String getPaymentmethod() {
        return PaymentMethod;
    }

    public void setPaymentmethod(String PaymentMethod) {
        this.PaymentMethod = PaymentMethod;
    }
    public String getDate() {
        return Date;
    }

    public void setDate(String Date) {
        this.Date = Date;
    }
    public None getHomeaddress() {
        return HomeAddress;
    }

    public void setHomeaddress(None HomeAddress) {
        this.HomeAddress = HomeAddress;
    }
    public None getCustomername() {
        return CustomerName;
    }

    public void setCustomername(None CustomerName) {
        this.CustomerName = CustomerName;
    }
    public int getOrdernumber() {
        return OrderNumber;
    }

    public void setOrdernumber(int OrderNumber) {
        this.OrderNumber = OrderNumber;
    }
    public None getProducts() {
        return Products;
    }

    public void setProducts(None Products) {
        this.Products = Products;
    }

    public List<ClientAccount> getClientaccounts() {
        return clientaccounts;
    }

    public void addClientaccount(Clientaccount clientaccount) {
        this.clientaccounts.add(clientaccount);
    }

}