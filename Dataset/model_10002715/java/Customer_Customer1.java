





import java.util.List;
import java.util.ArrayList;

public class Customer_Customer1  {

    private float PaymentMet__;
    private String select__;
    private String Account__;
    private String userId;



    public Customer_Customer1(
        float PaymentMet__,        String select__,        String Account__,        String userId    ) {
        this.PaymentMet__ = PaymentMet__;
        this.select__ = select__;
        this.Account__ = Account__;
        this.userId = userId;
    }


    public float getPaymentmet__() {
        return PaymentMet__;
    }

    public void setPaymentmet__(float PaymentMet__) {
        this.PaymentMet__ = PaymentMet__;
    }
    public String getSelect__() {
        return select__;
    }

    public void setSelect__(String select__) {
        this.select__ = select__;
    }
    public String getAccount__() {
        return Account__;
    }

    public void setAccount__(String Account__) {
        this.Account__ = Account__;
    }
    public String getUserid() {
        return userId;
    }

    public void setUserid(String userId) {
        this.userId = userId;
    }


}