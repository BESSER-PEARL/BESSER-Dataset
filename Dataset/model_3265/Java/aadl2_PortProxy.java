





import java.util.List;
import java.util.ArrayList;

public class aadl2_PortProxy extends PortConnectionEnd, ProcessorFeature, TriggerPort, FeatureConnectionEnd {

    private String direction;





    private aadl2_DataClassifier aadl2_dataclassifier;




    private aadl2_ComponentImplementation aadl2_componentimplementation;


    public aadl2_PortProxy(
        String direction    ) {
        super(
        );
        this.direction = direction;
    }


    public String getDirection() {
        return direction;
    }

    public void setDirection(String direction) {
        this.direction = direction;
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