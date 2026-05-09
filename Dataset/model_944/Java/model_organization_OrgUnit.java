





import java.util.List;
import java.util.ArrayList;

public class model_organization_OrgUnit extends UnicaseModelElement {

    private String acOrgId;





    private List<task_WorkItem> task_workitems;




    private List<task_WorkItem> task_workitems;


    public model_organization_OrgUnit(
        String acOrgId    ) {
        super(
        );
        this.acOrgId = acOrgId;
        this.task_workitems = new ArrayList<>();
        this.task_workitems = new ArrayList<>();
    }

    public model_organization_OrgUnit(
        String acOrgId        ArrayList<task_WorkItem> task_workitems,        ArrayList<task_WorkItem> task_workitems    ) {
        this.acOrgId = acOrgId;
        this.task_workitems = task_workitems;
        this.task_workitems = task_workitems;
    }

    public String getAcorgid() {
        return acOrgId;
    }

    public void setAcorgid(String acOrgId) {
        this.acOrgId = acOrgId;
    }

    public List<task_WorkItem> getTask_workitems() {
        return task_workitems;
    }

    public void addTask_workitem(Task_workitem task_workitem) {
        this.task_workitems.add(task_workitem);
    }
    public List<task_WorkItem> getTask_workitems() {
        return task_workitems;
    }

    public void addTask_workitem(Task_workitem task_workitem) {
        this.task_workitems.add(task_workitem);
    }

}