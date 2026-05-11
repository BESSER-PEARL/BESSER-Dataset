





import java.util.List;
import java.util.ArrayList;

public class avm_cad_Geometry extends AnalysisConstruct {

    private String PartIntersectionModifier;
    private String GeometryQualifier;



    public avm_cad_Geometry(
        String PartIntersectionModifier,        String GeometryQualifier    ) {
        super(
        );
        this.PartIntersectionModifier = PartIntersectionModifier;
        this.GeometryQualifier = GeometryQualifier;
    }


    public String getPartintersectionmodifier() {
        return PartIntersectionModifier;
    }

    public void setPartintersectionmodifier(String PartIntersectionModifier) {
        this.PartIntersectionModifier = PartIntersectionModifier;
    }
    public String getGeometryqualifier() {
        return GeometryQualifier;
    }

    public void setGeometryqualifier(String GeometryQualifier) {
        this.GeometryQualifier = GeometryQualifier;
    }


}