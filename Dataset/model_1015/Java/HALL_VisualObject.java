





import java.util.List;
import java.util.ArrayList;

public class HALL_VisualObject extends Component {






    private HALL_UserProfile hall_userprofile;




    private HALL_UserProfile hall_userprofile;




    private HALL_VisualObject hall_visualobject;




    private List<HALL_VisualObject> hall_visualobjects;


    public HALL_VisualObject(
    ) {
        super(
        );
        this.hall_visualobjects = new ArrayList<>();
    }

    public HALL_VisualObject(
        ArrayList<HALL_VisualObject> hall_visualobjects    ) {
        this.hall_visualobjects = hall_visualobjects;
    }


    public HALL_UserProfile getHall_userprofile() {
        return hall_userprofile;
    }

    public void setHall_userprofile(HALL_UserProfile hall_userprofile) {
        this.hall_userprofile = hall_userprofile;
    }
    public HALL_UserProfile getHall_userprofile() {
        return hall_userprofile;
    }

    public void setHall_userprofile(HALL_UserProfile hall_userprofile) {
        this.hall_userprofile = hall_userprofile;
    }
    public HALL_VisualObject getHall_visualobject() {
        return hall_visualobject;
    }

    public void setHall_visualobject(HALL_VisualObject hall_visualobject) {
        this.hall_visualobject = hall_visualobject;
    }
    public List<HALL_VisualObject> getHall_visualobjects() {
        return hall_visualobjects;
    }

    public void addHall_visualobject(Hall_visualobject hall_visualobject) {
        this.hall_visualobjects.add(hall_visualobject);
    }

}