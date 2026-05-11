





import java.util.List;
import java.util.ArrayList;

public class testpackage_Group  {

    private String name;





    private List<testpackage_User> testpackage_users;


    public testpackage_Group(
        String name    ) {
        this.name = name;
        this.testpackage_users = new ArrayList<>();
    }

    public testpackage_Group(
        String name        ArrayList<testpackage_User> testpackage_users    ) {
        this.name = name;
        this.testpackage_users = testpackage_users;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<testpackage_User> getTestpackage_users() {
        return testpackage_users;
    }

    public void addTestpackage_user(Testpackage_user testpackage_user) {
        this.testpackage_users.add(testpackage_user);
    }

}