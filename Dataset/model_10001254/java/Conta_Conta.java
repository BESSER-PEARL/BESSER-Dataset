





import java.util.List;
import java.util.ArrayList;

public class Conta_Conta  {

    private None type;
    private String contanum;
    private float balance;





    private List<transaction_Transaction> transaction_transactions;




    private Cliente cliente;


    public Conta_Conta(
        None type,        String contanum,        float balance    ) {
        this.type = type;
        this.contanum = contanum;
        this.balance = balance;
        this.transaction_transactions = new ArrayList<>();
    }

    public Conta_Conta(
        None type,        String contanum,        float balance        ArrayList<transaction_Transaction> transaction_transactions    ) {
        this.type = type;
        this.contanum = contanum;
        this.balance = balance;
        this.transaction_transactions = transaction_transactions;
    }

    public None getType() {
        return type;
    }

    public void setType(None type) {
        this.type = type;
    }
    public String getContanum() {
        return contanum;
    }

    public void setContanum(String contanum) {
        this.contanum = contanum;
    }
    public float getBalance() {
        return balance;
    }

    public void setBalance(float balance) {
        this.balance = balance;
    }

    public List<transaction_Transaction> getTransaction_transactions() {
        return transaction_transactions;
    }

    public void addTransaction_transaction(Transaction_transaction transaction_transaction) {
        this.transaction_transactions.add(transaction_transaction);
    }
    public Cliente getCliente() {
        return cliente;
    }

    public void setCliente(Cliente cliente) {
        this.cliente = cliente;
    }

}