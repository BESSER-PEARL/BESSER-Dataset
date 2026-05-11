





import java.util.List;
import java.util.ArrayList;

public class afpText_ObjectOffset extends triplet {

    private String ObjTpe;
    private String ObjOset;
    private String ObjOstHi;



    public afpText_ObjectOffset(
        String ObjTpe,        String ObjOset,        String ObjOstHi    ) {
        super(
        );
        this.ObjTpe = ObjTpe;
        this.ObjOset = ObjOset;
        this.ObjOstHi = ObjOstHi;
    }


    public String getObjtpe() {
        return ObjTpe;
    }

    public void setObjtpe(String ObjTpe) {
        this.ObjTpe = ObjTpe;
    }
    public String getObjoset() {
        return ObjOset;
    }

    public void setObjoset(String ObjOset) {
        this.ObjOset = ObjOset;
    }
    public String getObjosthi() {
        return ObjOstHi;
    }

    public void setObjosthi(String ObjOstHi) {
        this.ObjOstHi = ObjOstHi;
    }


}