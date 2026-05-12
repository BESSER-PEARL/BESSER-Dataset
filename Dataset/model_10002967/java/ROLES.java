





import java.util.List;
import java.util.ArrayList;

public class ROLES  {

    private String _id;
    private String name;
    private String createdAt;





    private List<USER> users;


    public ROLES(
        String _id,        String name,        String createdAt    ) {
        this._id = _id;
        this.name = name;
        this.createdAt = createdAt;
        this.users = new ArrayList<>();
    }

    public ROLES(
        String _id,        String name,        String createdAt        ArrayList<USER> users    ) {
        this._id = _id;
        this.name = name;
        this.createdAt = createdAt;
        this.users = users;
    }

    public String get_id() {
        return _id;
    }

    public void set_id(String _id) {
        this._id = _id;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getCreatedat() {
        return createdAt;
    }

    public void setCreatedat(String createdAt) {
        this.createdAt = createdAt;
    }

    public List<USER> getUsers() {
        return users;
    }

    public void addUser(User user) {
        this.users.add(user);
    }

}