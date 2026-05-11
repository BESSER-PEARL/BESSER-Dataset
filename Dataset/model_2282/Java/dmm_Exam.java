





import java.util.List;
import java.util.ArrayList;

public class dmm_Exam  {

    private String examID;





    private dmm_Course dmm_course;


    public dmm_Exam(
        String examID    ) {
        this.examID = examID;
    }


    public String getExamid() {
        return examID;
    }

    public void setExamid(String examID) {
        this.examID = examID;
    }

    public dmm_Course getDmm_course() {
        return dmm_course;
    }

    public void setDmm_course(dmm_Course dmm_course) {
        this.dmm_course = dmm_course;
    }

}