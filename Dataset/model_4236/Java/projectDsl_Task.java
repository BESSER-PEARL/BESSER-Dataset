





import java.util.List;
import java.util.ArrayList;

public class projectDsl_Task  {

    private String type;
    private String name;





    private projectDsl_Project projectdsl_project;


    public projectDsl_Task(
        String type,        String name    ) {
        this.type = type;
        this.name = name;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public projectDsl_Project getProjectdsl_project() {
        return projectdsl_project;
    }

    public void setProjectdsl_project(projectDsl_Project projectdsl_project) {
        this.projectdsl_project = projectdsl_project;
    }

}