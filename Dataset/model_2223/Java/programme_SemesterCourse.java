





import java.util.List;
import java.util.ArrayList;

public class programme_SemesterCourse  {

    private String courseType;





    private programme_Course programme_course;




    private programme_Semester programme_semester;


    public programme_SemesterCourse(
        String courseType    ) {
        this.courseType = courseType;
    }


    public String getCoursetype() {
        return courseType;
    }

    public void setCoursetype(String courseType) {
        this.courseType = courseType;
    }

    public programme_Course getProgramme_course() {
        return programme_course;
    }

    public void setProgramme_course(programme_Course programme_course) {
        this.programme_course = programme_course;
    }
    public programme_Semester getProgramme_semester() {
        return programme_semester;
    }

    public void setProgramme_semester(programme_Semester programme_semester) {
        this.programme_semester = programme_semester;
    }

}