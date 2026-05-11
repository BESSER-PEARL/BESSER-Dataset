





import java.util.List;
import java.util.ArrayList;

public class aadl2_FlowImplementation extends ModalPath, StructuralFeature {

    private String kind;





    private aadl2_FlowSpecification aadl2_flowspecification;


    public aadl2_FlowImplementation(
        String kind    ) {
        super(
        );
        this.kind = kind;
    }


    public String getKind() {
        return kind;
    }

    public void setKind(String kind) {
        this.kind = kind;
    }

    public aadl2_FlowSpecification getAadl2_flowspecification() {
        return aadl2_flowspecification;
    }

    public void setAadl2_flowspecification(aadl2_FlowSpecification aadl2_flowspecification) {
        this.aadl2_flowspecification = aadl2_flowspecification;
    }

}