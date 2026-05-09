





import java.util.List;
import java.util.ArrayList;

public class model_organization_User extends OrgUnit {

    private String lastName;
    private String firstName;
    private String email;





    private List<task_WorkItem> task_workitems;


    public model_organization_User(
        String lastName,        String firstName,        String email    ) {
        super(
        );
        this.lastName = lastName;
        this.firstName = firstName;
        this.email = email;
        this.task_workitems = new ArrayList<>();
    }

    public model_organization_User(
        String lastName,        String firstName,        String email        ArrayList<task_WorkItem> task_workitems    ) {
        this.lastName = lastName;
        this.firstName = firstName;
        this.email = email;
        this.task_workitems = task_workitems;
    }

    public String getLastname() {
        return lastName;
    }

    public void setLastname(String lastName) {
        this.lastName = lastName;
    }
    public String getFirstname() {
        return firstName;
    }

    public void setFirstname(String firstName) {
        this.firstName = firstName;
    }
    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }

    public List<task_WorkItem> getTask_workitems() {
        return task_workitems;
    }

    public void addTask_workitem(Task_workitem task_workitem) {
        this.task_workitems.add(task_workitem);
    }

}