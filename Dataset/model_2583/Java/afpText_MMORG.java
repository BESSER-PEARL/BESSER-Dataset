





import java.util.List;
import java.util.ArrayList;

public class afpText_MMORG  {

    private String Flags;
    private String OVLname;
    private String OVLid;





    private afpText_MMO afptext_mmo;


    public afpText_MMORG(
        String Flags,        String OVLname,        String OVLid    ) {
        this.Flags = Flags;
        this.OVLname = OVLname;
        this.OVLid = OVLid;
    }


    public String getFlags() {
        return Flags;
    }

    public void setFlags(String Flags) {
        this.Flags = Flags;
    }
    public String getOvlname() {
        return OVLname;
    }

    public void setOvlname(String OVLname) {
        this.OVLname = OVLname;
    }
    public String getOvlid() {
        return OVLid;
    }

    public void setOvlid(String OVLid) {
        this.OVLid = OVLid;
    }

    public afpText_MMO getAfptext_mmo() {
        return afptext_mmo;
    }

    public void setAfptext_mmo(afpText_MMO afptext_mmo) {
        this.afptext_mmo = afptext_mmo;
    }

}