





import java.util.List;
import java.util.ArrayList;

public class BPMN2Model_CorrelationKey extends BaseElement {

    private String name;





    private BPMN2Model_ChoreographyActivity bpmn2model_choreographyactivity;




    private BPMN2Model_CorrelationSubscription bpmn2model_correlationsubscription;


    public BPMN2Model_CorrelationKey(
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

    public BPMN2Model_ChoreographyActivity getBpmn2model_choreographyactivity() {
        return bpmn2model_choreographyactivity;
    }

    public void setBpmn2model_choreographyactivity(BPMN2Model_ChoreographyActivity bpmn2model_choreographyactivity) {
        this.bpmn2model_choreographyactivity = bpmn2model_choreographyactivity;
    }
    public BPMN2Model_CorrelationSubscription getBpmn2model_correlationsubscription() {
        return bpmn2model_correlationsubscription;
    }

    public void setBpmn2model_correlationsubscription(BPMN2Model_CorrelationSubscription bpmn2model_correlationsubscription) {
        this.bpmn2model_correlationsubscription = bpmn2model_correlationsubscription;
    }

}