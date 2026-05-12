





import java.util.List;
import java.util.ArrayList;

public class login  {

    private String id;
    private String pass;
    private String name;





    private receptionist receptionist;


    public login(
        String id,        String pass,        String name    ) {
        this.id = id;
        this.pass = pass;
        this.name = name;
    }


    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getPass() {
        return pass;
    }

    public void setPass(String pass) {
        this.pass = pass;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public receptionist getReceptionist() {
        return receptionist;
    }

    public void setReceptionist(receptionist receptionist) {
        this.receptionist = receptionist;
    }

}