





import java.util.List;
import java.util.ArrayList;

public class OCL_Attribute extends OclFeature {

    private String name;





    private OclType ocltype;


    public OCL_Attribute(
        String name    ) {
        super(
        );
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public OclType getOcltype() {
        return ocltype;
    }

    public void setOcltype(OclType ocltype) {
        this.ocltype = ocltype;
    }

}