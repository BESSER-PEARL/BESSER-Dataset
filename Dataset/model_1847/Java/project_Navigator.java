





import java.util.List;
import java.util.ArrayList;

public class project_Navigator extends Property {

    private String id;





    private List<project_NavigatorAttribute> project_navigatorattributes;


    public project_Navigator(
        String id    ) {
        super(
        );
        this.id = id;
        this.project_navigatorattributes = new ArrayList<>();
    }

    public project_Navigator(
        String id        ArrayList<project_NavigatorAttribute> project_navigatorattributes    ) {
        this.id = id;
        this.project_navigatorattributes = project_navigatorattributes;
    }

    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public List<project_NavigatorAttribute> getProject_navigatorattributes() {
        return project_navigatorattributes;
    }

    public void addProject_navigatorattribute(Project_navigatorattribute project_navigatorattribute) {
        this.project_navigatorattributes.add(project_navigatorattribute);
    }

}