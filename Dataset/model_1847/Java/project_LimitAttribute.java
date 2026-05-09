





import java.util.List;
import java.util.ArrayList;

public class project_LimitAttribute  {

    private String start;
    private String end;





    private List<project_Resource> project_resources;




    private project_Interval1 project_interval1;




    private project_Limit project_limit;


    public project_LimitAttribute(
        String start,        String end    ) {
        this.start = start;
        this.end = end;
        this.project_resources = new ArrayList<>();
    }

    public project_LimitAttribute(
        String start,        String end        ArrayList<project_Resource> project_resources    ) {
        this.start = start;
        this.end = end;
        this.project_resources = project_resources;
    }

    public String getStart() {
        return start;
    }

    public void setStart(String start) {
        this.start = start;
    }
    public String getEnd() {
        return end;
    }

    public void setEnd(String end) {
        this.end = end;
    }

    public List<project_Resource> getProject_resources() {
        return project_resources;
    }

    public void addProject_resource(Project_resource project_resource) {
        this.project_resources.add(project_resource);
    }
    public project_Interval1 getProject_interval1() {
        return project_interval1;
    }

    public void setProject_interval1(project_Interval1 project_interval1) {
        this.project_interval1 = project_interval1;
    }
    public project_Limit getProject_limit() {
        return project_limit;
    }

    public void setProject_limit(project_Limit project_limit) {
        this.project_limit = project_limit;
    }

}