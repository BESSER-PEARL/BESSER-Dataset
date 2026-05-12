





import java.util.List;
import java.util.ArrayList;

public class course  {

    private String placed_on;
    private String teached_by;
    private String course_name;
    private None course_id;





    private student student;


    public course(
        String placed_on,        String teached_by,        String course_name,        None course_id    ) {
        this.placed_on = placed_on;
        this.teached_by = teached_by;
        this.course_name = course_name;
        this.course_id = course_id;
    }


    public String getPlaced_on() {
        return placed_on;
    }

    public void setPlaced_on(String placed_on) {
        this.placed_on = placed_on;
    }
    public String getTeached_by() {
        return teached_by;
    }

    public void setTeached_by(String teached_by) {
        this.teached_by = teached_by;
    }
    public String getCourse_name() {
        return course_name;
    }

    public void setCourse_name(String course_name) {
        this.course_name = course_name;
    }
    public None getCourse_id() {
        return course_id;
    }

    public void setCourse_id(None course_id) {
        this.course_id = course_id;
    }

    public student getStudent() {
        return student;
    }

    public void setStudent(student student) {
        this.student = student;
    }

}