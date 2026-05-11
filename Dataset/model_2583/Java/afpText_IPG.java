





import java.util.List;
import java.util.ArrayList;

public class afpText_IPG extends structuredField {

    private String PgName;
    private String IPgFlgs;



    public afpText_IPG(
        String PgName,        String IPgFlgs    ) {
        super(
        );
        this.PgName = PgName;
        this.IPgFlgs = IPgFlgs;
    }


    public String getPgname() {
        return PgName;
    }

    public void setPgname(String PgName) {
        this.PgName = PgName;
    }
    public String getIpgflgs() {
        return IPgFlgs;
    }

    public void setIpgflgs(String IPgFlgs) {
        this.IPgFlgs = IPgFlgs;
    }


}