





import java.util.List;
import java.util.ArrayList;

public class Payment  {

    private int Payment_method;
    private String Payment_type;
    private String Payment_id;





    private order order;


    public Payment(
        int Payment_method,        String Payment_type,        String Payment_id    ) {
        this.Payment_method = Payment_method;
        this.Payment_type = Payment_type;
        this.Payment_id = Payment_id;
    }


    public int getPayment_method() {
        return Payment_method;
    }

    public void setPayment_method(int Payment_method) {
        this.Payment_method = Payment_method;
    }
    public String getPayment_type() {
        return Payment_type;
    }

    public void setPayment_type(String Payment_type) {
        this.Payment_type = Payment_type;
    }
    public String getPayment_id() {
        return Payment_id;
    }

    public void setPayment_id(String Payment_id) {
        this.Payment_id = Payment_id;
    }

    public order getOrder() {
        return order;
    }

    public void setOrder(order order) {
        this.order = order;
    }

}