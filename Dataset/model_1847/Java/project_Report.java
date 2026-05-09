





import java.util.List;
import java.util.ArrayList;

public class project_Report extends AccountReport, TaskReport, TextReport, ResourceReport {

    private String id;
    private String name;





    private project_SupplementReport project_supplementreport;




    private project_ReportPrefix project_reportprefix;


    public project_Report(
        String id,        String name    ) {
        super(
        );
        this.id = id;
        this.name = name;
    }


    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public project_SupplementReport getProject_supplementreport() {
        return project_supplementreport;
    }

    public void setProject_supplementreport(project_SupplementReport project_supplementreport) {
        this.project_supplementreport = project_supplementreport;
    }
    public project_ReportPrefix getProject_reportprefix() {
        return project_reportprefix;
    }

    public void setProject_reportprefix(project_ReportPrefix project_reportprefix) {
        this.project_reportprefix = project_reportprefix;
    }

}