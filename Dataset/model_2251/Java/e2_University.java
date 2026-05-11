





import java.util.List;
import java.util.ArrayList;

public class e2_University  {

    private String Name;





    private List<e2_Course> e2_courses;




    private List<e2_Person> e2_persons;


    public e2_University(
        String Name    ) {
        this.Name = Name;
        this.e2_courses = new ArrayList<>();
        this.e2_persons = new ArrayList<>();
    }

    public e2_University(
        String Name        ArrayList<e2_Course> e2_courses,        ArrayList<e2_Person> e2_persons    ) {
        this.Name = Name;
        this.e2_courses = e2_courses;
        this.e2_persons = e2_persons;
    }

    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }

    public List<e2_Course> getE2_courses() {
        return e2_courses;
    }

    public void addE2_course(E2_course e2_course) {
        this.e2_courses.add(e2_course);
    }
    public List<e2_Person> getE2_persons() {
        return e2_persons;
    }

    public void addE2_person(E2_person e2_person) {
        this.e2_persons.add(e2_person);
    }

}