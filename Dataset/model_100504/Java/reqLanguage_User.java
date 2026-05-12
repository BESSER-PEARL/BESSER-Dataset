





import java.util.List;
import java.util.ArrayList;

public class reqLanguage_User  {

    private String name;
    private String user;



    public reqLanguage_User(
        String name,        String user    ) {
        this.name = name;
        this.user = user;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getUser() {
        return user;
    }

    public void setUser(String user) {
        this.user = user;
    }


}