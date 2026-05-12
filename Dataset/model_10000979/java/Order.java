





import java.util.List;
import java.util.ArrayList;

public class Order  {

    private None status;
    private float finalTotal;
    private int id;
    private String shippingAddress;





    private Payment payment;


    public Order(
        None status,        float finalTotal,        int id,        String shippingAddress    ) {
        this.status = status;
        this.finalTotal = finalTotal;
        this.id = id;
        this.shippingAddress = shippingAddress;
    }


    public None getStatus() {
        return status;
    }

    public void setStatus(None status) {
        this.status = status;
    }
    public float getFinaltotal() {
        return finalTotal;
    }

    public void setFinaltotal(float finalTotal) {
        this.finalTotal = finalTotal;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    public String getShippingaddress() {
        return shippingAddress;
    }

    public void setShippingaddress(String shippingAddress) {
        this.shippingAddress = shippingAddress;
    }

    public Payment getPayment() {
        return payment;
    }

    public void setPayment(Payment payment) {
        this.payment = payment;
    }

}