





import java.util.List;
import java.util.ArrayList;

public class projectDsl_Project  {

    private String type;
    private String name;





    private projectDsl_Company projectdsl_company;


    public projectDsl_Project(
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

    public projectDsl_Company getProjectdsl_company() {
        return projectdsl_company;
    }

    public void setProjectdsl_company(projectDsl_Company projectdsl_company) {
        this.projectdsl_company = projectdsl_company;
    }

}