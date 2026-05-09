





import java.util.List;
import java.util.ArrayList;

public class eTJ_HideResource extends IcalReportAttribute, ExportAttribute, StatusSheetReportAttribute, NikuReportAttribute, TimesheetReportAttribute, ReportAttribute {






    private eTJ_TagFile etj_tagfile;


    public eTJ_HideResource(
    ) {
        super(
        );
    }



    public eTJ_TagFile getEtj_tagfile() {
        return etj_tagfile;
    }

    public void setEtj_tagfile(eTJ_TagFile etj_tagfile) {
        this.etj_tagfile = etj_tagfile;
    }

}