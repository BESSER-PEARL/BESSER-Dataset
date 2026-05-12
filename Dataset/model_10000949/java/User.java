





import java.util.List;
import java.util.ArrayList;

public class User  {

    private String name;
    private String lastName;



    public User(
        String name,        String lastName    ) {
        this.name = name;
        this.lastName = lastName;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getLastname() {
        return lastName;
    }

    public void setLastname(String lastName) {
        this.lastName = lastName;
    }


}