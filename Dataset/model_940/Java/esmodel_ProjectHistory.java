





import java.util.List;
import java.util.ArrayList;

public class esmodel_ProjectHistory  {

    private String projectDescription;
    private String projectName;



    public esmodel_ProjectHistory(
        String projectDescription,        String projectName    ) {
        this.projectDescription = projectDescription;
        this.projectName = projectName;
    }


    public String getProjectdescription() {
        return projectDescription;
    }

    public void setProjectdescription(String projectDescription) {
        this.projectDescription = projectDescription;
    }
    public String getProjectname() {
        return projectName;
    }

    public void setProjectname(String projectName) {
        this.projectName = projectName;
    }


}