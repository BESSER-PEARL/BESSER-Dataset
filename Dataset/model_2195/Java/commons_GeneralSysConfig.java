





import java.util.List;
import java.util.ArrayList;

public class commons_GeneralSysConfig extends SysConfig, Expandable {

    private String sslSupported;



    public commons_GeneralSysConfig(
        String sslSupported    ) {
        super(
        );
        this.sslSupported = sslSupported;
    }


    public String getSslsupported() {
        return sslSupported;
    }

    public void setSslsupported(String sslSupported) {
        this.sslSupported = sslSupported;
    }


}