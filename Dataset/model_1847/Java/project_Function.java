





import java.util.List;
import java.util.ArrayList;

public class project_Function  {

    private String date;
    private String parentId;
    private int distance;
    private int level;





    private project_Resource project_resource;




    private project_Task project_task;




    private project_Scenario project_scenario;


    public project_Function(
        String date,        String parentId,        int distance,        int level    ) {
        this.date = date;
        this.parentId = parentId;
        this.distance = distance;
        this.level = level;
    }


    public String getDate() {
        return date;
    }

    public void setDate(String date) {
        this.date = date;
    }
    public String getParentid() {
        return parentId;
    }

    public void setParentid(String parentId) {
        this.parentId = parentId;
    }
    public int getDistance() {
        return distance;
    }

    public void setDistance(int distance) {
        this.distance = distance;
    }
    public int getLevel() {
        return level;
    }

    public void setLevel(int level) {
        this.level = level;
    }

    public project_Resource getProject_resource() {
        return project_resource;
    }

    public void setProject_resource(project_Resource project_resource) {
        this.project_resource = project_resource;
    }
    public project_Task getProject_task() {
        return project_task;
    }

    public void setProject_task(project_Task project_task) {
        this.project_task = project_task;
    }
    public project_Scenario getProject_scenario() {
        return project_scenario;
    }

    public void setProject_scenario(project_Scenario project_scenario) {
        this.project_scenario = project_scenario;
    }

}