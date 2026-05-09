





import java.util.List;
import java.util.ArrayList;

public class eTJ_Report extends TaskReport, TextReport, ResourceReport, AccountReport {

    private String name;
    private String id;





    private eTJ_SupplementReport etj_supplementreport;




    private eTJ_ReportPrefix etj_reportprefix;


    public eTJ_Report(
        String name,        String id    ) {
        super(
        );
        this.name = name;
        this.id = id;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public eTJ_SupplementReport getEtj_supplementreport() {
        return etj_supplementreport;
    }

    public void setEtj_supplementreport(eTJ_SupplementReport etj_supplementreport) {
        this.etj_supplementreport = etj_supplementreport;
    }
    public eTJ_ReportPrefix getEtj_reportprefix() {
        return etj_reportprefix;
    }

    public void setEtj_reportprefix(eTJ_ReportPrefix etj_reportprefix) {
        this.etj_reportprefix = etj_reportprefix;
    }

}