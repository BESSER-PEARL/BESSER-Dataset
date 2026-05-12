





import java.util.List;
import java.util.ArrayList;

public class Account  {

    private String password;
    private String name;
    private String entity;
    private String email;



    public Account(
        String password,        String name,        String entity,        String email    ) {
        this.password = password;
        this.name = name;
        this.entity = entity;
        this.email = email;
    }


    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getEntity() {
        return entity;
    }

    public void setEntity(String entity) {
        this.entity = entity;
    }
    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }


}