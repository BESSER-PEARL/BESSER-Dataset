





import java.util.List;
import java.util.ArrayList;

public class ADMIN  {

    private String password;
    private String id;





    private List<PARENT> parents;


    public ADMIN(
        String password,        String id    ) {
        this.password = password;
        this.id = id;
        this.parents = new ArrayList<>();
    }

    public ADMIN(
        String password,        String id        ArrayList<PARENT> parents    ) {
        this.password = password;
        this.id = id;
        this.parents = parents;
    }

    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public List<PARENT> getParents() {
        return parents;
    }

    public void addParent(Parent parent) {
        this.parents.add(parent);
    }

}