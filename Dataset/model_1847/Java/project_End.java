





import java.util.List;
import java.util.ArrayList;

public class project_End extends ExportAttribute, NikuReportAttribute, TaskTimesheetAttribute, StatusSheetReportAttribute, TaskAttribute, NewTaskAttribute, ColumnAttribute, ReportAttribute, TimesheetReportAttribute, IcalReportAttribute {

    private String end;



    public project_End(
        String end    ) {
        super(
        );
        this.end = end;
    }


    public String getEnd() {
        return end;
    }

    public void setEnd(String end) {
        this.end = end;
    }


}