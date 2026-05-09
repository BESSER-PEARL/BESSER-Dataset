





import java.util.List;
import java.util.ArrayList;

public class model_User  {

    private String administrator;
    private String surname;
    private String password;
    private String firstName;
    private String receptionist;
    private String id;



    public model_User(
        String administrator,        String surname,        String password,        String firstName,        String receptionist,        String id    ) {
        this.administrator = administrator;
        this.surname = surname;
        this.password = password;
        this.firstName = firstName;
        this.receptionist = receptionist;
        this.id = id;
    }


    public String getAdministrator() {
        return administrator;
    }

    public void setAdministrator(String administrator) {
        this.administrator = administrator;
    }
    public String getSurname() {
        return surname;
    }

    public void setSurname(String surname) {
        this.surname = surname;
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
    public String getReceptionist() {
        return receptionist;
    }

    public void setReceptionist(String receptionist) {
        this.receptionist = receptionist;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }


}