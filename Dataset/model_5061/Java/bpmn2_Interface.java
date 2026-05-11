





import java.util.List;
import java.util.ArrayList;

public class bpmn2_Interface extends RootElement {

    private String name;





    private List<bpmn2_Operation> bpmn2_operations;




    private bpmn2_Participant bpmn2_participant;




    private bpmn2_EObject bpmn2_eobject;


    public bpmn2_Interface(
        String name    ) {
        super(
        );
        this.name = name;
        this.bpmn2_operations = new ArrayList<>();
    }

    public bpmn2_Interface(
        String name        ArrayList<bpmn2_Operation> bpmn2_operations    ) {
        this.name = name;
        this.bpmn2_operations = bpmn2_operations;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<bpmn2_Operation> getBpmn2_operations() {
        return bpmn2_operations;
    }

    public void addBpmn2_operation(Bpmn2_operation bpmn2_operation) {
        this.bpmn2_operations.add(bpmn2_operation);
    }
    public bpmn2_Participant getBpmn2_participant() {
        return bpmn2_participant;
    }

    public void setBpmn2_participant(bpmn2_Participant bpmn2_participant) {
        this.bpmn2_participant = bpmn2_participant;
    }
    public bpmn2_EObject getBpmn2_eobject() {
        return bpmn2_eobject;
    }

    public void setBpmn2_eobject(bpmn2_EObject bpmn2_eobject) {
        this.bpmn2_eobject = bpmn2_eobject;
    }

}