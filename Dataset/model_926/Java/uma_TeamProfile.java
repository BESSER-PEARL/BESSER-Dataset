





import java.util.List;
import java.util.ArrayList;

public class uma_TeamProfile extends BreakdownElement {






    private uma_TeamProfile uma_teamprofile;




    private List<uma_TeamProfile> uma_teamprofiles;


    public uma_TeamProfile(
    ) {
        super(
        );
        this.uma_teamprofiles = new ArrayList<>();
    }

    public uma_TeamProfile(
        ArrayList<uma_TeamProfile> uma_teamprofiles    ) {
        this.uma_teamprofiles = uma_teamprofiles;
    }


    public uma_TeamProfile getUma_teamprofile() {
        return uma_teamprofile;
    }

    public void setUma_teamprofile(uma_TeamProfile uma_teamprofile) {
        this.uma_teamprofile = uma_teamprofile;
    }
    public List<uma_TeamProfile> getUma_teamprofiles() {
        return uma_teamprofiles;
    }

    public void addUma_teamprofile(Uma_teamprofile uma_teamprofile) {
        this.uma_teamprofiles.add(uma_teamprofile);
    }

}