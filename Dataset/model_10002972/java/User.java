





import java.util.List;
import java.util.ArrayList;

public class User  {

    private String location;
    private String email;





    private List<Request> requests;


    public User(
        String location,        String email    ) {
        this.location = location;
        this.email = email;
        this.requests = new ArrayList<>();
    }

    public User(
        String location,        String email        ArrayList<Request> requests    ) {
        this.location = location;
        this.email = email;
        this.requests = requests;
    }

    public String getLocation() {
        return location;
    }

    public void setLocation(String location) {
        this.location = location;
    }
    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }

    public List<Request> getRequests() {
        return requests;
    }

    public void addRequest(Request request) {
        this.requests.add(request);
    }

}