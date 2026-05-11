





import java.util.List;
import java.util.ArrayList;

public class accounting_Clients  {






    private List<accounting_Client> accounting_clients;


    public accounting_Clients(
    ) {
        this.accounting_clients = new ArrayList<>();
    }

    public accounting_Clients(
        ArrayList<accounting_Client> accounting_clients    ) {
        this.accounting_clients = accounting_clients;
    }


    public List<accounting_Client> getAccounting_clients() {
        return accounting_clients;
    }

    public void addAccounting_client(Accounting_client accounting_client) {
        this.accounting_clients.add(accounting_client);
    }

}