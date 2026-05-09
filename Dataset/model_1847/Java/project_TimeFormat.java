





import java.util.List;
import java.util.ArrayList;

public class project_TimeFormat extends ProjectAttribute, ReportAttribute {

    private String timeformat;



    public project_TimeFormat(
        String timeformat    ) {
        super(
        );
        this.timeformat = timeformat;
    }


    public String getTimeformat() {
        return timeformat;
    }

    public void setTimeformat(String timeformat) {
        this.timeformat = timeformat;
    }


}