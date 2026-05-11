





import java.util.List;
import java.util.ArrayList;

public class camel_organisation_User extends Entity {

    private String firstName;
    private String email;
    private String www;
    private String lastName;
    private String name;



    public camel_organisation_User(
        String firstName,        String email,        String www,        String lastName,        String name    ) {
        super(
        );
        this.firstName = firstName;
        this.email = email;
        this.www = www;
        this.lastName = lastName;
        this.name = name;
    }


    public String getFirstname() {
        return firstName;
    }

    public void setFirstname(String firstName) {
        this.firstName = firstName;
    }
    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }
    public String getWww() {
        return www;
    }

    public void setWww(String www) {
        this.www = www;
    }
    public String getLastname() {
        return lastName;
    }

    public void setLastname(String lastName) {
        this.lastName = lastName;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}