





import java.util.List;
import java.util.ArrayList;

public class Groupe  {

    private String rang;





    private List<Client> clients;


    public Groupe(
        String rang    ) {
        this.rang = rang;
        this.clients = new ArrayList<>();
    }

    public Groupe(
        String rang        ArrayList<Client> clients    ) {
        this.rang = rang;
        this.clients = clients;
    }

    public String getRang() {
        return rang;
    }

    public void setRang(String rang) {
        this.rang = rang;
    }

    public List<Client> getClients() {
        return clients;
    }

    public void addClient(Client client) {
        this.clients.add(client);
    }

}