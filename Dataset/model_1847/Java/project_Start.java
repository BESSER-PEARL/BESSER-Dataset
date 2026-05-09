





import java.util.List;
import java.util.ArrayList;

public class project_Start extends ExportAttribute, NikuReportAttribute, StatusSheetReportAttribute, TaskAttribute, ColumnAttribute, ReportAttribute, TimesheetReportAttribute, IcalReportAttribute {

    private String start;



    public project_Start(
        String start    ) {
        super(
        );
        this.start = start;
    }


    public String getStart() {
        return start;
    }

    public void setStart(String start) {
        this.start = start;
    }


}