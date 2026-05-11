





import java.util.List;
import java.util.ArrayList;

public class course_desc_Student extends PersonRole {

    private float totalStudyPoints;



    public course_desc_Student(
        float totalStudyPoints    ) {
        super(
        );
        this.totalStudyPoints = totalStudyPoints;
    }


    public float getTotalstudypoints() {
        return totalStudyPoints;
    }

    public void setTotalstudypoints(float totalStudyPoints) {
        this.totalStudyPoints = totalStudyPoints;
    }


}