





import java.util.List;
import java.util.ArrayList;

public class Package_Expense  {

    private String user_id;
    private String id;
    private String project_id;
    private String mission_id;
    private String manager_id;



    public Package_Expense(
        String user_id,        String id,        String project_id,        String mission_id,        String manager_id    ) {
        this.user_id = user_id;
        this.id = id;
        this.project_id = project_id;
        this.mission_id = mission_id;
        this.manager_id = manager_id;
    }


    public String getUser_id() {
        return user_id;
    }

    public void setUser_id(String user_id) {
        this.user_id = user_id;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getProject_id() {
        return project_id;
    }

    public void setProject_id(String project_id) {
        this.project_id = project_id;
    }
    public String getMission_id() {
        return mission_id;
    }

    public void setMission_id(String mission_id) {
        this.mission_id = mission_id;
    }
    public String getManager_id() {
        return manager_id;
    }

    public void setManager_id(String manager_id) {
        this.manager_id = manager_id;
    }


}