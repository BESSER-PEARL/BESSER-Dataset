





import java.util.List;
import java.util.ArrayList;

public class Order  {

    private float finalTotal;
    private String shippingAddress;
    private None status;
    private int id;





    private Payment payment;


    public Order(
        float finalTotal,        String shippingAddress,        None status,        int id    ) {
        this.finalTotal = finalTotal;
        this.shippingAddress = shippingAddress;
        this.status = status;
        this.id = id;
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