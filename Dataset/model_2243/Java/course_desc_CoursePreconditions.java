





import java.util.List;
import java.util.ArrayList;

public class course_desc_CoursePreconditions  {

    private float reductionPoints;
    private boolean isRecommended;
    private boolean isRequired;





    private course_desc_Course course_desc_course;




    private course_desc_Univ course_desc_univ;




    private course_desc_Course course_desc_course;


    public course_desc_CoursePreconditions(
        float reductionPoints,        boolean isRecommended,        boolean isRequired    ) {
        this.reductionPoints = reductionPoints;
        this.isRecommended = isRecommended;
        this.isRequired = isRequired;
    }


    public float getReductionpoints() {
        return reductionPoints;
    }

    public void setReductionpoints(float reductionPoints) {
        this.reductionPoints = reductionPoints;
    }
    public boolean getIsrecommended() {
        return isRecommended;
    }

    public void setIsrecommended(boolean isRecommended) {
        this.isRecommended = isRecommended;
    }
    public boolean getIsrequired() {
        return isRequired;
    }

    public void setIsrequired(boolean isRequired) {
        this.isRequired = isRequired;
    }

    public course_desc_Course getCourse_desc_course() {
        return course_desc_course;
    }

    public void setCourse_desc_course(course_desc_Course course_desc_course) {
        this.course_desc_course = course_desc_course;
    }
    public course_desc_Univ getCourse_desc_univ() {
        return course_desc_univ;
    }

    public void setCourse_desc_univ(course_desc_Univ course_desc_univ) {
        this.course_desc_univ = course_desc_univ;
    }
    public course_desc_Course getCourse_desc_course() {
        return course_desc_course;
    }

    public void setCourse_desc_course(course_desc_Course course_desc_course) {
        this.course_desc_course = course_desc_course;
    }

}