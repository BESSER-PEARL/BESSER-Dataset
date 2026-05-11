





import java.util.List;
import java.util.ArrayList;

public class aadl2_PortProxy extends FeatureConnectionEnd, TriggerPort, PortConnectionEnd, ProcessorFeature {

    private String out;
    private String direction;
    private String in_;





    private aadl2_DataClassifier aadl2_dataclassifier;




    private aadl2_ComponentImplementation aadl2_componentimplementation;


    public aadl2_PortProxy(
        String out,        String direction,        String in_    ) {
        super(
        );
        this.out = out;
        this.direction = direction;
        this.in_ = in_;
    }


    public String getOut() {
        return out;
    }

    public void setOut(String out) {
        this.out = out;
    }
    public String getDirection() {
        return direction;
    }

    public void setDirection(String direction) {
        this.direction = direction;
    }
    public String getIn_() {
        return in_;
    }

    public void setIn_(String in_) {
        this.in_ = in_;
    }

    public aadl2_DataClassifier getAadl2_dataclassifier() {
        return aadl2_dataclassifier;
    }

    public void setAadl2_dataclassifier(aadl2_DataClassifier aadl2_dataclassifier) {
        this.aadl2_dataclassifier = aadl2_dataclassifier;
    }
    public aadl2_ComponentImplementation getAadl2_componentimplementation() {
        return aadl2_componentimplementation;
    }

    public void setAadl2_componentimplementation(aadl2_ComponentImplementation aadl2_componentimplementation) {
        this.aadl2_componentimplementation = aadl2_componentimplementation;
    }

}