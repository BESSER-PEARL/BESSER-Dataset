





import java.util.List;
import java.util.ArrayList;

public class mypackage_Course  {

    private String CId;
    private int CreditHours;
    private String CName;
    private String CourseFileName;



    public mypackage_Course(
        String CId,        int CreditHours,        String CName,        String CourseFileName    ) {
        this.CId = CId;
        this.CreditHours = CreditHours;
        this.CName = CName;
        this.CourseFileName = CourseFileName;
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
    public String getCname() {
        return CName;
    }

    public void setCname(String CName) {
        this.CName = CName;
    }
    public String getCoursefilename() {
        return CourseFileName;
    }

    public void setCoursefilename(String CourseFileName) {
        this.CourseFileName = CourseFileName;
    }


}