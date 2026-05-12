





import java.util.List;
import java.util.ArrayList;

public class client_ClientAccount  {

    private String clientNo;
    private None type;





    private Client client;




    private List<virtualtour_Transaction> virtualtour_transactions;


    public client_ClientAccount(
        String clientNo,        None type    ) {
        this.clientNo = clientNo;
        this.type = type;
        this.virtualtour_transactions = new ArrayList<>();
    }

    public client_ClientAccount(
        String clientNo,        None type        ArrayList<virtualtour_Transaction> virtualtour_transactions    ) {
        this.clientNo = clientNo;
        this.type = type;
        this.virtualtour_transactions = virtualtour_transactions;
    }

    public String getClientno() {
        return clientNo;
    }

    public void setClientno(String clientNo) {
        this.clientNo = clientNo;
    }
    public None getType() {
        return type;
    }

    public void setType(None type) {
        this.type = type;
    }

    public Client getClient() {
        return client;
    }

    public void setClient(Client client) {
        this.client = client;
    }
    public List<virtualtour_Transaction> getVirtualtour_transactions() {
        return virtualtour_transactions;
    }

    public void addVirtualtour_transaction(Virtualtour_transaction virtualtour_transaction) {
        this.virtualtour_transactions.add(virtualtour_transaction);
    }

}