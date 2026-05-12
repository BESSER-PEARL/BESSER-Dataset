





import java.util.List;
import java.util.ArrayList;

public class mypackage_Exam  {

    private String EName;
    private String EId;
    private String ExamsFileName;
    private String MaxGrade;





    private mypackage_Course mypackage_course;


    public mypackage_Exam(
        String EName,        String EId,        String ExamsFileName,        String MaxGrade    ) {
        this.EName = EName;
        this.EId = EId;
        this.ExamsFileName = ExamsFileName;
        this.MaxGrade = MaxGrade;
    }


    public String getEname() {
        return EName;
    }

    public void setEname(String EName) {
        this.EName = EName;
    }
    public String getEid() {
        return EId;
    }

    public void setEid(String EId) {
        this.EId = EId;
    }
    public String getExamsfilename() {
        return ExamsFileName;
    }

    public void setExamsfilename(String ExamsFileName) {
        this.ExamsFileName = ExamsFileName;
    }
    public String getMaxgrade() {
        return MaxGrade;
    }

    public void setMaxgrade(String MaxGrade) {
        this.MaxGrade = MaxGrade;
    }

    public mypackage_Course getMypackage_course() {
        return mypackage_course;
    }

    public void setMypackage_course(mypackage_Course mypackage_course) {
        this.mypackage_course = mypackage_course;
    }

}