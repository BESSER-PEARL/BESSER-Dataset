





import java.util.List;
import java.util.ArrayList;

public class BPMN2Model_Process extends FlowElementsContainer, CallableElement {

    private boolean isClosed;
    private String processType;
    private boolean isExecutable;





    private List<BPMN2Model_Process> bpmn2model_processs;




    private BPMN2Model_Monitoring bpmn2model_monitoring;




    private BPMN2Model_Participant bpmn2model_participant;


    public BPMN2Model_Process(
        boolean isClosed,        String processType,        boolean isExecutable    ) {
        super(
        );
        this.isClosed = isClosed;
        this.processType = processType;
        this.isExecutable = isExecutable;
        this.bpmn2model_processs = new ArrayList<>();
    }

    public BPMN2Model_Process(
        boolean isClosed,        String processType,        boolean isExecutable        ArrayList<BPMN2Model_Process> bpmn2model_processs    ) {
        this.isClosed = isClosed;
        this.processType = processType;
        this.isExecutable = isExecutable;
        this.bpmn2model_processs = bpmn2model_processs;
    }

    public boolean getIsclosed() {
        return isClosed;
    }

    public void setIsclosed(boolean isClosed) {
        this.isClosed = isClosed;
    }
    public String getProcesstype() {
        return processType;
    }

    public void setProcesstype(String processType) {
        this.processType = processType;
    }
    public boolean getIsexecutable() {
        return isExecutable;
    }

    public void setIsexecutable(boolean isExecutable) {
        this.isExecutable = isExecutable;
    }

    public List<BPMN2Model_Process> getBpmn2model_processs() {
        return bpmn2model_processs;
    }

    public void addBpmn2model_process(Bpmn2model_process bpmn2model_process) {
        this.bpmn2model_processs.add(bpmn2model_process);
    }
    public BPMN2Model_Monitoring getBpmn2model_monitoring() {
        return bpmn2model_monitoring;
    }

    public void setBpmn2model_monitoring(BPMN2Model_Monitoring bpmn2model_monitoring) {
        this.bpmn2model_monitoring = bpmn2model_monitoring;
    }
    public BPMN2Model_Participant getBpmn2model_participant() {
        return bpmn2model_participant;
    }

    public void setBpmn2model_participant(BPMN2Model_Participant bpmn2model_participant) {
        this.bpmn2model_participant = bpmn2model_participant;
    }

}