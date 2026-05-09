





import java.util.List;
import java.util.ArrayList;

public class eTJ_Flags extends StatusStatusSheetAttribute, StatusTimesheetAttribute, ResourceAttribute, Property, AccountAttribute, ReportAttribute {

    private String flags;



    public eTJ_Flags(
        String flags    ) {
        super(
        );
        this.flags = flags;
    }


    public String getFlags() {
        return flags;
    }

    public void setFlags(String flags) {
        this.flags = flags;
    }


}