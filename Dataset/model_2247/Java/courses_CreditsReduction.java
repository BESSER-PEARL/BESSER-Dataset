





import java.util.List;
import java.util.ArrayList;

public class courses_CreditsReduction  {

    private float reduction;





    private courses_CourseInstance courses_courseinstance;




    private courses_Course courses_course;


    public courses_CreditsReduction(
        float reduction    ) {
        this.reduction = reduction;
    }


    public float getReduction() {
        return reduction;
    }

    public void setReduction(float reduction) {
        this.reduction = reduction;
    }

    public courses_CourseInstance getCourses_courseinstance() {
        return courses_courseinstance;
    }

    public void setCourses_courseinstance(courses_CourseInstance courses_courseinstance) {
        this.courses_courseinstance = courses_courseinstance;
    }
    public courses_Course getCourses_course() {
        return courses_course;
    }

    public void setCourses_course(courses_Course courses_course) {
        this.courses_course = courses_course;
    }

}