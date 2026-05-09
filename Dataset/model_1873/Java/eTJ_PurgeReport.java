





import java.util.List;
import java.util.ArrayList;

public class eTJ_PurgeReport extends ReportAttribute {

    private String listAttribute;



    public eTJ_PurgeReport(
        String listAttribute    ) {
        super(
        );
        this.listAttribute = listAttribute;
    }


    public String getListattribute() {
        return listAttribute;
    }

    public void setListattribute(String listAttribute) {
        this.listAttribute = listAttribute;
    }


}