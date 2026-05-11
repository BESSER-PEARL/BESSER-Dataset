





import java.util.List;
import java.util.ArrayList;

public class bpmn2_InputSet extends BaseElement {

    private String name;





    private bpmn2_InputOutputSpecification bpmn2_inputoutputspecification;


    public bpmn2_InputSet(
        String name    ) {
        super(
        );
        this.name = name;
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

}