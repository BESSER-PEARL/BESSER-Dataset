





import java.util.List;
import java.util.ArrayList;

public class org_aries_common_EmailAccount  {

    private String password;
    private String firstName;
    private String enabled;
    private String lastName;
    private String userId;
    private String id;



    public org_aries_common_EmailAccount(
        String password,        String firstName,        String enabled,        String lastName,        String userId,        String id    ) {
        this.password = password;
        this.firstName = firstName;
        this.enabled = enabled;
        this.lastName = lastName;
        this.userId = userId;
        this.id = id;
    }


    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }
    public String getFirstname() {
        return firstName;
    }

    public void setFirstname(String firstName) {
        this.firstName = firstName;
    }
    public String getEnabled() {
        return enabled;
    }

    public void setEnabled(String enabled) {
        this.enabled = enabled;
    }
    public String getLastname() {
        return lastName;
    }

    public void setLastname(String lastName) {
        this.lastName = lastName;
    }
    public String getUserid() {
        return userId;
    }

    public void setUserid(String userId) {
        this.userId = userId;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }


}