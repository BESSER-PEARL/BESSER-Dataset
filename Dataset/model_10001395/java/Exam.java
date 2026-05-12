





import java.util.List;
import java.util.ArrayList;

public class Exam  {

    private String EID;
    private String EName;
    private String MaxGrade;
    private String Exam_File_Name;
    private String ETIME;





    private Course course;


    public Exam(
        String EID,        String EName,        String MaxGrade,        String Exam_File_Name,        String ETIME    ) {
        this.EID = EID;
        this.EName = EName;
        this.MaxGrade = MaxGrade;
        this.Exam_File_Name = Exam_File_Name;
        this.ETIME = ETIME;
    }


    public String getEid() {
        return EID;
    }

    public void setEid(String EID) {
        this.EID = EID;
    }
    public String getEname() {
        return EName;
    }

    public void setEname(String EName) {
        this.EName = EName;
    }
    public String getMaxgrade() {
        return MaxGrade;
    }

    public void setMaxgrade(String MaxGrade) {
        this.MaxGrade = MaxGrade;
    }
    public String getExam_file_name() {
        return Exam_File_Name;
    }

    public void setExam_file_name(String Exam_File_Name) {
        this.Exam_File_Name = Exam_File_Name;
    }
    public String getEtime() {
        return ETIME;
    }

    public void setEtime(String ETIME) {
        this.ETIME = ETIME;
    }

    public Course getCourse() {
        return course;
    }

    public void setCourse(Course course) {
        this.course = course;
    }

}