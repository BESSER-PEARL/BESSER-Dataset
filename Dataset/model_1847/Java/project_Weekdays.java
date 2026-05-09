





import java.util.List;
import java.util.ArrayList;

public class project_Weekdays  {

    private String last;
    private String first;





    private project_WorkingHours project_workinghours;


    public project_Weekdays(
        String last,        String first    ) {
        this.last = last;
        this.first = first;
    }


    public String getLast() {
        return last;
    }

    public void setLast(String last) {
        this.last = last;
    }
    public String getFirst() {
        return first;
    }

    public void setFirst(String first) {
        this.first = first;
    }

    public project_WorkingHours getProject_workinghours() {
        return project_workinghours;
    }

    public void setProject_workinghours(project_WorkingHours project_workinghours) {
        this.project_workinghours = project_workinghours;
    }

}