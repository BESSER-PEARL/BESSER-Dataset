





import java.util.List;
import java.util.ArrayList;

public class aadl2_Port extends PortConnectionEnd, DirectedFeature {

    private String category;





    private aadl2_TriggerPort aadl2_triggerport;


    public aadl2_Port(
        String category    ) {
        super(
        );
        this.category = category;
    }


    public String getCategory() {
        return category;
    }

    public void setCategory(String category) {
        this.category = category;
    }

    public aadl2_TriggerPort getAadl2_triggerport() {
        return aadl2_triggerport;
    }

    public void setAadl2_triggerport(aadl2_TriggerPort aadl2_triggerport) {
        this.aadl2_triggerport = aadl2_triggerport;
    }

}