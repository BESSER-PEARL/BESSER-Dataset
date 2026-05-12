





import java.util.List;
import java.util.ArrayList;

public class Package_Bill  {

    private String sum;
    private String id;
    private None payment_method;
    private String attachment_id;
    private String distance;
    private String date;
    private None status;





    private Package_Expense package_expense;


    public Package_Bill(
        String sum,        String id,        None payment_method,        String attachment_id,        String distance,        String date,        None status    ) {
        this.sum = sum;
        this.id = id;
        this.payment_method = payment_method;
        this.attachment_id = attachment_id;
        this.distance = distance;
        this.date = date;
        this.status = status;
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
    public None getPayment_method() {
        return payment_method;
    }

    public void setPayment_method(None payment_method) {
        this.payment_method = payment_method;
    }
    public String getAttachment_id() {
        return attachment_id;
    }

    public void setAttachment_id(String attachment_id) {
        this.attachment_id = attachment_id;
    }
    public String getDistance() {
        return distance;
    }

    public void setDistance(String distance) {
        this.distance = distance;
    }
    public String getDate() {
        return date;
    }

    public void setDate(String date) {
        this.date = date;
    }
    public None getStatus() {
        return status;
    }

    public void setStatus(None status) {
        this.status = status;
    }

    public Package_Expense getPackage_expense() {
        return package_expense;
    }

    public void setPackage_expense(Package_Expense package_expense) {
        this.package_expense = package_expense;
    }

}