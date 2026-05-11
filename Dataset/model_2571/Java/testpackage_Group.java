





import java.util.List;
import java.util.ArrayList;

public class testpackage_Group extends NamedElement {






    private List<testpackage_User> testpackage_users;


    public testpackage_Group(
    ) {
        super(
        );
        this.testpackage_users = new ArrayList<>();
    }

    public testpackage_Group(
        ArrayList<testpackage_User> testpackage_users    ) {
        this.testpackage_users = testpackage_users;
    }


    public List<testpackage_User> getTestpackage_users() {
        return testpackage_users;
    }

    public void addTestpackage_user(Testpackage_user testpackage_user) {
        this.testpackage_users.add(testpackage_user);
    }

}