





import java.util.List;
import java.util.ArrayList;

public class project_Defintions extends Definitions {

    private boolean tasks;
    private boolean resources;
    private boolean flags;
    private boolean project;
    private boolean projectids;



    public project_Defintions(
        boolean tasks,        boolean resources,        boolean flags,        boolean project,        boolean projectids    ) {
        super(
        );
        this.tasks = tasks;
        this.resources = resources;
        this.flags = flags;
        this.project = project;
        this.projectids = projectids;
    }


    public boolean getTasks() {
        return tasks;
    }

    public void setTasks(boolean tasks) {
        this.tasks = tasks;
    }
    public boolean getResources() {
        return resources;
    }

    public void setResources(boolean resources) {
        this.resources = resources;
    }
    public boolean getFlags() {
        return flags;
    }

    public void setFlags(boolean flags) {
        this.flags = flags;
    }
    public boolean getProject() {
        return project;
    }

    public void setProject(boolean project) {
        this.project = project;
    }
    public boolean getProjectids() {
        return projectids;
    }

    public void setProjectids(boolean projectids) {
        this.projectids = projectids;
    }


}