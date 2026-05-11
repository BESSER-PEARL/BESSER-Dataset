





import java.util.List;
import java.util.ArrayList;

public class education_Course  {

    private String name;





    private education_Teacher education_teacher;




    private List<education_Student> education_students;


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

    public education_Teacher getEducation_teacher() {
        return education_teacher;
    }

    public void setEducation_teacher(education_Teacher education_teacher) {
        this.education_teacher = education_teacher;
    }
    public List<education_Student> getEducation_students() {
        return education_students;
    }

    public void addEducation_student(Education_student education_student) {
        this.education_students.add(education_student);
    }

}