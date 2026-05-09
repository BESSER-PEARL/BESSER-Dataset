





import java.util.List;
import java.util.ArrayList;

public class project_Extend  {

    private boolean scenariospecific;
    private String id;
    private boolean inherit;
    private String name;





    private project_ExtendedTaskAttribute project_extendedtaskattribute;




    private project_ExtendTask project_extendtask;




    private project_ExtendedResourceAttribute project_extendedresourceattribute;




    private project_ExtendResource project_extendresource;


    public project_Extend(
        boolean scenariospecific,        String id,        boolean inherit,        String name    ) {
        this.scenariospecific = scenariospecific;
        this.id = id;
        this.inherit = inherit;
        this.name = name;
    }


    public boolean getScenariospecific() {
        return scenariospecific;
    }

    public void setScenariospecific(boolean scenariospecific) {
        this.scenariospecific = scenariospecific;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public boolean getInherit() {
        return inherit;
    }

    public void setInherit(boolean inherit) {
        this.inherit = inherit;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public project_ExtendedTaskAttribute getProject_extendedtaskattribute() {
        return project_extendedtaskattribute;
    }

    public void setProject_extendedtaskattribute(project_ExtendedTaskAttribute project_extendedtaskattribute) {
        this.project_extendedtaskattribute = project_extendedtaskattribute;
    }
    public project_ExtendTask getProject_extendtask() {
        return project_extendtask;
    }

    public void setProject_extendtask(project_ExtendTask project_extendtask) {
        this.project_extendtask = project_extendtask;
    }
    public project_ExtendedResourceAttribute getProject_extendedresourceattribute() {
        return project_extendedresourceattribute;
    }

    public void setProject_extendedresourceattribute(project_ExtendedResourceAttribute project_extendedresourceattribute) {
        this.project_extendedresourceattribute = project_extendedresourceattribute;
    }
    public project_ExtendResource getProject_extendresource() {
        return project_extendresource;
    }

    public void setProject_extendresource(project_ExtendResource project_extendresource) {
        this.project_extendresource = project_extendresource;
    }

}