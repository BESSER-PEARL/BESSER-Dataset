





import java.util.List;
import java.util.ArrayList;

public class Ant_PreDefinedTask extends Task {

    private String taskname;
    private String id;
    private String description;



    public Ant_PreDefinedTask(
        String taskname,        String id,        String description    ) {
        super(
        );
        this.taskname = taskname;
        this.id = id;
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
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }


}