





import java.util.List;
import java.util.ArrayList;

public class mypackage_Course  {

    private String CourseFileName;
    private String CName;
    private String CId;
    private int CreditHours;



    public mypackage_Course(
        String CourseFileName,        String CName,        String CId,        int CreditHours    ) {
        this.CourseFileName = CourseFileName;
        this.CName = CName;
        this.CId = CId;
        this.CreditHours = CreditHours;
    }


    public String getCoursefilename() {
        return CourseFileName;
    }

    public void setCoursefilename(String CourseFileName) {
        this.CourseFileName = CourseFileName;
    }
    public String getCname() {
        return CName;
    }

    public void setCname(String CName) {
        this.CName = CName;
    }
    public String getCid() {
        return CId;
    }

    public void setCid(String CId) {
        this.CId = CId;
    }
    public int getCredithours() {
        return CreditHours;
    }

    public void setCredithours(int CreditHours) {
        this.CreditHours = CreditHours;
    }


}