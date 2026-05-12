





import java.util.List;
import java.util.ArrayList;

public class Delivering_Management  {

    private String client_key;
    private String client_name;
    private String deliver_boy_id;





    private Cleaning_Management cleaning_management;




    private User user;


    public Delivering_Management(
        String client_key,        String client_name,        String deliver_boy_id    ) {
        this.client_key = client_key;
        this.client_name = client_name;
        this.deliver_boy_id = deliver_boy_id;
    }


    public String getClient_key() {
        return client_key;
    }

    public void setClient_key(String client_key) {
        this.client_key = client_key;
    }
    public String getClient_name() {
        return client_name;
    }

    public void setClient_name(String client_name) {
        this.client_name = client_name;
    }
    public String getDeliver_boy_id() {
        return deliver_boy_id;
    }

    public void setDeliver_boy_id(String deliver_boy_id) {
        this.deliver_boy_id = deliver_boy_id;
    }

    public Cleaning_Management getCleaning_management() {
        return cleaning_management;
    }

    public void setCleaning_management(Cleaning_Management cleaning_management) {
        this.cleaning_management = cleaning_management;
    }
    public User getUser() {
        return user;
    }

    public void setUser(User user) {
        this.user = user;
    }

}