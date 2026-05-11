





import java.util.List;
import java.util.ArrayList;

public class BPMN2Model_CallableElement extends RootElement {

    private String name;





    private BPMN2Model_InputOutputSpecification bpmn2model_inputoutputspecification;




    private BPMN2Model_CallActivity bpmn2model_callactivity;


    public BPMN2Model_CallableElement(
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

    public BPMN2Model_InputOutputSpecification getBpmn2model_inputoutputspecification() {
        return bpmn2model_inputoutputspecification;
    }

    public void setBpmn2model_inputoutputspecification(BPMN2Model_InputOutputSpecification bpmn2model_inputoutputspecification) {
        this.bpmn2model_inputoutputspecification = bpmn2model_inputoutputspecification;
    }
    public BPMN2Model_CallActivity getBpmn2model_callactivity() {
        return bpmn2model_callactivity;
    }

    public void setBpmn2model_callactivity(BPMN2Model_CallActivity bpmn2model_callactivity) {
        this.bpmn2model_callactivity = bpmn2model_callactivity;
    }

}