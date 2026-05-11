





import java.util.List;
import java.util.ArrayList;

public class education_Course  {

    private String name;





    private List<education_Student> education_students;




    private education_Student education_student;


    public education_Course(
        String name    ) {
        this.name = name;
        this.education_students = new ArrayList<>();
    }

    public education_Course(
        String name        ArrayList<education_Student> education_students    ) {
        this.name = name;
        this.education_students = education_students;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<education_Student> getEducation_students() {
        return education_students;
    }

    public void addEducation_student(Education_student education_student) {
        this.education_students.add(education_student);
    }
    public education_Student getEducation_student() {
        return education_student;
    }

    public void setEducation_student(education_Student education_student) {
        this.education_student = education_student;
    }

}