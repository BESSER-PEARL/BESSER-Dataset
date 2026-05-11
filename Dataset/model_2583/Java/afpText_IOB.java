





import java.util.List;
import java.util.ArrayList;

public class afpText_IOB extends structuredField {

    private String RefCSys;
    private String YocaOset;
    private String XoaOrent;
    private String ObjName;
    private String ObjType;
    private String XoaOset;
    private String YoaOset;
    private String XocaOset;
    private String YoaOrent;



    public afpText_IOB(
        String RefCSys,        String YocaOset,        String XoaOrent,        String ObjName,        String ObjType,        String XoaOset,        String YoaOset,        String XocaOset,        String YoaOrent    ) {
        super(
        );
        this.RefCSys = RefCSys;
        this.YocaOset = YocaOset;
        this.XoaOrent = XoaOrent;
        this.ObjName = ObjName;
        this.ObjType = ObjType;
        this.XoaOset = XoaOset;
        this.YoaOset = YoaOset;
        this.XocaOset = XocaOset;
        this.YoaOrent = YoaOrent;
    }


    public String getRefcsys() {
        return RefCSys;
    }

    public void setRefcsys(String RefCSys) {
        this.RefCSys = RefCSys;
    }
    public String getYocaoset() {
        return YocaOset;
    }

    public void setYocaoset(String YocaOset) {
        this.YocaOset = YocaOset;
    }
    public String getXoaorent() {
        return XoaOrent;
    }

    public void setXoaorent(String XoaOrent) {
        this.XoaOrent = XoaOrent;
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
    public String getXoaoset() {
        return XoaOset;
    }

    public void setXoaoset(String XoaOset) {
        this.XoaOset = XoaOset;
    }
    public String getYoaoset() {
        return YoaOset;
    }

    public void setYoaoset(String YoaOset) {
        this.YoaOset = YoaOset;
    }
    public String getXocaoset() {
        return XocaOset;
    }

    public void setXocaoset(String XocaOset) {
        this.XocaOset = XocaOset;
    }
    public String getYoaorent() {
        return YoaOrent;
    }

    public void setYoaorent(String YoaOrent) {
        this.YoaOrent = YoaOrent;
    }


}