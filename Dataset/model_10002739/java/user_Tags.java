





import java.util.List;
import java.util.ArrayList;

public class user_Tags  {

    private String id;
    private String name;





    private List<user_Business> user_businesss;


    public user_Tags(
        String id,        String name    ) {
        this.id = id;
        this.name = name;
        this.user_businesss = new ArrayList<>();
    }

    public user_Tags(
        String id,        String name        ArrayList<user_Business> user_businesss    ) {
        this.id = id;
        this.name = name;
        this.user_businesss = user_businesss;
    }

    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<user_Business> getUser_businesss() {
        return user_businesss;
    }

    public void addUser_business(User_business user_business) {
        this.user_businesss.add(user_business);
    }

}