





import java.util.List;
import java.util.ArrayList;

public class Order  {

    private String shipped;
    private String status;
    private String t;
    private String address;
    private String ordered;
    private String items;





    private Account account;




    private Payment payment;


    public Order(
        String shipped,        String status,        String t,        String address,        String ordered,        String items    ) {
        this.shipped = shipped;
        this.status = status;
        this.t = t;
        this.address = address;
        this.ordered = ordered;
        this.items = items;
    }


    public String getShipped() {
        return shipped;
    }

    public void setShipped(String shipped) {
        this.shipped = shipped;
    }
    public String getStatus() {
        return status;
    }

    public void setStatus(String status) {
        this.status = status;
    }
    public String getT() {
        return t;
    }

    public void setT(String t) {
        this.t = t;
    }
    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }
    public String getOrdered() {
        return ordered;
    }

    public void setOrdered(String ordered) {
        this.ordered = ordered;
    }
    public String getItems() {
        return items;
    }

    public void setItems(String items) {
        this.items = items;
    }

    public Account getAccount() {
        return account;
    }

    public void setAccount(Account account) {
        this.account = account;
    }
    public Payment getPayment() {
        return payment;
    }

    public void setPayment(Payment payment) {
        this.payment = payment;
    }

}