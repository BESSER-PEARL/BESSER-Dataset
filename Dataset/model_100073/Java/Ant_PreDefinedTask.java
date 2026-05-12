





import java.util.List;
import java.util.ArrayList;

public class Ant_PreDefinedTask extends Task {

    private String description;
    private String taskname;
    private String id;



    public Ant_PreDefinedTask(
        String description,        String taskname,        String id    ) {
        super(
        );
        this.description = description;
        this.taskname = taskname;
        this.id = id;
    }


    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public String getTaskname() {
        return taskname;
    }

    public void setTaskname(String taskname) {
        this.taskname = taskname;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }


}