





import java.util.List;
import java.util.ArrayList;

public class Schedule  {

    private None Teacher;
    private None Course;





    private Teachers teachers;


    public Schedule(
        None Teacher,        None Course    ) {
        this.Teacher = Teacher;
        this.Course = Course;
    }


    public None getTeacher() {
        return Teacher;
    }

    public void setTeacher(None Teacher) {
        this.Teacher = Teacher;
    }
    public None getCourse() {
        return Course;
    }

    public void setCourse(None Course) {
        this.Course = Course;
    }

    public Teachers getTeachers() {
        return teachers;
    }

    public void setTeachers(Teachers teachers) {
        this.teachers = teachers;
    }

}