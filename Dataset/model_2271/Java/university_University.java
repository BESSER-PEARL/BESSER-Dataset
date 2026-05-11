





import java.util.List;
import java.util.ArrayList;

public class university_University  {

    private String name;





    private List<university_Student> university_students;




    private List<university_Course> university_courses;


    public university_University(
        String name    ) {
        this.name = name;
        this.university_students = new ArrayList<>();
        this.university_courses = new ArrayList<>();
    }

    public university_University(
        String name        ArrayList<university_Student> university_students,        ArrayList<university_Course> university_courses    ) {
        this.name = name;
        this.university_students = university_students;
        this.university_courses = university_courses;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<university_Student> getUniversity_students() {
        return university_students;
    }

    public void addUniversity_student(University_student university_student) {
        this.university_students.add(university_student);
    }
    public List<university_Course> getUniversity_courses() {
        return university_courses;
    }

    public void addUniversity_course(University_course university_course) {
        this.university_courses.add(university_course);
    }

}