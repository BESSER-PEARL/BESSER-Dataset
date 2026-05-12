





import java.util.List;
import java.util.ArrayList;

public class Medical_Record_NHS_Number  {

    private float balance;
    private None type;
    private String accountNo;





    private Patient patient;




    private List<transaction_Interface> transaction_interfaces;


    public Medical_Record_NHS_Number(
        float balance,        None type,        String accountNo    ) {
        this.balance = balance;
        this.type = type;
        this.accountNo = accountNo;
        this.transaction_interfaces = new ArrayList<>();
    }

    public Medical_Record_NHS_Number(
        float balance,        None type,        String accountNo        ArrayList<transaction_Interface> transaction_interfaces    ) {
        this.balance = balance;
        this.type = type;
        this.accountNo = accountNo;
        this.transaction_interfaces = transaction_interfaces;
    }

    public float getBalance() {
        return balance;
    }

    public void setBalance(float balance) {
        this.balance = balance;
    }
    public None getType() {
        return type;
    }

    public void setType(None type) {
        this.type = type;
    }
    public String getAccountno() {
        return accountNo;
    }

    public void setAccountno(String accountNo) {
        this.accountNo = accountNo;
    }

    public Patient getPatient() {
        return patient;
    }

    public void setPatient(Patient patient) {
        this.patient = patient;
    }
    public List<transaction_Interface> getTransaction_interfaces() {
        return transaction_interfaces;
    }

    public void addTransaction_interface(Transaction_interface transaction_interface) {
        this.transaction_interfaces.add(transaction_interface);
    }

}