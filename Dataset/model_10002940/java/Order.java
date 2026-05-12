





import java.util.List;
import java.util.ArrayList;

public class Order  {

    private String shippingAddress;
    private float finalTotal;
    private int id;
    private None status;





    private Payment payment;


    public Order(
        String shippingAddress,        float finalTotal,        int id,        None status    ) {
        this.shippingAddress = shippingAddress;
        this.finalTotal = finalTotal;
        this.id = id;
        this.status = status;
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

    public Payment getPayment() {
        return payment;
    }

    public void setPayment(Payment payment) {
        this.payment = payment;
    }

}