





import java.util.List;
import java.util.ArrayList;

public class ActivityType  {

    private int subjectCode;
    private int id;
    private String activityTypeName;
    private int activityTypeCode;





    private Subject subject;


    public ActivityType(
        int subjectCode,        int id,        String activityTypeName,        int activityTypeCode    ) {
        this.subjectCode = subjectCode;
        this.id = id;
        this.activityTypeName = activityTypeName;
        this.activityTypeCode = activityTypeCode;
    }


    public int getSubjectcode() {
        return subjectCode;
    }

    public void setSubjectcode(int subjectCode) {
        this.subjectCode = subjectCode;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    public String getActivitytypename() {
        return activityTypeName;
    }

    public void setActivitytypename(String activityTypeName) {
        this.activityTypeName = activityTypeName;
    }
    public int getActivitytypecode() {
        return activityTypeCode;
    }

    public void setActivitytypecode(int activityTypeCode) {
        this.activityTypeCode = activityTypeCode;
    }

    public Subject getSubject() {
        return subject;
    }

    public void setSubject(Subject subject) {
        this.subject = subject;
    }

}