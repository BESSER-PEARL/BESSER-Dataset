





import java.util.List;
import java.util.ArrayList;

public class Classes_BuisnessLogicLayer_PaymentInfo  {

    private int CreditCard;
    private int ExpiryDate;
    private boolean PaymentComplete;
    private int CVV;





    private PaymentHandler paymenthandler;


    public Classes_BuisnessLogicLayer_PaymentInfo(
        int CreditCard,        int ExpiryDate,        boolean PaymentComplete,        int CVV    ) {
        this.CreditCard = CreditCard;
        this.ExpiryDate = ExpiryDate;
        this.PaymentComplete = PaymentComplete;
        this.CVV = CVV;
    }


    public int getCreditcard() {
        return CreditCard;
    }

    public void setCreditcard(int CreditCard) {
        this.CreditCard = CreditCard;
    }
    public int getExpirydate() {
        return ExpiryDate;
    }

    public void setExpirydate(int ExpiryDate) {
        this.ExpiryDate = ExpiryDate;
    }
    public boolean getPaymentcomplete() {
        return PaymentComplete;
    }

    public void setPaymentcomplete(boolean PaymentComplete) {
        this.PaymentComplete = PaymentComplete;
    }
    public int getCvv() {
        return CVV;
    }

    public void setCvv(int CVV) {
        this.CVV = CVV;
    }

    public PaymentHandler getPaymenthandler() {
        return paymenthandler;
    }

    public void setPaymenthandler(PaymentHandler paymenthandler) {
        this.paymenthandler = paymenthandler;
    }

}