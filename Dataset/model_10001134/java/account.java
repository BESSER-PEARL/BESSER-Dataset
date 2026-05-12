





import java.util.List;
import java.util.ArrayList;

public class account  {

    private String office;
    private int id;
    private String password;
    private String username;





    private Person person;


    public account(
        String office,        int id,        String password,        String username    ) {
        this.office = office;
        this.id = id;
        this.password = password;
        this.username = username;
    }


    public String getOffice() {
        return office;
    }

    public void setOffice(String office) {
        this.office = office;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }
    public String getUsername() {
        return username;
    }

    public void setUsername(String username) {
        this.username = username;
    }

    public Person getPerson() {
        return person;
    }

    public void setPerson(Person person) {
        this.person = person;
    }

}