





import java.util.List;
import java.util.ArrayList;

public class HALL_TaskObject extends Component {

    private int completionTime;
    private int numberofgoalscompleted;





    private HALL_UserProfile hall_userprofile;




    private List<HALL_TaskObject> hall_taskobjects;




    private HALL_UserProfile hall_userprofile;




    private HALL_TaskObject hall_taskobject;


    public HALL_TaskObject(
        int completionTime,        int numberofgoalscompleted    ) {
        super(
        );
        this.completionTime = completionTime;
        this.numberofgoalscompleted = numberofgoalscompleted;
        this.hall_taskobjects = new ArrayList<>();
    }

    public HALL_TaskObject(
        int completionTime,        int numberofgoalscompleted        ArrayList<HALL_TaskObject> hall_taskobjects    ) {
        this.completionTime = completionTime;
        this.numberofgoalscompleted = numberofgoalscompleted;
        this.hall_taskobjects = hall_taskobjects;
    }

    public int getCompletiontime() {
        return completionTime;
    }

    public void setCompletiontime(int completionTime) {
        this.completionTime = completionTime;
    }
    public int getNumberofgoalscompleted() {
        return numberofgoalscompleted;
    }

    public void setNumberofgoalscompleted(int numberofgoalscompleted) {
        this.numberofgoalscompleted = numberofgoalscompleted;
    }

    public HALL_UserProfile getHall_userprofile() {
        return hall_userprofile;
    }

    public void setHall_userprofile(HALL_UserProfile hall_userprofile) {
        this.hall_userprofile = hall_userprofile;
    }
    public List<HALL_TaskObject> getHall_taskobjects() {
        return hall_taskobjects;
    }

    public void addHall_taskobject(Hall_taskobject hall_taskobject) {
        this.hall_taskobjects.add(hall_taskobject);
    }
    public HALL_UserProfile getHall_userprofile() {
        return hall_userprofile;
    }

    public void setHall_userprofile(HALL_UserProfile hall_userprofile) {
        this.hall_userprofile = hall_userprofile;
    }
    public HALL_TaskObject getHall_taskobject() {
        return hall_taskobject;
    }

    public void setHall_taskobject(HALL_TaskObject hall_taskobject) {
        this.hall_taskobject = hall_taskobject;
    }

}