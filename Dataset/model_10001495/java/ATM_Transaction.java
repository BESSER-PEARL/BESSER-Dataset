





import java.util.List;
import java.util.ArrayList;

public class ATM_Transaction  {

    private String Date;
    private int Amount;
    private String TransactionId;





    private ATM_INFO atm_info;


    public ATM_Transaction(
        String Date,        int Amount,        String TransactionId    ) {
        this.Date = Date;
        this.Amount = Amount;
        this.TransactionId = TransactionId;
    }


    public String getDate() {
        return Date;
    }

    public void setDate(String Date) {
        this.Date = Date;
    }
    public int getAmount() {
        return Amount;
    }

    public void setAmount(int Amount) {
        this.Amount = Amount;
    }
    public String getTransactionid() {
        return TransactionId;
    }

    public void setTransactionid(String TransactionId) {
        this.TransactionId = TransactionId;
    }

    public ATM_INFO getAtm_info() {
        return atm_info;
    }

    public void setAtm_info(ATM_INFO atm_info) {
        this.atm_info = atm_info;
    }

}