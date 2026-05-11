





import java.util.List;
import java.util.ArrayList;

public class aadl2_Port extends TriggerPort, PortConnectionEnd, DirectedFeature {

    private String category;



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


}