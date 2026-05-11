





import java.util.List;
import java.util.ArrayList;

public class org_sgiusa_model_LeadershipRole  {

    private String lastUpdate;
    private String level;
    private String active;
    private String endDate;
    private String subDivision;
    private String activityGroup;
    private String position;
    private String id;
    private String division;
    private String startDate;



    public org_sgiusa_model_LeadershipRole(
        String lastUpdate,        String level,        String active,        String endDate,        String subDivision,        String activityGroup,        String position,        String id,        String division,        String startDate    ) {
        this.lastUpdate = lastUpdate;
        this.level = level;
        this.active = active;
        this.endDate = endDate;
        this.subDivision = subDivision;
        this.activityGroup = activityGroup;
        this.position = position;
        this.id = id;
        this.division = division;
        this.startDate = startDate;
    }


    public String getLastupdate() {
        return lastUpdate;
    }

    public void setLastupdate(String lastUpdate) {
        this.lastUpdate = lastUpdate;
    }
    public String getLevel() {
        return level;
    }

    public void setLevel(String level) {
        this.level = level;
    }
    public String getActive() {
        return active;
    }

    public void setActive(String active) {
        this.active = active;
    }
    public String getEnddate() {
        return endDate;
    }

    public void setEnddate(String endDate) {
        this.endDate = endDate;
    }
    public String getSubdivision() {
        return subDivision;
    }

    public void setSubdivision(String subDivision) {
        this.subDivision = subDivision;
    }
    public String getActivitygroup() {
        return activityGroup;
    }

    public void setActivitygroup(String activityGroup) {
        this.activityGroup = activityGroup;
    }
    public String getPosition() {
        return position;
    }

    public void setPosition(String position) {
        this.position = position;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getDivision() {
        return division;
    }

    public void setDivision(String division) {
        this.division = division;
    }
    public String getStartdate() {
        return startDate;
    }

    public void setStartdate(String startDate) {
        this.startDate = startDate;
    }


}