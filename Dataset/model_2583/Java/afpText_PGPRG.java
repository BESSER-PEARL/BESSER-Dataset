





import java.util.List;
import java.util.ArrayList;

public class afpText_PGPRG  {

    private String PGorient;
    private String SHside;
    private String RGLength;
    private String PMCid;
    private String PgFlgs;
    private String YmOset;
    private String XmOset;





    private afpText_PGP afptext_pgp;


    public afpText_PGPRG(
        String PGorient,        String SHside,        String RGLength,        String PMCid,        String PgFlgs,        String YmOset,        String XmOset    ) {
        this.PGorient = PGorient;
        this.SHside = SHside;
        this.RGLength = RGLength;
        this.PMCid = PMCid;
        this.PgFlgs = PgFlgs;
        this.YmOset = YmOset;
        this.XmOset = XmOset;
    }


    public String getPgorient() {
        return PGorient;
    }

    public void setPgorient(String PGorient) {
        this.PGorient = PGorient;
    }
    public String getShside() {
        return SHside;
    }

    public void setShside(String SHside) {
        this.SHside = SHside;
    }
    public String getRglength() {
        return RGLength;
    }

    public void setRglength(String RGLength) {
        this.RGLength = RGLength;
    }
    public String getPmcid() {
        return PMCid;
    }

    public void setPmcid(String PMCid) {
        this.PMCid = PMCid;
    }
    public String getPgflgs() {
        return PgFlgs;
    }

    public void setPgflgs(String PgFlgs) {
        this.PgFlgs = PgFlgs;
    }
    public String getYmoset() {
        return YmOset;
    }

    public void setYmoset(String YmOset) {
        this.YmOset = YmOset;
    }
    public String getXmoset() {
        return XmOset;
    }

    public void setXmoset(String XmOset) {
        this.XmOset = XmOset;
    }

    public afpText_PGP getAfptext_pgp() {
        return afptext_pgp;
    }

    public void setAfptext_pgp(afpText_PGP afptext_pgp) {
        this.afptext_pgp = afptext_pgp;
    }

}