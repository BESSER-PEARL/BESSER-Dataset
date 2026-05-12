





import java.util.List;
import java.util.ArrayList;

public class Payment  {

    private int paymentId;
    private String paymentTotal;



    public Payment(
        int paymentId,        String paymentTotal    ) {
        this.paymentId = paymentId;
        this.paymentTotal = paymentTotal;
    }


    public int getPaymentid() {
        return paymentId;
    }

    public void setPaymentid(int paymentId) {
        this.paymentId = paymentId;
    }
    public String getPaymenttotal() {
        return paymentTotal;
    }

    public void setPaymenttotal(String paymentTotal) {
        this.paymentTotal = paymentTotal;
    }


}