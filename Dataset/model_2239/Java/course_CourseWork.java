





import java.util.List;
import java.util.ArrayList;

public class course_CourseWork  {

    private int labHours;
    private int lectureHours;



    public course_CourseWork(
        int labHours,        int lectureHours    ) {
        this.labHours = labHours;
        this.lectureHours = lectureHours;
    }


    public int getLabhours() {
        return labHours;
    }

    public void setLabhours(int labHours) {
        this.labHours = labHours;
    }
    public int getLecturehours() {
        return lectureHours;
    }

    public void setLecturehours(int lectureHours) {
        this.lectureHours = lectureHours;
    }


}