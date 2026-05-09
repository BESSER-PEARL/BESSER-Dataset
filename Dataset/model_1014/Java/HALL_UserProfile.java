





import java.util.List;
import java.util.ArrayList;

public class HALL_UserProfile extends Component {

    private int numberofcompletedtasks;





    private HALL_UserProfile hall_userprofile;




    private List<HALL_UserProfile> hall_userprofiles;


    public HALL_UserProfile(
        int numberofcompletedtasks    ) {
        super(
        );
        this.numberofcompletedtasks = numberofcompletedtasks;
        this.hall_userprofiles = new ArrayList<>();
    }

    public HALL_UserProfile(
        int numberofcompletedtasks        ArrayList<HALL_UserProfile> hall_userprofiles    ) {
        this.numberofcompletedtasks = numberofcompletedtasks;
        this.hall_userprofiles = hall_userprofiles;
    }

    public int getNumberofcompletedtasks() {
        return numberofcompletedtasks;
    }

    public void setNumberofcompletedtasks(int numberofcompletedtasks) {
        this.numberofcompletedtasks = numberofcompletedtasks;
    }

    public HALL_UserProfile getHall_userprofile() {
        return hall_userprofile;
    }

    public void setHall_userprofile(HALL_UserProfile hall_userprofile) {
        this.hall_userprofile = hall_userprofile;
    }
    public List<HALL_UserProfile> getHall_userprofiles() {
        return hall_userprofiles;
    }

    public void addHall_userprofile(Hall_userprofile hall_userprofile) {
        this.hall_userprofiles.add(hall_userprofile);
    }

}