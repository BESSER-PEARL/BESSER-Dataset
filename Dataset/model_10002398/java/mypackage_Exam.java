





import java.util.List;
import java.util.ArrayList;

public class mypackage_Exam  {

    private String EId;
    private String EName;
    private String MaxGrade;
    private String ExamsFileName;





    private mypackage_Course mypackage_course;


    public mypackage_Exam(
        String EId,        String EName,        String MaxGrade,        String ExamsFileName    ) {
        this.EId = EId;
        this.EName = EName;
        this.MaxGrade = MaxGrade;
        this.ExamsFileName = ExamsFileName;
    }


    public String getEid() {
        return EId;
    }

    public void setEid(String EId) {
        this.EId = EId;
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
    public String getExamsfilename() {
        return ExamsFileName;
    }

    public void setExamsfilename(String ExamsFileName) {
        this.ExamsFileName = ExamsFileName;
    }

    public mypackage_Course getMypackage_course() {
        return mypackage_course;
    }

    public void setMypackage_course(mypackage_Course mypackage_course) {
        this.mypackage_course = mypackage_course;
    }

}