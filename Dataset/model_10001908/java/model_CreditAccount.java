





import java.util.List;
import java.util.ArrayList;

public class model_CreditAccount  {

    private String paymentDueDate;
    private float minPayment;
    private String type;
    private float interestRate;



    public model_CreditAccount(
        String paymentDueDate,        float minPayment,        String type,        float interestRate    ) {
        this.paymentDueDate = paymentDueDate;
        this.minPayment = minPayment;
        this.type = type;
        this.interestRate = interestRate;
    }


    public String getPaymentduedate() {
        return paymentDueDate;
    }

    public void setPaymentduedate(String paymentDueDate) {
        this.paymentDueDate = paymentDueDate;
    }
    public float getMinpayment() {
        return minPayment;
    }

    public void setMinpayment(float minPayment) {
        this.minPayment = minPayment;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public float getInterestrate() {
        return interestRate;
    }

    public void setInterestrate(float interestRate) {
        this.interestRate = interestRate;
    }


}