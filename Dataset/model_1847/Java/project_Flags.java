





import java.util.List;
import java.util.ArrayList;

public class project_Flags extends TaskAttribute, AccountAttribute, StatusStatusSheetAttribute, StatusTimesheetAttribute, Property, ReportAttribute, ResourceAttribute {

    private String flags;



    public project_Flags(
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