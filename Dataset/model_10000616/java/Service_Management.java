





import java.util.List;
import java.util.ArrayList;

public class Service_Management  {

    private String client_name;
    private String client_key;
    private String Staff_boy_id;





    private User user;




    private Cleaning_Management cleaning_management;


    public Service_Management(
        String client_name,        String client_key,        String Staff_boy_id    ) {
        this.client_name = client_name;
        this.client_key = client_key;
        this.Staff_boy_id = Staff_boy_id;
    }


    public String getClient_name() {
        return client_name;
    }

    public void setClient_name(String client_name) {
        this.client_name = client_name;
    }
    public String getClient_key() {
        return client_key;
    }

    public void setClient_key(String client_key) {
        this.client_key = client_key;
    }
    public String getStaff_boy_id() {
        return Staff_boy_id;
    }

    public void setStaff_boy_id(String Staff_boy_id) {
        this.Staff_boy_id = Staff_boy_id;
    }

    public User getUser() {
        return user;
    }

    public void setUser(User user) {
        this.user = user;
    }
    public Cleaning_Management getCleaning_management() {
        return cleaning_management;
    }

    public void setCleaning_management(Cleaning_Management cleaning_management) {
        this.cleaning_management = cleaning_management;
    }

}