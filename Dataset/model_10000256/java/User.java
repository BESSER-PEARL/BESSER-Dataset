





import java.util.List;
import java.util.ArrayList;

public class User  {

    private String email;
    private String location;





    private Administrator administrator;




    private List<Request> requests;


    public User(
        String email,        String location    ) {
        this.email = email;
        this.location = location;
        this.requests = new ArrayList<>();
    }

    public User(
        String email,        String location        ArrayList<Request> requests    ) {
        this.email = email;
        this.location = location;
        this.requests = requests;
    }

    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }
    public String getLocation() {
        return location;
    }

    public void setLocation(String location) {
        this.location = location;
    }

    public Administrator getAdministrator() {
        return administrator;
    }

    public void setAdministrator(Administrator administrator) {
        this.administrator = administrator;
    }
    public List<Request> getRequests() {
        return requests;
    }

    public void addRequest(Request request) {
        this.requests.add(request);
    }

}