





import java.util.List;
import java.util.ArrayList;

public class project_TaskStatusSheet extends StatusSheetAttribute, TaskStatusSheetAttribute {






    private project_Task project_task;


    public project_TaskStatusSheet(
    ) {
        super(
        );
    }



    public project_Task getProject_task() {
        return project_task;
    }

    public void setProject_task(project_Task project_task) {
        this.project_task = project_task;
    }

}