





import java.util.List;
import java.util.ArrayList;

public class builds_User extends BuildElement {

    private String email;
    private String id;



    public builds_User(
        String email,        String id    ) {
        super(
        );
        this.email = email;
        this.id = id;
    }


    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }


}