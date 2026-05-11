





import java.util.List;
import java.util.ArrayList;

public class remember_Task extends Node {

    private String priority;
    private String budget;
    private int taskId;
    private String status;
    private String text;
    private boolean done;





    private remember_Folder remember_folder;




    private remember_Folder remember_folder;


    public remember_Task(
        String priority,        String budget,        int taskId,        String status,        String text,        boolean done    ) {
        super(
        );
        this.priority = priority;
        this.budget = budget;
        this.taskId = taskId;
        this.status = status;
        this.text = text;
        this.done = done;
    }


    public String getPriority() {
        return priority;
    }

    public void setPriority(String priority) {
        this.priority = priority;
    }
    public String getBudget() {
        return budget;
    }

    public void setBudget(String budget) {
        this.budget = budget;
    }
    public int getTaskid() {
        return taskId;
    }

    public void setTaskid(int taskId) {
        this.taskId = taskId;
    }
    public String getStatus() {
        return status;
    }

    public void setStatus(String status) {
        this.status = status;
    }
    public String getText() {
        return text;
    }

    public void setText(String text) {
        this.text = text;
    }
    public boolean getDone() {
        return done;
    }

    public void setDone(boolean done) {
        this.done = done;
    }

    public remember_Folder getRemember_folder() {
        return remember_folder;
    }

    public void setRemember_folder(remember_Folder remember_folder) {
        this.remember_folder = remember_folder;
    }
    public remember_Folder getRemember_folder() {
        return remember_folder;
    }

    public void setRemember_folder(remember_Folder remember_folder) {
        this.remember_folder = remember_folder;
    }

}