





import java.util.List;
import java.util.ArrayList;

public class afpText_MSURG  {

    private String SUPname;
    private String Reserved;
    private String SUPid;





    private afpText_MSU afptext_msu;


    public afpText_MSURG(
        String SUPname,        String Reserved,        String SUPid    ) {
        this.SUPname = SUPname;
        this.Reserved = Reserved;
        this.SUPid = SUPid;
    }


    public String getSupname() {
        return SUPname;
    }

    public void setSupname(String SUPname) {
        this.SUPname = SUPname;
    }
    public String getReserved() {
        return Reserved;
    }

    public void setReserved(String Reserved) {
        this.Reserved = Reserved;
    }
    public String getSupid() {
        return SUPid;
    }

    public void setSupid(String SUPid) {
        this.SUPid = SUPid;
    }

    public afpText_MSU getAfptext_msu() {
        return afptext_msu;
    }

    public void setAfptext_msu(afpText_MSU afptext_msu) {
        this.afptext_msu = afptext_msu;
    }

}