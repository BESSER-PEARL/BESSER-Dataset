





import java.util.List;
import java.util.ArrayList;

public class project_Interval2  {

    private String end;
    private String start;





    private project_Period project_period;




    private project_Project project_project;


    public project_Interval2(
        String end,        String start    ) {
        this.end = end;
        this.start = start;
    }


    public String getEnd() {
        return end;
    }

    public void setEnd(String end) {
        this.end = end;
    }
    public String getStart() {
        return start;
    }

    public void setStart(String start) {
        this.start = start;
    }

    public project_Period getProject_period() {
        return project_period;
    }

    public void setProject_period(project_Period project_period) {
        this.project_period = project_period;
    }
    public project_Project getProject_project() {
        return project_project;
    }

    public void setProject_project(project_Project project_project) {
        this.project_project = project_project;
    }

}