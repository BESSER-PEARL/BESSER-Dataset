





import java.util.List;
import java.util.ArrayList;

public class esmodel_ProjectHistory  {

    private String projectName;
    private String projectDescription;



    public esmodel_ProjectHistory(
        String projectName,        String projectDescription    ) {
        this.projectName = projectName;
        this.projectDescription = projectDescription;
    }


    public String getProjectname() {
        return projectName;
    }

    public void setProjectname(String projectName) {
        this.projectName = projectName;
    }
    public String getProjectdescription() {
        return projectDescription;
    }

    public void setProjectdescription(String projectDescription) {
        this.projectDescription = projectDescription;
    }


}