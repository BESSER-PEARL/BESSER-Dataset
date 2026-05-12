





import java.util.List;
import java.util.ArrayList;

public class sqlmodel_schema_Database extends SQLObject {

    private String vendor;
    private String version;



    public sqlmodel_schema_Database(
        String vendor,        String version    ) {
        super(
        );
        this.vendor = vendor;
        this.version = version;
    }


    public String getVendor() {
        return vendor;
    }

    public void setVendor(String vendor) {
        this.vendor = vendor;
    }
    public String getVersion() {
        return version;
    }

    public void setVersion(String version) {
        this.version = version;
    }


}