





import java.util.List;
import java.util.ArrayList;

public class spem_TeamProfile extends BreakdownElement {






    private List<spem_TeamProfile> spem_teamprofiles;




    private spem_TeamProfile spem_teamprofile;


    public spem_TeamProfile(
    ) {
        super(
        );
        this.spem_teamprofiles = new ArrayList<>();
    }

    public spem_TeamProfile(
        ArrayList<spem_TeamProfile> spem_teamprofiles    ) {
        this.spem_teamprofiles = spem_teamprofiles;
    }


    public List<spem_TeamProfile> getSpem_teamprofiles() {
        return spem_teamprofiles;
    }

    public void addSpem_teamprofile(Spem_teamprofile spem_teamprofile) {
        this.spem_teamprofiles.add(spem_teamprofile);
    }
    public spem_TeamProfile getSpem_teamprofile() {
        return spem_teamprofile;
    }

    public void setSpem_teamprofile(spem_TeamProfile spem_teamprofile) {
        this.spem_teamprofile = spem_teamprofile;
    }

}