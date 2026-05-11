





import java.util.List;
import java.util.ArrayList;

public class course_StudyProgram  {

    private String code;





    private course_Course course_course;




    private course_Department course_department;


    public course_StudyProgram(
        String code    ) {
        this.code = code;
    }


    public String getCode() {
        return code;
    }

    public void setCode(String code) {
        this.code = code;
    }

    public course_Course getCourse_course() {
        return course_course;
    }

    public void setCourse_course(course_Course course_course) {
        this.course_course = course_course;
    }
    public course_Department getCourse_department() {
        return course_department;
    }

    public void setCourse_department(course_Department course_department) {
        this.course_department = course_department;
    }

}