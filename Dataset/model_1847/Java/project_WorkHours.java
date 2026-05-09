





import java.util.List;
import java.util.ArrayList;

public class project_WorkHours  {

    private String start;
    private String stop;





    private project_WorkingHours project_workinghours;


    public project_WorkHours(
        String start,        String stop    ) {
        this.start = start;
        this.stop = stop;
    }


    public String getStart() {
        return start;
    }

    public void setStart(String start) {
        this.start = start;
    }
    public String getStop() {
        return stop;
    }

    public void setStop(String stop) {
        this.stop = stop;
    }

    public project_WorkingHours getProject_workinghours() {
        return project_workinghours;
    }

    public void setProject_workinghours(project_WorkingHours project_workinghours) {
        this.project_workinghours = project_workinghours;
    }

}