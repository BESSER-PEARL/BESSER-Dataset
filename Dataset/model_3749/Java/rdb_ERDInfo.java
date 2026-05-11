





import java.util.List;
import java.util.ArrayList;

public class rdb_ERDInfo  {

    private String version;
    private boolean autoLayout;





    private rdb_Style rdb_style;


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

    public rdb_Style getRdb_style() {
        return rdb_style;
    }

    public void setRdb_style(rdb_Style rdb_style) {
        this.rdb_style = rdb_style;
    }

}