





import java.util.List;
import java.util.ArrayList;

public class System  {

    private String id;
    private String session;
    private String name;





    private User user;


    public System(
        String id,        String session,        String name    ) {
        this.id = id;
        this.session = session;
        this.name = name;
    }


    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getSession() {
        return session;
    }

    public void setSession(String session) {
        this.session = session;
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