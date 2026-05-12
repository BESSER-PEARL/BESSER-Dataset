





import java.util.List;
import java.util.ArrayList;

public class User  {

    private String lastName;
    private String name;



    public User(
        String lastName,        String name    ) {
        this.lastName = lastName;
        this.name = name;
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