





import java.util.List;
import java.util.ArrayList;

public class Browse_Recipes  {

    private String description;
    private String name;





    private User user;


    public Browse_Recipes(
        String description,        String name    ) {
        this.description = description;
        this.name = name;
    }


    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public User getUser() {
        return user;
    }

    public void setUser(User user) {
        this.user = user;
    }

}