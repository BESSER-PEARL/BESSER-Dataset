





import java.util.List;
import java.util.ArrayList;

public class RefOntoUML_ReferenceStructure extends DataType {






    private List<RefOntoUML_ReferenceRegion> refontouml_referenceregions;




    private RefOntoUML_ReferenceRegion refontouml_referenceregion;


    public RefOntoUML_ReferenceStructure(
    ) {
        super(
        );
        this.refontouml_referenceregions = new ArrayList<>();
    }

    public RefOntoUML_ReferenceStructure(
        ArrayList<RefOntoUML_ReferenceRegion> refontouml_referenceregions    ) {
        this.refontouml_referenceregions = refontouml_referenceregions;
    }


    public List<RefOntoUML_ReferenceRegion> getRefontouml_referenceregions() {
        return refontouml_referenceregions;
    }

    public void addRefontouml_referenceregion(Refontouml_referenceregion refontouml_referenceregion) {
        this.refontouml_referenceregions.add(refontouml_referenceregion);
    }
    public RefOntoUML_ReferenceRegion getRefontouml_referenceregion() {
        return refontouml_referenceregion;
    }

    public void setRefontouml_referenceregion(RefOntoUML_ReferenceRegion refontouml_referenceregion) {
        this.refontouml_referenceregion = refontouml_referenceregion;
    }

}