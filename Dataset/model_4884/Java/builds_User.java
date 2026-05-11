





import java.util.List;
import java.util.ArrayList;

public class builds_User extends BuildElement {

    private String id;
    private String email;



    public builds_User(
        String id,        String email    ) {
        super(
        );
        this.id = id;
        this.email = email;
    }


    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }


}