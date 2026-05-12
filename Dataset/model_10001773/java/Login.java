





import java.util.List;
import java.util.ArrayList;

public class Login  {

    private String password;
    private String name;





    private Owner owner;


    public Login(
        String password,        String name    ) {
        this.password = password;
        this.name = name;
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

    public Owner getOwner() {
        return owner;
    }

    public void setOwner(Owner owner) {
        this.owner = owner;
    }

}