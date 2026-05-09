





import java.util.List;
import java.util.ArrayList;

public class university_Department extends NamedElement {






    private List<university_Student> university_students;




    private university_University university_university;


    public university_Department(
    ) {
        super(
        );
        this.university_students = new ArrayList<>();
    }

    public university_Department(
        ArrayList<university_Student> university_students    ) {
        this.university_students = university_students;
    }


    public List<university_Student> getUniversity_students() {
        return university_students;
    }

    public void addUniversity_student(University_student university_student) {
        this.university_students.add(university_student);
    }
    public university_University getUniversity_university() {
        return university_university;
    }

    public void setUniversity_university(university_University university_university) {
        this.university_university = university_university;
    }

}