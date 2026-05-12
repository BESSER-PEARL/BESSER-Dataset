





import java.util.List;
import java.util.ArrayList;

public class Payment  {

    private String paymentType;





    private List<Bill> bills;


    public Payment(
        String paymentType    ) {
        this.paymentType = paymentType;
        this.bills = new ArrayList<>();
    }

    public Payment(
        String paymentType        ArrayList<Bill> bills    ) {
        this.paymentType = paymentType;
        this.bills = bills;
    }

    public String getPaymenttype() {
        return paymentType;
    }

    public void setPaymenttype(String paymentType) {
        this.paymentType = paymentType;
    }

    public List<Bill> getBills() {
        return bills;
    }

    public void addBill(Bill bill) {
        this.bills.add(bill);
    }

}