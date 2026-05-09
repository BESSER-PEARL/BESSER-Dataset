





import java.util.List;
import java.util.ArrayList;

public class esmodel_accesscontrol_OrgUnitProperty  {

    private String name;
    private String value;





    private ProjectId projectid;


    public esmodel_accesscontrol_OrgUnitProperty(
        String name,        String value    ) {
        this.name = name;
        this.value = value;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }

    public ProjectId getProjectid() {
        return projectid;
    }

    public void setProjectid(ProjectId projectid) {
        this.projectid = projectid;
    }

}