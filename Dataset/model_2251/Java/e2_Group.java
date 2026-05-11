





import java.util.List;
import java.util.ArrayList;

public class e2_Group  {

    private String Name;





    private List<e2_AssignmentSubmission> e2_assignmentsubmissions;




    private List<e2_Person> e2_persons;


    public e2_Group(
        String Name    ) {
        this.Name = Name;
        this.e2_assignmentsubmissions = new ArrayList<>();
        this.e2_persons = new ArrayList<>();
    }

    public e2_Group(
        String Name        ArrayList<e2_AssignmentSubmission> e2_assignmentsubmissions,        ArrayList<e2_Person> e2_persons    ) {
        this.Name = Name;
        this.e2_assignmentsubmissions = e2_assignmentsubmissions;
        this.e2_persons = e2_persons;
    }

    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }

    public List<e2_AssignmentSubmission> getE2_assignmentsubmissions() {
        return e2_assignmentsubmissions;
    }

    public void addE2_assignmentsubmission(E2_assignmentsubmission e2_assignmentsubmission) {
        this.e2_assignmentsubmissions.add(e2_assignmentsubmission);
    }
    public List<e2_Person> getE2_persons() {
        return e2_persons;
    }

    public void addE2_person(E2_person e2_person) {
        this.e2_persons.add(e2_person);
    }

}