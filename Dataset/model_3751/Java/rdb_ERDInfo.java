





import java.util.List;
import java.util.ArrayList;

public class rdb_ERDInfo  {

    private boolean autoLayout;
    private String version;



    public rdb_ERDInfo(
        boolean autoLayout,        String version    ) {
        this.autoLayout = autoLayout;
        this.version = version;
    }


    public boolean getAutolayout() {
        return autoLayout;
    }

    public void setAutolayout(boolean autoLayout) {
        this.autoLayout = autoLayout;
    }
    public String getVersion() {
        return version;
    }

    public void setVersion(String version) {
        this.version = version;
    }


}