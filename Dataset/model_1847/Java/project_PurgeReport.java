





import java.util.List;
import java.util.ArrayList;

public class project_PurgeReport extends ReportAttribute {

    private String listAttribute;



    public project_PurgeReport(
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