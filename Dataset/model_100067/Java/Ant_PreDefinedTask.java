





import java.util.List;
import java.util.ArrayList;

public class Ant_PreDefinedTask extends Task {

    private String id;
    private String taskname;
    private String description;



    public Ant_PreDefinedTask(
        String id,        String taskname,        String description    ) {
        super(
        );
        this.id = id;
        this.taskname = taskname;
        this.description = description;
    }


    public String getId() {
        return id;
    }

    public void setId(String id) {
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


}