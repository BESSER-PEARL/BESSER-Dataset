





import java.util.List;
import java.util.ArrayList;

public class Task  {

    private String Deadline;
    private String Task_Name;
    private String Name;
    private String Task_Detail;



    public Task(
        String Deadline,        String Task_Name,        String Name,        String Task_Detail    ) {
        this.Deadline = Deadline;
        this.Task_Name = Task_Name;
        this.Name = Name;
        this.Task_Detail = Task_Detail;
    }


    public String getDeadline() {
        return Deadline;
    }

    public void setDeadline(String Deadline) {
        this.Deadline = Deadline;
    }
    public String getTask_name() {
        return Task_Name;
    }

    public void setTask_name(String Task_Name) {
        this.Task_Name = Task_Name;
    }
    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }
    public String getTask_detail() {
        return Task_Detail;
    }

    public void setTask_detail(String Task_Detail) {
        this.Task_Detail = Task_Detail;
    }


}