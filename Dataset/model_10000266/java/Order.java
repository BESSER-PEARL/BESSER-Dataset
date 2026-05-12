





import java.util.List;
import java.util.ArrayList;

public class Order  {

    private int id;
    private None status;
    private float finalTotal;
    private String shippingAddress;





    private Payment payment;


    public Order(
        int id,        None status,        float finalTotal,        String shippingAddress    ) {
        this.id = id;
        this.status = status;
        this.finalTotal = finalTotal;
        this.shippingAddress = shippingAddress;
    }


    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
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