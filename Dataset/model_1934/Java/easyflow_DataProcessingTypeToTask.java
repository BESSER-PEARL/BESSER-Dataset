





import java.util.List;
import java.util.ArrayList;

public class easyflow_DataProcessingTypeToTask  {






    private List<easyflow_Task> easyflow_tasks;




    private easyflow_DataProcessingType easyflow_dataprocessingtype;




    private easyflow_Workflow easyflow_workflow;


    public easyflow_DataProcessingTypeToTask(
    ) {
        this.easyflow_tasks = new ArrayList<>();
    }

    public easyflow_DataProcessingTypeToTask(
        ArrayList<easyflow_Task> easyflow_tasks    ) {
        this.easyflow_tasks = easyflow_tasks;
    }


    public List<easyflow_Task> getEasyflow_tasks() {
        return easyflow_tasks;
    }

    public void addEasyflow_task(Easyflow_task easyflow_task) {
        this.easyflow_tasks.add(easyflow_task);
    }
    public easyflow_DataProcessingType getEasyflow_dataprocessingtype() {
        return easyflow_dataprocessingtype;
    }

    public void setEasyflow_dataprocessingtype(easyflow_DataProcessingType easyflow_dataprocessingtype) {
        this.easyflow_dataprocessingtype = easyflow_dataprocessingtype;
    }
    public easyflow_Workflow getEasyflow_workflow() {
        return easyflow_workflow;
    }

    public void setEasyflow_workflow(easyflow_Workflow easyflow_workflow) {
        this.easyflow_workflow = easyflow_workflow;
    }

}