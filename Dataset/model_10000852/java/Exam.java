





import java.util.List;
import java.util.ArrayList;

public class Exam  {

    private String Exam_File_Name;
    private String MaxGrade;
    private String ETIME;
    private String EName;
    private String EID;



    public Exam(
        String Exam_File_Name,        String MaxGrade,        String ETIME,        String EName,        String EID    ) {
        this.Exam_File_Name = Exam_File_Name;
        this.MaxGrade = MaxGrade;
        this.ETIME = ETIME;
        this.EName = EName;
        this.EID = EID;
    }


    public String getExam_file_name() {
        return Exam_File_Name;
    }

    public void setExam_file_name(String Exam_File_Name) {
        this.Exam_File_Name = Exam_File_Name;
    }
    public String getMaxgrade() {
        return MaxGrade;
    }

    public void setMaxgrade(String MaxGrade) {
        this.MaxGrade = MaxGrade;
    }
    public String getEtime() {
        return ETIME;
    }

    public void setEtime(String ETIME) {
        this.ETIME = ETIME;
    }
    public String getEname() {
        return EName;
    }

    public void setEname(String EName) {
        this.EName = EName;
    }
    public String getEid() {
        return EID;
    }

    public void setEid(String EID) {
        this.EID = EID;
    }


}