





import java.util.List;
import java.util.ArrayList;

public class Orders  {

    private String dateShipped;
    private int u_id;
    private String dateCreated;
    private int customer_id;
    private int status;



    public Orders(
        String dateShipped,        int u_id,        String dateCreated,        int customer_id,        int status    ) {
        this.dateShipped = dateShipped;
        this.u_id = u_id;
        this.dateCreated = dateCreated;
        this.customer_id = customer_id;
        this.status = status;
    }


    public String getDateshipped() {
        return dateShipped;
    }

    public void setDateshipped(String dateShipped) {
        this.dateShipped = dateShipped;
    }
    public int getU_id() {
        return u_id;
    }

    public void setU_id(int u_id) {
        this.u_id = u_id;
    }
    public String getDatecreated() {
        return dateCreated;
    }

    public void setDatecreated(String dateCreated) {
        this.dateCreated = dateCreated;
    }
    public int getCustomer_id() {
        return customer_id;
    }

    public void setCustomer_id(int customer_id) {
        this.customer_id = customer_id;
    }
    public int getStatus() {
        return status;
    }

    public void setStatus(int status) {
        this.status = status;
    }


}