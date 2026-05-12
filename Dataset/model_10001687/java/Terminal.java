





import java.util.List;
import java.util.ArrayList;

public class Terminal  {

    private String Current_Employee;





    private List<Transactions> transactionss;


    public Terminal(
        String Current_Employee    ) {
        this.Current_Employee = Current_Employee;
        this.transactionss = new ArrayList<>();
    }

    public Terminal(
        String Current_Employee        ArrayList<Transactions> transactionss    ) {
        this.Current_Employee = Current_Employee;
        this.transactionss = transactionss;
    }

    public String getCurrent_employee() {
        return Current_Employee;
    }

    public void setCurrent_employee(String Current_Employee) {
        this.Current_Employee = Current_Employee;
    }

    public List<Transactions> getTransactionss() {
        return transactionss;
    }

    public void addTransactions(Transactions transactions) {
        this.transactionss.add(transactions);
    }

}