





import java.util.List;
import java.util.ArrayList;

public class Medical_Record_NHS_Number  {

    private None type;
    private float balance;
    private String accountNo;





    private List<transaction_Interface> transaction_interfaces;


    public Medical_Record_NHS_Number(
        None type,        float balance,        String accountNo    ) {
        this.type = type;
        this.balance = balance;
        this.accountNo = accountNo;
        this.transaction_interfaces = new ArrayList<>();
    }

    public Medical_Record_NHS_Number(
        None type,        float balance,        String accountNo        ArrayList<transaction_Interface> transaction_interfaces    ) {
        this.type = type;
        this.balance = balance;
        this.accountNo = accountNo;
        this.transaction_interfaces = transaction_interfaces;
    }

    public None getType() {
        return type;
    }

    public void setType(None type) {
        this.type = type;
    }
    public float getBalance() {
        return balance;
    }

    public void setBalance(float balance) {
        this.balance = balance;
    }
    public String getAccountno() {
        return accountNo;
    }

    public void setAccountno(String accountNo) {
        this.accountNo = accountNo;
    }

    public List<transaction_Interface> getTransaction_interfaces() {
        return transaction_interfaces;
    }

    public void addTransaction_interface(Transaction_interface transaction_interface) {
        this.transaction_interfaces.add(transaction_interface);
    }

}