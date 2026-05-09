





import java.util.List;
import java.util.ArrayList;

public class mancoosimm_Group extends NamedElement {






    private List<mancoosimm_User> mancoosimm_users;




    private mancoosimm_User mancoosimm_user;




    private mancoosimm_Environment mancoosimm_environment;




    private mancoosimm_Environment mancoosimm_environment;




    private mancoosimm_File mancoosimm_file;


    public mancoosimm_Group(
    ) {
        super(
        );
        this.mancoosimm_users = new ArrayList<>();
    }

    public mancoosimm_Group(
        ArrayList<mancoosimm_User> mancoosimm_users    ) {
        this.mancoosimm_users = mancoosimm_users;
    }


    public List<mancoosimm_User> getMancoosimm_users() {
        return mancoosimm_users;
    }

    public void addMancoosimm_user(Mancoosimm_user mancoosimm_user) {
        this.mancoosimm_users.add(mancoosimm_user);
    }
    public mancoosimm_User getMancoosimm_user() {
        return mancoosimm_user;
    }

    public void setMancoosimm_user(mancoosimm_User mancoosimm_user) {
        this.mancoosimm_user = mancoosimm_user;
    }
    public mancoosimm_Environment getMancoosimm_environment() {
        return mancoosimm_environment;
    }

    public void setMancoosimm_environment(mancoosimm_Environment mancoosimm_environment) {
        this.mancoosimm_environment = mancoosimm_environment;
    }
    public mancoosimm_Environment getMancoosimm_environment() {
        return mancoosimm_environment;
    }

    public void setMancoosimm_environment(mancoosimm_Environment mancoosimm_environment) {
        this.mancoosimm_environment = mancoosimm_environment;
    }
    public mancoosimm_File getMancoosimm_file() {
        return mancoosimm_file;
    }

    public void setMancoosimm_file(mancoosimm_File mancoosimm_file) {
        this.mancoosimm_file = mancoosimm_file;
    }

}