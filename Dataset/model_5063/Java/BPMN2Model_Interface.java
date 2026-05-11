





import java.util.List;
import java.util.ArrayList;

public class BPMN2Model_Interface extends RootElement {

    private String name;





    private BPMN2Model_Participant bpmn2model_participant;




    private BPMN2Model_CallableElement bpmn2model_callableelement;




    private BPMN2Model_EObject bpmn2model_eobject;




    private List<BPMN2Model_Operation> bpmn2model_operations;


    public BPMN2Model_Interface(
        String name    ) {
        super(
        );
        this.name = name;
        this.bpmn2model_operations = new ArrayList<>();
    }

    public BPMN2Model_Interface(
        String name        ArrayList<BPMN2Model_Operation> bpmn2model_operations    ) {
        this.name = name;
        this.bpmn2model_operations = bpmn2model_operations;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public BPMN2Model_Participant getBpmn2model_participant() {
        return bpmn2model_participant;
    }

    public void setBpmn2model_participant(BPMN2Model_Participant bpmn2model_participant) {
        this.bpmn2model_participant = bpmn2model_participant;
    }
    public BPMN2Model_CallableElement getBpmn2model_callableelement() {
        return bpmn2model_callableelement;
    }

    public void setBpmn2model_callableelement(BPMN2Model_CallableElement bpmn2model_callableelement) {
        this.bpmn2model_callableelement = bpmn2model_callableelement;
    }
    public BPMN2Model_EObject getBpmn2model_eobject() {
        return bpmn2model_eobject;
    }

    public void setBpmn2model_eobject(BPMN2Model_EObject bpmn2model_eobject) {
        this.bpmn2model_eobject = bpmn2model_eobject;
    }
    public List<BPMN2Model_Operation> getBpmn2model_operations() {
        return bpmn2model_operations;
    }

    public void addBpmn2model_operation(Bpmn2model_operation bpmn2model_operation) {
        this.bpmn2model_operations.add(bpmn2model_operation);
    }

}