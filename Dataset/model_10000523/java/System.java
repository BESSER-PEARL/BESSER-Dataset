





import java.util.List;
import java.util.ArrayList;

public class System  {

    private String session;
    private String id;
    private String name;





    private User user;


    public System(
        String session,        String id,        String name    ) {
        this.session = session;
        this.id = id;
        this.name = name;
    }


    public String getSession() {
        return session;
    }

    public void setSession(String session) {
        this.session = session;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public User getUser() {
        return user;
    }

    public void setUser(User user) {
        this.user = user;
    }

}