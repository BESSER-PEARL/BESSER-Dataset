





import java.util.List;
import java.util.ArrayList;

public class Order  {

    private String shippingAddress;
    private None status;
    private int id;
    private float finalTotal;





    private Payment payment;


    public Order(
        String shippingAddress,        None status,        int id,        float finalTotal    ) {
        this.shippingAddress = shippingAddress;
        this.status = status;
        this.id = id;
        this.finalTotal = finalTotal;
    }


    public String getShippingaddress() {
        return shippingAddress;
    }

    public void setShippingaddress(String shippingAddress) {
        this.shippingAddress = shippingAddress;
    }
    public None getStatus() {
        return status;
    }

    public void setStatus(None status) {
        this.status = status;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    public float getFinaltotal() {
        return finalTotal;
    }

    public void setFinaltotal(float finalTotal) {
        this.finalTotal = finalTotal;
    }

    public Payment getPayment() {
        return payment;
    }

    public void setPayment(Payment payment) {
        this.payment = payment;
    }

}