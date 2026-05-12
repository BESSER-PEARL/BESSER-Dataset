





import java.util.List;
import java.util.ArrayList;

public class SubjectShedule  {

    private String date;
    private int auditoriumNumber;
    private int subjectCode;
    private int id;
    private int groupNumber;
    private int activityTypeCode;
    private int individualIdentificationCode;



    public SubjectShedule(
        String date,        int auditoriumNumber,        int subjectCode,        int id,        int groupNumber,        int activityTypeCode,        int individualIdentificationCode    ) {
        this.date = date;
        this.auditoriumNumber = auditoriumNumber;
        this.subjectCode = subjectCode;
        this.id = id;
        this.groupNumber = groupNumber;
        this.activityTypeCode = activityTypeCode;
        this.individualIdentificationCode = individualIdentificationCode;
    }


    public String getDate() {
        return date;
    }

    public void setDate(String date) {
        this.date = date;
    }
    public int getAuditoriumnumber() {
        return auditoriumNumber;
    }

    public void setAuditoriumnumber(int auditoriumNumber) {
        this.auditoriumNumber = auditoriumNumber;
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
    public int getGroupnumber() {
        return groupNumber;
    }

    public void setGroupnumber(int groupNumber) {
        this.groupNumber = groupNumber;
    }
    public int getActivitytypecode() {
        return activityTypeCode;
    }

    public void setActivitytypecode(int activityTypeCode) {
        this.activityTypeCode = activityTypeCode;
    }
    public int getIndividualidentificationcode() {
        return individualIdentificationCode;
    }

    public void setIndividualidentificationcode(int individualIdentificationCode) {
        this.individualIdentificationCode = individualIdentificationCode;
    }


}