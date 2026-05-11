





import java.util.List;
import java.util.ArrayList;

public class afpText_ResourceObjectType extends triplet {

    private String ObjType;
    private String ConData;



    public afpText_ResourceObjectType(
        String ObjType,        String ConData    ) {
        super(
        );
        this.ObjType = ObjType;
        this.ConData = ConData;
    }


    public String getObjtype() {
        return ObjType;
    }

    public void setObjtype(String ObjType) {
        this.ObjType = ObjType;
    }
    public String getCondata() {
        return ConData;
    }

    public void setCondata(String ConData) {
        this.ConData = ConData;
    }


}