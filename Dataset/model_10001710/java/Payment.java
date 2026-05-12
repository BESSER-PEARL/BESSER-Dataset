





import java.util.List;
import java.util.ArrayList;

public class Payment  {

    private String total;
    private String Details;
    private String txn_id;
    private String paid;



    public Payment(
        String total,        String Details,        String txn_id,        String paid    ) {
        this.total = total;
        this.Details = Details;
        this.txn_id = txn_id;
        this.paid = paid;
    }


    public String getTotal() {
        return total;
    }

    public void setTotal(String total) {
        this.total = total;
    }
    public String getDetails() {
        return Details;
    }

    public void setDetails(String Details) {
        this.Details = Details;
    }
    public String getTxn_id() {
        return txn_id;
    }

    public void setTxn_id(String txn_id) {
        this.txn_id = txn_id;
    }
    public String getPaid() {
        return paid;
    }

    public void setPaid(String paid) {
        this.paid = paid;
    }


}