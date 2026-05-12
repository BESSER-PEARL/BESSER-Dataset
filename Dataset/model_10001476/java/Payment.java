





import java.util.List;
import java.util.ArrayList;

public class Payment  {

    private int amout;
    private String paytype;
    private String status;





    private Client client;


    public Payment(
        int amout,        String paytype,        String status    ) {
        this.amout = amout;
        this.paytype = paytype;
        this.status = status;
    }


    public int getAmout() {
        return amout;
    }

    public void setAmout(int amout) {
        this.amout = amout;
    }
    public String getPaytype() {
        return paytype;
    }

    public void setPaytype(String paytype) {
        this.paytype = paytype;
    }
    public String getStatus() {
        return status;
    }

    public void setStatus(String status) {
        this.status = status;
    }

    public Client getClient() {
        return client;
    }

    public void setClient(Client client) {
        this.client = client;
    }

}