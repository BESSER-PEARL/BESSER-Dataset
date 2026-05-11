





import java.util.List;
import java.util.ArrayList;

public class afpText_ObjectFunctionSetSpecification extends triplet {

    private String ObjType;
    private String DCAFnSet;
    private String OCAFnSet;
    private String ArchVrsn;



    public afpText_ObjectFunctionSetSpecification(
        String ObjType,        String DCAFnSet,        String OCAFnSet,        String ArchVrsn    ) {
        super(
        );
        this.ObjType = ObjType;
        this.DCAFnSet = DCAFnSet;
        this.OCAFnSet = OCAFnSet;
        this.ArchVrsn = ArchVrsn;
    }


    public String getObjtype() {
        return ObjType;
    }

    public void setObjtype(String ObjType) {
        this.ObjType = ObjType;
    }
    public String getDcafnset() {
        return DCAFnSet;
    }

    public void setDcafnset(String DCAFnSet) {
        this.DCAFnSet = DCAFnSet;
    }
    public String getOcafnset() {
        return OCAFnSet;
    }

    public void setOcafnset(String OCAFnSet) {
        this.OCAFnSet = OCAFnSet;
    }
    public String getArchvrsn() {
        return ArchVrsn;
    }

    public void setArchvrsn(String ArchVrsn) {
        this.ArchVrsn = ArchVrsn;
    }


}