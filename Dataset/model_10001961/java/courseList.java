





import java.util.List;
import java.util.ArrayList;

public class courseList  {

    private None currentCourse;
    private None Class;





    private Course course;




    private Teacher teacher;


    public courseList(
        None currentCourse,        None Class    ) {
        this.currentCourse = currentCourse;
        this.Class = Class;
    }


    public None getCurrentcourse() {
        return currentCourse;
    }

    public void setCurrentcourse(None currentCourse) {
        this.currentCourse = currentCourse;
    }
    public None getClass() {
        return Class;
    }

    public void setClass(None Class) {
        this.Class = Class;
    }

    public Course getCourse() {
        return course;
    }

    public void setCourse(Course course) {
        this.course = course;
    }
    public Teacher getTeacher() {
        return teacher;
    }

    public void setTeacher(Teacher teacher) {
        this.teacher = teacher;
    }

}