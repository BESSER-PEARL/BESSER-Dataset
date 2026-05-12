





import java.util.List;
import java.util.ArrayList;

public class Ant_Project  {

    private String basedir;
    private String description;
    private String name;





    private Path path;




    private List<Target> targets;




    private Target target;




    private List<Property> propertys;




    private List<TaskDef> taskdefs;


    public Ant_Project(
        String basedir,        String description,        String name    ) {
        this.basedir = basedir;
        this.description = description;
        this.name = name;
        this.targets = new ArrayList<>();
        this.propertys = new ArrayList<>();
        this.taskdefs = new ArrayList<>();
    }

    public Ant_Project(
        String basedir,        String description,        String name        ArrayList<Target> targets,        ArrayList<Property> propertys,        ArrayList<TaskDef> taskdefs    ) {
        this.basedir = basedir;
        this.description = description;
        this.name = name;
        this.targets = targets;
        this.propertys = propertys;
        this.taskdefs = taskdefs;
    }

    public String getBasedir() {
        return basedir;
    }

    public void setBasedir(String basedir) {
        this.basedir = basedir;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public Path getPath() {
        return path;
    }

    public void setPath(Path path) {
        this.path = path;
    }
    public List<Target> getTargets() {
        return targets;
    }

    public void addTarget(Target target) {
        this.targets.add(target);
    }
    public Target getTarget() {
        return target;
    }

    public void setTarget(Target target) {
        this.target = target;
    }
    public List<Property> getPropertys() {
        return propertys;
    }

    public void addProperty(Property property) {
        this.propertys.add(property);
    }
    public List<TaskDef> getTaskdefs() {
        return taskdefs;
    }

    public void addTaskdef(Taskdef taskdef) {
        this.taskdefs.add(taskdef);
    }

}