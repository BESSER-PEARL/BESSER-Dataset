





import java.util.List;
import java.util.ArrayList;

public class librarian  {

    private int username;
    private String name;



    public librarian(
        int username,        String name    ) {
        this.username = username;
        this.name = name;
    }


    public int getUsername() {
        return username;
    }

    public void setUsername(int username) {
        this.username = username;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}