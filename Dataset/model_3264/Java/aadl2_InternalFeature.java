





import java.util.List;
import java.util.ArrayList;

public class aadl2_InternalFeature extends StructuralFeature, ModalElement, PortConnectionEnd, FeatureConnectionEnd, TriggerPort {

    private String direction;



    public aadl2_InternalFeature(
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


}