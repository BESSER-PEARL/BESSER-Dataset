





import java.util.List;
import java.util.ArrayList;

public class afpText_ObjectClassification extends triplet {

    private String RegObjId;
    private String ObjClass;
    private String CompName;
    private String StrucFlgs;
    private String ObjLev;
    private String ObjTpName;



    public afpText_ObjectClassification(
        String RegObjId,        String ObjClass,        String CompName,        String StrucFlgs,        String ObjLev,        String ObjTpName    ) {
        super(
        );
        this.RegObjId = RegObjId;
        this.ObjClass = ObjClass;
        this.CompName = CompName;
        this.StrucFlgs = StrucFlgs;
        this.ObjLev = ObjLev;
        this.ObjTpName = ObjTpName;
    }


    public String getRegobjid() {
        return RegObjId;
    }

    public void setRegobjid(String RegObjId) {
        this.RegObjId = RegObjId;
    }
    public String getObjclass() {
        return ObjClass;
    }

    public void setObjclass(String ObjClass) {
        this.ObjClass = ObjClass;
    }
    public String getCompname() {
        return CompName;
    }

    public void setCompname(String CompName) {
        this.CompName = CompName;
    }
    public String getStrucflgs() {
        return StrucFlgs;
    }

    public void setStrucflgs(String StrucFlgs) {
        this.StrucFlgs = StrucFlgs;
    }
    public String getObjlev() {
        return ObjLev;
    }

    public void setObjlev(String ObjLev) {
        this.ObjLev = ObjLev;
    }
    public String getObjtpname() {
        return ObjTpName;
    }

    public void setObjtpname(String ObjTpName) {
        this.ObjTpName = ObjTpName;
    }


}