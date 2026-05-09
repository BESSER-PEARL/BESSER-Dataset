




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class model_task_WorkItem extends Annotation {

    private int estimate;
    private int effort;
    private int priority;
    private boolean resolved;
    private LocalDate dueDate;





    private organization_OrgUnit organization_orgunit;




    private task_WorkPackage task_workpackage;




    private organization_User organization_user;




    private List<organization_OrgUnit> organization_orgunits;


    public model_task_WorkItem(
        int estimate,        int effort,        int priority,        boolean resolved,        LocalDate dueDate    ) {
        super(
        );
        this.estimate = estimate;
        this.effort = effort;
        this.priority = priority;
        this.resolved = resolved;
        this.dueDate = dueDate;
        this.organization_orgunits = new ArrayList<>();
    }

    public model_task_WorkItem(
        int estimate,        int effort,        int priority,        boolean resolved,        LocalDate dueDate        ArrayList<organization_OrgUnit> organization_orgunits    ) {
        this.estimate = estimate;
        this.effort = effort;
        this.priority = priority;
        this.resolved = resolved;
        this.dueDate = dueDate;
        this.organization_orgunits = organization_orgunits;
    }

    public int getEstimate() {
        return estimate;
    }

    public void setEstimate(int estimate) {
        this.estimate = estimate;
    }
    public int getEffort() {
        return effort;
    }

    public void setEffort(int effort) {
        this.effort = effort;
    }
    public int getPriority() {
        return priority;
    }

    public void setPriority(int priority) {
        this.priority = priority;
    }
    public boolean getResolved() {
        return resolved;
    }

    public void setResolved(boolean resolved) {
        this.resolved = resolved;
    }
    public LocalDate getDuedate() {
        return dueDate;
    }

    public void setDuedate(LocalDate dueDate) {
        this.dueDate = dueDate;
    }

    public organization_OrgUnit getOrganization_orgunit() {
        return organization_orgunit;
    }

    public void setOrganization_orgunit(organization_OrgUnit organization_orgunit) {
        this.organization_orgunit = organization_orgunit;
    }
    public task_WorkPackage getTask_workpackage() {
        return task_workpackage;
    }

    public void setTask_workpackage(task_WorkPackage task_workpackage) {
        this.task_workpackage = task_workpackage;
    }
    public organization_User getOrganization_user() {
        return organization_user;
    }

    public void setOrganization_user(organization_User organization_user) {
        this.organization_user = organization_user;
    }
    public List<organization_OrgUnit> getOrganization_orgunits() {
        return organization_orgunits;
    }

    public void addOrganization_orgunit(Organization_orgunit organization_orgunit) {
        this.organization_orgunits.add(organization_orgunit);
    }

}