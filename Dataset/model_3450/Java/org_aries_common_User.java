





import java.util.List;
import java.util.ArrayList;

public class org_aries_common_User  {

    private String firstName;
    private String id;
    private String lastName;
    private String enabled;
    private String password;
    private String userId;



    public org_aries_common_User(
        String firstName,        String id,        String lastName,        String enabled,        String password,        String userId    ) {
        this.firstName = firstName;
        this.id = id;
        this.lastName = lastName;
        this.enabled = enabled;
        this.password = password;
        this.userId = userId;
    }


    public String getFirstname() {
        return firstName;
    }

    public void setFirstname(String firstName) {
        this.firstName = firstName;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getLastname() {
        return lastName;
    }

    public void setLastname(String lastName) {
        this.lastName = lastName;
    }
    public String getEnabled() {
        return enabled;
    }

    public void setEnabled(String enabled) {
        this.enabled = enabled;
    }
    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }
    public String getUserid() {
        return userId;
    }

    public void setUserid(String userId) {
        this.userId = userId;
    }


}