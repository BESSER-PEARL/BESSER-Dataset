





import java.util.List;
import java.util.ArrayList;

public class connection_SAPBWTableField extends SAPTableField {

    private String logicalName;



    public connection_SAPBWTableField(
        String logicalName    ) {
        super(
        );
        this.logicalName = logicalName;
    }


    public String getLogicalname() {
        return logicalName;
    }

    public void setLogicalname(String logicalName) {
        this.logicalName = logicalName;
    }


}