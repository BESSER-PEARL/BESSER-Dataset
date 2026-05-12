





import java.util.List;
import java.util.ArrayList;

public class Credit_Card  {

    private String Pin_No_;
    private String Card_No_;





    private Payment payment;


    public Credit_Card(
        String Pin_No_,        String Card_No_    ) {
        this.Pin_No_ = Pin_No_;
        this.Card_No_ = Card_No_;
    }


    public String getPin_no_() {
        return Pin_No_;
    }

    public void setPin_no_(String Pin_No_) {
        this.Pin_No_ = Pin_No_;
    }
    public String getCard_no_() {
        return Card_No_;
    }

    public void setCard_no_(String Card_No_) {
        this.Card_No_ = Card_No_;
    }

    public Payment getPayment() {
        return payment;
    }

    public void setPayment(Payment payment) {
        this.payment = payment;
    }

}