





import java.util.List;
import java.util.ArrayList;

public class TimeCreditForEducationalSemester  {

    private int totalHours;
    private int subjectCode;
    private int groupNumber;
    private int id;
    private int activityTypeCode;



    public TimeCreditForEducationalSemester(
        int totalHours,        int subjectCode,        int groupNumber,        int id,        int activityTypeCode    ) {
        this.totalHours = totalHours;
        this.subjectCode = subjectCode;
        this.groupNumber = groupNumber;
        this.id = id;
        this.activityTypeCode = activityTypeCode;
    }


    public int getTotalhours() {
        return totalHours;
    }

    public void setTotalhours(int totalHours) {
        this.totalHours = totalHours;
    }
    public int getSubjectcode() {
        return subjectCode;
    }

    public void setSubjectcode(int subjectCode) {
        this.subjectCode = subjectCode;
    }
    public int getGroupnumber() {
        return groupNumber;
    }

    public void setGroupnumber(int groupNumber) {
        this.groupNumber = groupNumber;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    public int getActivitytypecode() {
        return activityTypeCode;
    }

    public void setActivitytypecode(int activityTypeCode) {
        this.activityTypeCode = activityTypeCode;
    }


}