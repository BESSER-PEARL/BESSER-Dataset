





import java.util.List;
import java.util.ArrayList;

public class Course  {

    private String material;
    private String name;
    private String description;





    private List<User> users;




    private User user;


    public Course(
        String material,        String name,        String description    ) {
        this.material = material;
        this.name = name;
        this.description = description;
        this.users = new ArrayList<>();
    }

    public Course(
        String material,        String name,        String description        ArrayList<User> users    ) {
        this.material = material;
        this.name = name;
        this.description = description;
        this.users = users;
    }

    public String getMaterial() {
        return material;
    }

    public void setMaterial(String material) {
        this.material = material;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    public List<User> getUsers() {
        return users;
    }

    public void addUser(User user) {
        this.users.add(user);
    }
    public User getUser() {
        return user;
    }

    public void setUser(User user) {
        this.user = user;
    }

}