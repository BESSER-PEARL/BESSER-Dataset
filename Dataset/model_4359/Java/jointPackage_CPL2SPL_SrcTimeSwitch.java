





import java.util.List;
import java.util.ArrayList;

public class jointPackage_CPL2SPL_SrcTimeSwitch extends SrcSwitch {

    private String tzurl;
    private String tzid;



    public jointPackage_CPL2SPL_SrcTimeSwitch(
        String tzurl,        String tzid    ) {
        super(
        );
        this.tzurl = tzurl;
        this.tzid = tzid;
    }


    public String getTzurl() {
        return tzurl;
    }

    public void setTzurl(String tzurl) {
        this.tzurl = tzurl;
    }
    public String getTzid() {
        return tzid;
    }

    public void setTzid(String tzid) {
        this.tzid = tzid;
    }


}