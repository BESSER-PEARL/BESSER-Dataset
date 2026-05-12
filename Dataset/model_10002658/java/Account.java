





import java.util.List;
import java.util.ArrayList;

public class Account  {

    private String password;
    private String name;
    private String email;
    private String entity;



    public Account(
        String password,        String name,        String email,        String entity    ) {
        this.password = password;
        this.name = name;
        this.email = email;
        this.entity = entity;
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
    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }
    public String getEntity() {
        return entity;
    }

    public void setEntity(String entity) {
        this.entity = entity;
    }


}