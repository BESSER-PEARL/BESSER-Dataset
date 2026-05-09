





import java.util.List;
import java.util.ArrayList;

public class spem_TeamProfile extends BreakdownElement {






    private List<spem_RoleUse> spem_roleuses;




    private spem_TeamProfile spem_teamprofile;




    private spem_TeamProfile spem_teamprofile;


    public spem_TeamProfile(
    ) {
        super(
        );
        this.spem_roleuses = new ArrayList<>();
    }

    public spem_TeamProfile(
        ArrayList<spem_RoleUse> spem_roleuses    ) {
        this.spem_roleuses = spem_roleuses;
    }


    public List<spem_RoleUse> getSpem_roleuses() {
        return spem_roleuses;
    }

    public void addSpem_roleuse(Spem_roleuse spem_roleuse) {
        this.spem_roleuses.add(spem_roleuse);
    }
    public spem_TeamProfile getSpem_teamprofile() {
        return spem_teamprofile;
    }

    public void setSpem_teamprofile(spem_TeamProfile spem_teamprofile) {
        this.spem_teamprofile = spem_teamprofile;
    }
    public spem_TeamProfile getSpem_teamprofile() {
        return spem_teamprofile;
    }

    public void setSpem_teamprofile(spem_TeamProfile spem_teamprofile) {
        this.spem_teamprofile = spem_teamprofile;
    }

}