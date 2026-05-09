





import java.util.List;
import java.util.ArrayList;

public class project_RollupTask extends ExportAttribute, IcalReportAttribute, ReportAttribute {






    private project_LogicalExpression project_logicalexpression;




    private project_TagFile project_tagfile;


    public project_RollupTask(
    ) {
        super(
        );
    }



    public project_LogicalExpression getProject_logicalexpression() {
        return project_logicalexpression;
    }

    public void setProject_logicalexpression(project_LogicalExpression project_logicalexpression) {
        this.project_logicalexpression = project_logicalexpression;
    }
    public project_TagFile getProject_tagfile() {
        return project_tagfile;
    }

    public void setProject_tagfile(project_TagFile project_tagfile) {
        this.project_tagfile = project_tagfile;
    }

}