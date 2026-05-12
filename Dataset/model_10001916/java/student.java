





import java.util.List;
import java.util.ArrayList;

public class student  {

    private None student_id;
    private None no_of_courses;
    private String student_name;



    public student(
        None student_id,        None no_of_courses,        String student_name    ) {
        this.student_id = student_id;
        this.no_of_courses = no_of_courses;
        this.student_name = student_name;
    }


    public None getStudent_id() {
        return student_id;
    }

    public void setStudent_id(None student_id) {
        this.student_id = student_id;
    }
    public None getNo_of_courses() {
        return no_of_courses;
    }

    public void setNo_of_courses(None no_of_courses) {
        this.no_of_courses = no_of_courses;
    }
    public String getStudent_name() {
        return student_name;
    }

    public void setStudent_name(String student_name) {
        this.student_name = student_name;
    }


}