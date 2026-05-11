





import java.util.List;
import java.util.ArrayList;

public class coursePages_CourseWorker  {

    private String courseRole;





    private coursePages_Course coursepages_course;




    private coursePages_Employee coursepages_employee;


    public coursePages_CourseWorker(
        String courseRole    ) {
        this.courseRole = courseRole;
    }


    public String getCourserole() {
        return courseRole;
    }

    public void setCourserole(String courseRole) {
        this.courseRole = courseRole;
    }

    public coursePages_Course getCoursepages_course() {
        return coursepages_course;
    }

    public void setCoursepages_course(coursePages_Course coursepages_course) {
        this.coursepages_course = coursepages_course;
    }
    public coursePages_Employee getCoursepages_employee() {
        return coursepages_employee;
    }

    public void setCoursepages_employee(coursePages_Employee coursepages_employee) {
        this.coursepages_employee = coursepages_employee;
    }

}