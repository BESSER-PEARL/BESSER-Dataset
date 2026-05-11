





import java.util.List;
import java.util.ArrayList;

public class bpmnprof_BPMNOperation extends BaseElement {






    private bpmnprof_ServiceTask bpmnprof_servicetask;




    private bpmnprof_InputOutputBinding bpmnprof_inputoutputbinding;




    private bpmnprof_SendTask bpmnprof_sendtask;




    private bpmnprof_ReceiveTask bpmnprof_receivetask;




    private bpmnprof_Element bpmnprof_element;


    public bpmnprof_BPMNOperation(
    ) {
        super(
        );
    }



    public bpmnprof_ServiceTask getBpmnprof_servicetask() {
        return bpmnprof_servicetask;
    }

    public void setBpmnprof_servicetask(bpmnprof_ServiceTask bpmnprof_servicetask) {
        this.bpmnprof_servicetask = bpmnprof_servicetask;
    }
    public bpmnprof_InputOutputBinding getBpmnprof_inputoutputbinding() {
        return bpmnprof_inputoutputbinding;
    }

    public void setBpmnprof_inputoutputbinding(bpmnprof_InputOutputBinding bpmnprof_inputoutputbinding) {
        this.bpmnprof_inputoutputbinding = bpmnprof_inputoutputbinding;
    }
    public bpmnprof_SendTask getBpmnprof_sendtask() {
        return bpmnprof_sendtask;
    }

    public void setBpmnprof_sendtask(bpmnprof_SendTask bpmnprof_sendtask) {
        this.bpmnprof_sendtask = bpmnprof_sendtask;
    }
    public bpmnprof_ReceiveTask getBpmnprof_receivetask() {
        return bpmnprof_receivetask;
    }

    public void setBpmnprof_receivetask(bpmnprof_ReceiveTask bpmnprof_receivetask) {
        this.bpmnprof_receivetask = bpmnprof_receivetask;
    }
    public bpmnprof_Element getBpmnprof_element() {
        return bpmnprof_element;
    }

    public void setBpmnprof_element(bpmnprof_Element bpmnprof_element) {
        this.bpmnprof_element = bpmnprof_element;
    }

}