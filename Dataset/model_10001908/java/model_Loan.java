





import java.util.List;
import java.util.ArrayList;

public class model_Loan  {

    private float minPayment;
    private String paymentDueDate;
    private String type;
    private float interestRate;



    public model_Loan(
        float minPayment,        String paymentDueDate,        String type,        float interestRate    ) {
        this.minPayment = minPayment;
        this.paymentDueDate = paymentDueDate;
        this.type = type;
        this.interestRate = interestRate;
    }


    public float getMinpayment() {
        return minPayment;
    }

    public void setMinpayment(float minPayment) {
        this.minPayment = minPayment;
    }
    public String getPaymentduedate() {
        return paymentDueDate;
    }

    public void setPaymentduedate(String paymentDueDate) {
        this.paymentDueDate = paymentDueDate;
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