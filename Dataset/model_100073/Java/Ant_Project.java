





import java.util.List;
import java.util.ArrayList;

public class Ant_Project  {

    private String name;
    private String basedir;
    private String description;





    private List<TaskDef> taskdefs;




    private List<Target> targets;




    private Path path;




    private List<Property> propertys;




    private Target target;


    public Ant_Project(
        String name,        String basedir,        String description    ) {
        this.name = name;
        this.basedir = basedir;
        this.description = description;
        this.taskdefs = new ArrayList<>();
        this.targets = new ArrayList<>();
        this.propertys = new ArrayList<>();
    }

    public Ant_Project(
        String name,        String basedir,        String description        ArrayList<TaskDef> taskdefs,        ArrayList<Target> targets,        ArrayList<Property> propertys    ) {
        this.name = name;
        this.basedir = basedir;
        this.description = description;
        this.taskdefs = taskdefs;
        this.targets = targets;
        this.propertys = propertys;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
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

    public List<TaskDef> getTaskdefs() {
        return taskdefs;
    }

    public void addTaskdef(Taskdef taskdef) {
        this.taskdefs.add(taskdef);
    }
    public List<Target> getTargets() {
        return targets;
    }

    public void addTarget(Target target) {
        this.targets.add(target);
    }
    public Path getPath() {
        return path;
    }

    public void setPath(Path path) {
        this.path = path;
    }
    public List<Property> getPropertys() {
        return propertys;
    }

    public void addProperty(Property property) {
        this.propertys.add(property);
    }
    public Target getTarget() {
        return target;
    }

    public void setTarget(Target target) {
        this.target = target;
    }

}