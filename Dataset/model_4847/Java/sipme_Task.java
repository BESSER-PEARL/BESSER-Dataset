





import java.util.List;
import java.util.ArrayList;

public class sipme_Task extends EnterpriseProcessor {

    private int taskDuration;





    private List<sipme_Task> sipme_tasks;




    private sipme_BusinessRules sipme_businessrules;




    private sipme_Activity sipme_activity;




    private sipme_EnterpriseResource sipme_enterpriseresource;




    private sipme_Activity sipme_activity;


    public sipme_Task(
        int taskDuration    ) {
        super(
        );
        this.taskDuration = taskDuration;
        this.sipme_tasks = new ArrayList<>();
    }

    public sipme_Task(
        int taskDuration        ArrayList<sipme_Task> sipme_tasks    ) {
        this.taskDuration = taskDuration;
        this.sipme_tasks = sipme_tasks;
    }

    public int getTaskduration() {
        return taskDuration;
    }

    public void setTaskduration(int taskDuration) {
        this.taskDuration = taskDuration;
    }

    public List<sipme_Task> getSipme_tasks() {
        return sipme_tasks;
    }

    public void addSipme_task(Sipme_task sipme_task) {
        this.sipme_tasks.add(sipme_task);
    }
    public sipme_BusinessRules getSipme_businessrules() {
        return sipme_businessrules;
    }

    public void setSipme_businessrules(sipme_BusinessRules sipme_businessrules) {
        this.sipme_businessrules = sipme_businessrules;
    }
    public sipme_Activity getSipme_activity() {
        return sipme_activity;
    }

    public void setSipme_activity(sipme_Activity sipme_activity) {
        this.sipme_activity = sipme_activity;
    }
    public sipme_EnterpriseResource getSipme_enterpriseresource() {
        return sipme_enterpriseresource;
    }

    public void setSipme_enterpriseresource(sipme_EnterpriseResource sipme_enterpriseresource) {
        this.sipme_enterpriseresource = sipme_enterpriseresource;
    }
    public sipme_Activity getSipme_activity() {
        return sipme_activity;
    }

    public void setSipme_activity(sipme_Activity sipme_activity) {
        this.sipme_activity = sipme_activity;
    }

}