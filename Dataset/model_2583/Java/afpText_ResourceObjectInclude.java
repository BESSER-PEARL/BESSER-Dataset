





import java.util.List;
import java.util.ArrayList;

public class afpText_ResourceObjectInclude extends triplet {

    private String YobjOset;
    private String ObjName;
    private String ObjType;
    private String ObOrent;
    private String XobjOset;



    public afpText_ResourceObjectInclude(
        String YobjOset,        String ObjName,        String ObjType,        String ObOrent,        String XobjOset    ) {
        super(
        );
        this.YobjOset = YobjOset;
        this.ObjName = ObjName;
        this.ObjType = ObjType;
        this.ObOrent = ObOrent;
        this.XobjOset = XobjOset;
    }


    public String getYobjoset() {
        return YobjOset;
    }

    public void setYobjoset(String YobjOset) {
        this.YobjOset = YobjOset;
    }
    public String getObjname() {
        return ObjName;
    }

    public void setObjname(String ObjName) {
        this.ObjName = ObjName;
    }
    public String getObjtype() {
        return ObjType;
    }

    public void setObjtype(String ObjType) {
        this.ObjType = ObjType;
    }
    public String getOborent() {
        return ObOrent;
    }

    public void setOborent(String ObOrent) {
        this.ObOrent = ObOrent;
    }
    public String getXobjoset() {
        return XobjOset;
    }

    public void setXobjoset(String XobjOset) {
        this.XobjOset = XobjOset;
    }


}