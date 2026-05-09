





import java.util.List;
import java.util.ArrayList;

public class model_organization_User extends OrgUnit {

    private String email;
    private String firstName;
    private String lastName;





    private List<task_WorkItem> task_workitems;


    public model_organization_User(
        String email,        String firstName,        String lastName    ) {
        super(
        );
        this.email = email;
        this.firstName = firstName;
        this.lastName = lastName;
        this.task_workitems = new ArrayList<>();
    }

    public model_organization_User(
        String email,        String firstName,        String lastName        ArrayList<task_WorkItem> task_workitems    ) {
        this.email = email;
        this.firstName = firstName;
        this.lastName = lastName;
        this.task_workitems = task_workitems;
    }

    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }
    public String getFirstname() {
        return firstName;
    }

    public void setFirstname(String firstName) {
        this.firstName = firstName;
    }
    public String getLastname() {
        return lastName;
    }

    public void setLastname(String lastName) {
        this.lastName = lastName;
    }

    public List<task_WorkItem> getTask_workitems() {
        return task_workitems;
    }

    public void addTask_workitem(Task_workitem task_workitem) {
        this.task_workitems.add(task_workitem);
    }

}