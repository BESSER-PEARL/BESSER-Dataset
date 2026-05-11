





import java.util.List;
import java.util.ArrayList;

public class edu_Take_Course  {






    private List<edu_Student> edu_students;




    private List<edu_Course> edu_courses;


    public edu_Take_Course(
    ) {
        this.edu_students = new ArrayList<>();
        this.edu_courses = new ArrayList<>();
    }

    public edu_Take_Course(
        ArrayList<edu_Student> edu_students,        ArrayList<edu_Course> edu_courses    ) {
        this.edu_students = edu_students;
        this.edu_courses = edu_courses;
    }


    public List<edu_Student> getEdu_students() {
        return edu_students;
    }

    public void addEdu_student(Edu_student edu_student) {
        this.edu_students.add(edu_student);
    }
    public List<edu_Course> getEdu_courses() {
        return edu_courses;
    }

    public void addEdu_course(Edu_course edu_course) {
        this.edu_courses.add(edu_course);
    }

}