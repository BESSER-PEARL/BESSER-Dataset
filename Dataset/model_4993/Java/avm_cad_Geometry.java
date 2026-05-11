





import java.util.List;
import java.util.ArrayList;

public class avm_cad_Geometry extends AnalysisConstruct {

    private String GeometryQualifier;
    private String PartIntersectionModifier;



    public avm_cad_Geometry(
        String GeometryQualifier,        String PartIntersectionModifier    ) {
        super(
        );
        this.GeometryQualifier = GeometryQualifier;
        this.PartIntersectionModifier = PartIntersectionModifier;
    }


    public String getGeometryqualifier() {
        return GeometryQualifier;
    }

    public void setGeometryqualifier(String GeometryQualifier) {
        this.GeometryQualifier = GeometryQualifier;
    }
    public String getPartintersectionmodifier() {
        return PartIntersectionModifier;
    }

    public void setPartintersectionmodifier(String PartIntersectionModifier) {
        this.PartIntersectionModifier = PartIntersectionModifier;
    }


}