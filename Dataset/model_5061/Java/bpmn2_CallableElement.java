





import java.util.List;
import java.util.ArrayList;

public class bpmn2_CallableElement extends RootElement {

    private String name;





    private bpmn2_InputOutputSpecification bpmn2_inputoutputspecification;




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

    public bpmn2_InputOutputSpecification getBpmn2_inputoutputspecification() {
        return bpmn2_inputoutputspecification;
    }

    public void setBpmn2_inputoutputspecification(bpmn2_InputOutputSpecification bpmn2_inputoutputspecification) {
        this.bpmn2_inputoutputspecification = bpmn2_inputoutputspecification;
    }
    public List<bpmn2_Interface> getBpmn2_interfaces() {
        return bpmn2_interfaces;
    }

    public void addBpmn2_interface(Bpmn2_interface bpmn2_interface) {
        this.bpmn2_interfaces.add(bpmn2_interface);
    }

}