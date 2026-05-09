





import java.util.List;
import java.util.ArrayList;

public class project_Timezone extends ExportAttribute, ProjectAttribute, ReportAttribute {

    private String timezone;



    public project_Timezone(
        String timezone    ) {
        super(
        );
        this.timezone = timezone;
    }


    public String getTimezone() {
        return timezone;
    }

    public void setTimezone(String timezone) {
        this.timezone = timezone;
    }


}