





import java.util.List;
import java.util.ArrayList;

public class university_Staff  {

    private String staff;





    private List<university_Professor> university_professors;




    private List<university_Assistant> university_assistants;


    public university_Staff(
        String staff    ) {
        this.staff = staff;
        this.university_professors = new ArrayList<>();
        this.university_assistants = new ArrayList<>();
    }

    public university_Staff(
        String staff        ArrayList<university_Professor> university_professors,        ArrayList<university_Assistant> university_assistants    ) {
        this.staff = staff;
        this.university_professors = university_professors;
        this.university_assistants = university_assistants;
    }

    public String getStaff() {
        return staff;
    }

    public void setStaff(String staff) {
        this.staff = staff;
    }

    public List<university_Professor> getUniversity_professors() {
        return university_professors;
    }

    public void addUniversity_professor(University_professor university_professor) {
        this.university_professors.add(university_professor);
    }
    public List<university_Assistant> getUniversity_assistants() {
        return university_assistants;
    }

    public void addUniversity_assistant(University_assistant university_assistant) {
        this.university_assistants.add(university_assistant);
    }

}