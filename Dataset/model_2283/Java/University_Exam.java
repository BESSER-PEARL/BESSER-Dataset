





import java.util.List;
import java.util.ArrayList;

public class University_Exam  {

    private String examID;





    private University_Course university_course;


    public University_Exam(
        String examID    ) {
        this.examID = examID;
    }


    public String getExamid() {
        return examID;
    }

    public void setExamid(String examID) {
        this.examID = examID;
    }

    public University_Course getUniversity_course() {
        return university_course;
    }

    public void setUniversity_course(University_Course university_course) {
        this.university_course = university_course;
    }

}