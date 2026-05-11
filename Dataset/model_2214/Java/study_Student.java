





import java.util.List;
import java.util.ArrayList;

public class study_Student  {

    private String username;
    private String name;



    public study_Student(
        String username,        String name    ) {
        this.username = username;
        this.name = name;
    }


    public String getUsername() {
        return username;
    }

    public void setUsername(String username) {
        this.username = username;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}