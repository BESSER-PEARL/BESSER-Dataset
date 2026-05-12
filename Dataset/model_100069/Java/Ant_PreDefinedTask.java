





import java.util.List;
import java.util.ArrayList;

public class Ant_PreDefinedTask extends Task {

    private String id;
    private String description;
    private String taskname;



    public Ant_PreDefinedTask(
        String id,        String description,        String taskname    ) {
        super(
        );
        this.id = id;
        this.description = description;
        this.taskname = taskname;
    }


    public String getId() {
        return id;
    }

    public void setId(String id) {
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


}