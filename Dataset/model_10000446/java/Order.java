





import java.util.List;
import java.util.ArrayList;

public class Order  {

    private String shippingAddress;
    private float finalTotal;
    private None status;
    private int id;





    private Payment payment;


    public Order(
        String shippingAddress,        float finalTotal,        None status,        int id    ) {
        this.shippingAddress = shippingAddress;
        this.finalTotal = finalTotal;
        this.status = status;
        this.id = id;
    }


    public String getShippingaddress() {
        return shippingAddress;
    }

    public void setShippingaddress(String shippingAddress) {
        this.shippingAddress = shippingAddress;
    }
    public float getFinaltotal() {
        return finalTotal;
    }

    public void setFinaltotal(float finalTotal) {
        this.finalTotal = finalTotal;
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

    public Payment getPayment() {
        return payment;
    }

    public void setPayment(Payment payment) {
        this.payment = payment;
    }

}