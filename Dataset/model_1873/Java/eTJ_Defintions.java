





import java.util.List;
import java.util.ArrayList;

public class eTJ_Defintions extends Definitions {

    private boolean resources;
    private boolean project;
    private boolean projectids;
    private boolean flags;
    private boolean tasks;



    public eTJ_Defintions(
        boolean resources,        boolean project,        boolean projectids,        boolean flags,        boolean tasks    ) {
        super(
        );
        this.resources = resources;
        this.project = project;
        this.projectids = projectids;
        this.flags = flags;
        this.tasks = tasks;
    }


    public boolean getResources() {
        return resources;
    }

    public void setResources(boolean resources) {
        this.resources = resources;
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
    public boolean getFlags() {
        return flags;
    }

    public void setFlags(boolean flags) {
        this.flags = flags;
    }
    public boolean getTasks() {
        return tasks;
    }

    public void setTasks(boolean tasks) {
        this.tasks = tasks;
    }


}