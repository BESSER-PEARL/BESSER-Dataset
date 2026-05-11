





import java.util.List;
import java.util.ArrayList;

public class rdb_ERDInfo  {

    private String version;
    private boolean autoLayout;



    public rdb_ERDInfo(
        String version,        boolean autoLayout    ) {
        this.version = version;
        this.autoLayout = autoLayout;
    }


    public String getVersion() {
        return version;
    }

    public void setVersion(String version) {
        this.version = version;
    }
    public boolean getAutolayout() {
        return autoLayout;
    }

    public void setAutolayout(boolean autoLayout) {
        this.autoLayout = autoLayout;
    }


}