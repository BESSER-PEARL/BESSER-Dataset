





import java.util.List;
import java.util.ArrayList;

public class dXP_AcademicSession extends Base {

    private String schoolYear;
    private String title;
    private String endDate;
    private String type;
    private String startDate;





    private dXP_OneRoster dxp_oneroster;


    public dXP_AcademicSession(
        String schoolYear,        String title,        String endDate,        String type,        String startDate    ) {
        super(
        );
        this.schoolYear = schoolYear;
        this.title = title;
        this.endDate = endDate;
        this.type = type;
        this.startDate = startDate;
    }


    public String getSchoolyear() {
        return schoolYear;
    }

    public void setSchoolyear(String schoolYear) {
        this.schoolYear = schoolYear;
    }
    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }
    public String getEnddate() {
        return endDate;
    }

    public void setEnddate(String endDate) {
        this.endDate = endDate;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getStartdate() {
        return startDate;
    }

    public void setStartdate(String startDate) {
        this.startDate = startDate;
    }

    public dXP_OneRoster getDxp_oneroster() {
        return dxp_oneroster;
    }

    public void setDxp_oneroster(dXP_OneRoster dxp_oneroster) {
        this.dxp_oneroster = dxp_oneroster;
    }

}