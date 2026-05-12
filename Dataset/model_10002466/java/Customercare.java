





import java.util.List;
import java.util.ArrayList;

public class Customercare  {

    private int no;
    private String address;





    private List<Client> clients;


    public Customercare(
        int no,        String address    ) {
        this.no = no;
        this.address = address;
        this.clients = new ArrayList<>();
    }

    public Customercare(
        int no,        String address        ArrayList<Client> clients    ) {
        this.no = no;
        this.address = address;
        this.clients = clients;
    }

    public int getNo() {
        return no;
    }

    public void setNo(int no) {
        this.no = no;
    }
    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }

    public List<Client> getClients() {
        return clients;
    }

    public void addClient(Client client) {
        this.clients.add(client);
    }

}