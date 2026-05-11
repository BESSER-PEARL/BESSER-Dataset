





import java.util.List;
import java.util.ArrayList;

public class org_sgiusa_model_SchoolInfo  {

    private String lastUpdate;
    private String id;
    private String schoolName;
    private String schoolType;
    private String fieldOfStudy;
    private String endDate;
    private String startDate;



    public org_sgiusa_model_SchoolInfo(
        String lastUpdate,        String id,        String schoolName,        String schoolType,        String fieldOfStudy,        String endDate,        String startDate    ) {
        this.lastUpdate = lastUpdate;
        this.id = id;
        this.schoolName = schoolName;
        this.schoolType = schoolType;
        this.fieldOfStudy = fieldOfStudy;
        this.endDate = endDate;
        this.startDate = startDate;
    }


    public String getLastupdate() {
        return lastUpdate;
    }

    public void setLastupdate(String lastUpdate) {
        this.lastUpdate = lastUpdate;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getSchoolname() {
        return schoolName;
    }

    public void setSchoolname(String schoolName) {
        this.schoolName = schoolName;
    }
    public String getSchooltype() {
        return schoolType;
    }

    public void setSchooltype(String schoolType) {
        this.schoolType = schoolType;
    }
    public String getFieldofstudy() {
        return fieldOfStudy;
    }

    public void setFieldofstudy(String fieldOfStudy) {
        this.fieldOfStudy = fieldOfStudy;
    }
    public String getEnddate() {
        return endDate;
    }

    public void setEnddate(String endDate) {
        this.endDate = endDate;
    }
    public String getStartdate() {
        return startDate;
    }

    public void setStartdate(String startDate) {
        this.startDate = startDate;
    }


}