





import java.util.List;
import java.util.ArrayList;

public class esmodel_ServerSpace  {






    private List<accesscontrol_ACUser> accesscontrol_acusers;


    public esmodel_ServerSpace(
    ) {
        this.accesscontrol_acusers = new ArrayList<>();
    }

    public esmodel_ServerSpace(
        ArrayList<accesscontrol_ACUser> accesscontrol_acusers    ) {
        this.accesscontrol_acusers = accesscontrol_acusers;
    }


    public List<accesscontrol_ACUser> getAccesscontrol_acusers() {
        return accesscontrol_acusers;
    }

    public void addAccesscontrol_acuser(Accesscontrol_acuser accesscontrol_acuser) {
        this.accesscontrol_acusers.add(accesscontrol_acuser);
    }

}