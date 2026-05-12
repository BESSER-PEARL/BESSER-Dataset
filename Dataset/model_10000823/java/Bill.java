





import java.util.List;
import java.util.ArrayList;

public class Bill  {

    private String date;
    private String attachment_id;
    private None payment_method;
    private None status;
    private String distance;
    private String sum;
    private String id;





    private Expense expense;


    public Bill(
        String date,        String attachment_id,        None payment_method,        None status,        String distance,        String sum,        String id    ) {
        this.date = date;
        this.attachment_id = attachment_id;
        this.payment_method = payment_method;
        this.status = status;
        this.distance = distance;
        this.sum = sum;
        this.id = id;
    }


    public String getDate() {
        return date;
    }

    public void setDate(String date) {
        this.date = date;
    }
    public String getAttachment_id() {
        return attachment_id;
    }

    public void setAttachment_id(String attachment_id) {
        this.attachment_id = attachment_id;
    }
    public None getPayment_method() {
        return payment_method;
    }

    public void setPayment_method(None payment_method) {
        this.payment_method = payment_method;
    }
    public None getStatus() {
        return status;
    }

    public void setStatus(None status) {
        this.status = status;
    }
    public String getDistance() {
        return distance;
    }

    public void setDistance(String distance) {
        this.distance = distance;
    }
    public String getSum() {
        return sum;
    }

    public void setSum(String sum) {
        this.sum = sum;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public Expense getExpense() {
        return expense;
    }

    public void setExpense(Expense expense) {
        this.expense = expense;
    }

}