





import java.util.List;
import java.util.ArrayList;

public class Shopping_Cart  {

    private float total;
    private String id;
    private String number;





    private Payment payment;




    private Order order;


    public Shopping_Cart(
        float total,        String id,        String number    ) {
        this.total = total;
        this.id = id;
        this.number = number;
    }


    public float getTotal() {
        return total;
    }

    public void setTotal(float total) {
        this.total = total;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getNumber() {
        return number;
    }

    public void setNumber(String number) {
        this.number = number;
    }

    public Payment getPayment() {
        return payment;
    }

    public void setPayment(Payment payment) {
        this.payment = payment;
    }
    public Order getOrder() {
        return order;
    }

    public void setOrder(Order order) {
        this.order = order;
    }

}