





import java.util.List;
import java.util.ArrayList;

public class Payment_Verification  {

    private String status;
    private String txn_id;





    private Customer customer;




    private Payment payment;




    private Account account;


    public Payment_Verification(
        String status,        String txn_id    ) {
        this.status = status;
        this.txn_id = txn_id;
    }


    public String getStatus() {
        return status;
    }

    public void setStatus(String status) {
        this.status = status;
    }
    public String getTxn_id() {
        return txn_id;
    }

    public void setTxn_id(String txn_id) {
        this.txn_id = txn_id;
    }

    public Customer getCustomer() {
        return customer;
    }

    public void setCustomer(Customer customer) {
        this.customer = customer;
    }
    public Payment getPayment() {
        return payment;
    }

    public void setPayment(Payment payment) {
        this.payment = payment;
    }
    public Account getAccount() {
        return account;
    }

    public void setAccount(Account account) {
        this.account = account;
    }

}