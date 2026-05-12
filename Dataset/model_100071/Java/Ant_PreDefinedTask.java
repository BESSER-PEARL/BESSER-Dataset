





import java.util.List;
import java.util.ArrayList;

public class Ant_PreDefinedTask extends Task {

    private String taskname;
    private String description;
    private String id;



    public Ant_PreDefinedTask(
        String taskname,        String description,        String id    ) {
        super(
        );
        this.taskname = taskname;
        this.description = description;
        this.id = id;
    }


    public String getTaskname() {
        return taskname;
    }

    public void setTaskname(String taskname) {
        this.taskname = taskname;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }


}