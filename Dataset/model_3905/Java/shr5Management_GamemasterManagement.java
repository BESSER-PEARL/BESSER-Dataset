





import java.util.List;
import java.util.ArrayList;

public class shr5Management_GamemasterManagement extends PlayerManagement {






    private List<shr5Management_GruntGroup> shr5management_gruntgroups;


    public shr5Management_GamemasterManagement(
    ) {
        super(
        );
        this.shr5management_gruntgroups = new ArrayList<>();
    }

    public shr5Management_GamemasterManagement(
        ArrayList<shr5Management_GruntGroup> shr5management_gruntgroups    ) {
        this.shr5management_gruntgroups = shr5management_gruntgroups;
    }


    public List<shr5Management_GruntGroup> getShr5management_gruntgroups() {
        return shr5management_gruntgroups;
    }

    public void addShr5management_gruntgroup(Shr5management_gruntgroup shr5management_gruntgroup) {
        this.shr5management_gruntgroups.add(shr5management_gruntgroup);
    }

}