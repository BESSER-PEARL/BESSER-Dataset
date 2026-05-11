





import java.util.List;
import java.util.ArrayList;

public class bpmn2_CallableElement extends RootElement {

    private String name;





    private bpmn2_CallActivity bpmn2_callactivity;




    private List<bpmn2_Interface> bpmn2_interfaces;


    public bpmn2_CallableElement(
        String name    ) {
        super(
        );
        this.name = name;
        this.bpmn2_interfaces = new ArrayList<>();
    }

    public bpmn2_CallableElement(
        String name        ArrayList<bpmn2_Interface> bpmn2_interfaces    ) {
        this.name = name;
        this.bpmn2_interfaces = bpmn2_interfaces;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public bpmn2_CallActivity getBpmn2_callactivity() {
        return bpmn2_callactivity;
    }

    public void setBpmn2_callactivity(bpmn2_CallActivity bpmn2_callactivity) {
        this.bpmn2_callactivity = bpmn2_callactivity;
    }
    public List<bpmn2_Interface> getBpmn2_interfaces() {
        return bpmn2_interfaces;
    }

    public void addBpmn2_interface(Bpmn2_interface bpmn2_interface) {
        this.bpmn2_interfaces.add(bpmn2_interface);
    }

}