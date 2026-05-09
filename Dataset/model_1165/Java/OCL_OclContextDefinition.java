





import java.util.List;
import java.util.ArrayList;

public class OCL_OclContextDefinition extends LocatedElement {






    private OclFeatureDefinition oclfeaturedefinition;




    private OclType ocltype;


    public OCL_OclContextDefinition(
    ) {
        super(
        );
    }



    public OclFeatureDefinition getOclfeaturedefinition() {
        return oclfeaturedefinition;
    }

    public void setOclfeaturedefinition(OclFeatureDefinition oclfeaturedefinition) {
        this.oclfeaturedefinition = oclfeaturedefinition;
    }
    public OclType getOcltype() {
        return ocltype;
    }

    public void setOcltype(OclType ocltype) {
        this.ocltype = ocltype;
    }

}