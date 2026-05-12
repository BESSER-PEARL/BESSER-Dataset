





import java.util.List;
import java.util.ArrayList;

public class bank_Manager  {

    private String name;





    private bank_Bank bank_bank;




    private bank_Client bank_client;




    private List<bank_Client> bank_clients;


    public bank_Manager(
        String name    ) {
        this.name = name;
        this.bank_clients = new ArrayList<>();
    }

    public bank_Manager(
        String name        ArrayList<bank_Client> bank_clients    ) {
        this.name = name;
        this.bank_clients = bank_clients;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public bank_Bank getBank_bank() {
        return bank_bank;
    }

    public void setBank_bank(bank_Bank bank_bank) {
        this.bank_bank = bank_bank;
    }
    public bank_Client getBank_client() {
        return bank_client;
    }

    public void setBank_client(bank_Client bank_client) {
        this.bank_client = bank_client;
    }
    public List<bank_Client> getBank_clients() {
        return bank_clients;
    }

    public void addBank_client(Bank_client bank_client) {
        this.bank_clients.add(bank_client);
    }

}