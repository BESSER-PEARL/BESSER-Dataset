





import java.util.List;
import java.util.ArrayList;

public class UMLModel_StructuralFeatureAction extends Action {

    private String structuralFeature;



    public UMLModel_StructuralFeatureAction(
        String structuralFeature    ) {
        super(
        );
        this.structuralFeature = structuralFeature;
    }


    public String getStructuralfeature() {
        return structuralFeature;
    }

    public void setStructuralfeature(String structuralFeature) {
        this.structuralFeature = structuralFeature;
    }


}