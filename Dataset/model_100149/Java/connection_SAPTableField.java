





import java.util.List;
import java.util.ArrayList;

public class connection_SAPTableField extends MetadataColumn {

    private String businessName;
    private String refTable;



    public connection_SAPTableField(
        String businessName,        String refTable    ) {
        super(
        );
        this.businessName = businessName;
        this.refTable = refTable;
    }


    public String getBusinessname() {
        return businessName;
    }

    public void setBusinessname(String businessName) {
        this.businessName = businessName;
    }
    public String getReftable() {
        return refTable;
    }

    public void setReftable(String refTable) {
        this.refTable = refTable;
    }


}