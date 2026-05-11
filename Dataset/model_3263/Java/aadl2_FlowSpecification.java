





import java.util.List;
import java.util.ArrayList;

public class aadl2_FlowSpecification extends FlowElement, FlowFeature, ModalPath {

    private String kind;





    private aadl2_FlowSpecification aadl2_flowspecification;




    private aadl2_FlowEnd aadl2_flowend;




    private aadl2_FlowEnd aadl2_flowend;




    private aadl2_FlowImplementation aadl2_flowimplementation;




    private aadl2_ComponentType aadl2_componenttype;


    public aadl2_FlowSpecification(
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
    public aadl2_FlowEnd getAadl2_flowend() {
        return aadl2_flowend;
    }

    public void setAadl2_flowend(aadl2_FlowEnd aadl2_flowend) {
        this.aadl2_flowend = aadl2_flowend;
    }
    public aadl2_FlowEnd getAadl2_flowend() {
        return aadl2_flowend;
    }

    public void setAadl2_flowend(aadl2_FlowEnd aadl2_flowend) {
        this.aadl2_flowend = aadl2_flowend;
    }
    public aadl2_FlowImplementation getAadl2_flowimplementation() {
        return aadl2_flowimplementation;
    }

    public void setAadl2_flowimplementation(aadl2_FlowImplementation aadl2_flowimplementation) {
        this.aadl2_flowimplementation = aadl2_flowimplementation;
    }
    public aadl2_ComponentType getAadl2_componenttype() {
        return aadl2_componenttype;
    }

    public void setAadl2_componenttype(aadl2_ComponentType aadl2_componenttype) {
        this.aadl2_componenttype = aadl2_componenttype;
    }

}