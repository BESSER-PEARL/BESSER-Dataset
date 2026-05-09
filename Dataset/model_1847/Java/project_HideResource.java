





import java.util.List;
import java.util.ArrayList;

public class project_HideResource extends ExportAttribute, NikuReportAttribute, StatusSheetReportAttribute, ReportAttribute, TimesheetReportAttribute, IcalReportAttribute {






    private project_TagFile project_tagfile;




    private project_LogicalExpression project_logicalexpression;


    public project_HideResource(
    ) {
        super(
        );
    }



    public project_TagFile getProject_tagfile() {
        return project_tagfile;
    }

    public void setProject_tagfile(project_TagFile project_tagfile) {
        this.project_tagfile = project_tagfile;
    }
    public project_LogicalExpression getProject_logicalexpression() {
        return project_logicalexpression;
    }

    public void setProject_logicalexpression(project_LogicalExpression project_logicalexpression) {
        this.project_logicalexpression = project_logicalexpression;
    }

}