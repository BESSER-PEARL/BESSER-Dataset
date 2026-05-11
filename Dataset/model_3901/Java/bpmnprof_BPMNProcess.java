





import java.util.List;
import java.util.ArrayList;

public class bpmnprof_BPMNProcess extends CallableElement, FlowElementsContainer {

    private String processType;
    private String isExecutable;
    private String isClosed;





    private bpmnprof_Monitoring bpmnprof_monitoring;




    private bpmnprof_Auditing bpmnprof_auditing;




    private List<bpmnprof_CorrelationSubscription> bpmnprof_correlationsubscriptions;




    private bpmnprof_Participant bpmnprof_participant;




    private bpmnprof_BPMNProcess bpmnprof_bpmnprocess;




    private bpmnprof_ResourceRole bpmnprof_resourcerole;




    private List<bpmnprof_ResourceRole> bpmnprof_resourceroles;




    private List<bpmnprof_BPMNProperty> bpmnprof_bpmnpropertys;


    public bpmnprof_BPMNProcess(
        String processType,        String isExecutable,        String isClosed    ) {
        super(
        );
        this.processType = processType;
        this.isExecutable = isExecutable;
        this.isClosed = isClosed;
        this.bpmnprof_correlationsubscriptions = new ArrayList<>();
        this.bpmnprof_resourceroles = new ArrayList<>();
        this.bpmnprof_bpmnpropertys = new ArrayList<>();
    }

    public bpmnprof_BPMNProcess(
        String processType,        String isExecutable,        String isClosed        ArrayList<bpmnprof_CorrelationSubscription> bpmnprof_correlationsubscriptions,        ArrayList<bpmnprof_ResourceRole> bpmnprof_resourceroles,        ArrayList<bpmnprof_BPMNProperty> bpmnprof_bpmnpropertys    ) {
        this.processType = processType;
        this.isExecutable = isExecutable;
        this.isClosed = isClosed;
        this.bpmnprof_correlationsubscriptions = bpmnprof_correlationsubscriptions;
        this.bpmnprof_resourceroles = bpmnprof_resourceroles;
        this.bpmnprof_bpmnpropertys = bpmnprof_bpmnpropertys;
    }

    public String getProcesstype() {
        return processType;
    }

    public void setProcesstype(String processType) {
        this.processType = processType;
    }
    public String getIsexecutable() {
        return isExecutable;
    }

    public void setIsexecutable(String isExecutable) {
        this.isExecutable = isExecutable;
    }
    public String getIsclosed() {
        return isClosed;
    }

    public void setIsclosed(String isClosed) {
        this.isClosed = isClosed;
    }

    public bpmnprof_Monitoring getBpmnprof_monitoring() {
        return bpmnprof_monitoring;
    }

    public void setBpmnprof_monitoring(bpmnprof_Monitoring bpmnprof_monitoring) {
        this.bpmnprof_monitoring = bpmnprof_monitoring;
    }
    public bpmnprof_Auditing getBpmnprof_auditing() {
        return bpmnprof_auditing;
    }

    public void setBpmnprof_auditing(bpmnprof_Auditing bpmnprof_auditing) {
        this.bpmnprof_auditing = bpmnprof_auditing;
    }
    public List<bpmnprof_CorrelationSubscription> getBpmnprof_correlationsubscriptions() {
        return bpmnprof_correlationsubscriptions;
    }

    public void addBpmnprof_correlationsubscription(Bpmnprof_correlationsubscription bpmnprof_correlationsubscription) {
        this.bpmnprof_correlationsubscriptions.add(bpmnprof_correlationsubscription);
    }
    public bpmnprof_Participant getBpmnprof_participant() {
        return bpmnprof_participant;
    }

    public void setBpmnprof_participant(bpmnprof_Participant bpmnprof_participant) {
        this.bpmnprof_participant = bpmnprof_participant;
    }
    public bpmnprof_BPMNProcess getBpmnprof_bpmnprocess() {
        return bpmnprof_bpmnprocess;
    }

    public void setBpmnprof_bpmnprocess(bpmnprof_BPMNProcess bpmnprof_bpmnprocess) {
        this.bpmnprof_bpmnprocess = bpmnprof_bpmnprocess;
    }
    public bpmnprof_ResourceRole getBpmnprof_resourcerole() {
        return bpmnprof_resourcerole;
    }

    public void setBpmnprof_resourcerole(bpmnprof_ResourceRole bpmnprof_resourcerole) {
        this.bpmnprof_resourcerole = bpmnprof_resourcerole;
    }
    public List<bpmnprof_ResourceRole> getBpmnprof_resourceroles() {
        return bpmnprof_resourceroles;
    }

    public void addBpmnprof_resourcerole(Bpmnprof_resourcerole bpmnprof_resourcerole) {
        this.bpmnprof_resourceroles.add(bpmnprof_resourcerole);
    }
    public List<bpmnprof_BPMNProperty> getBpmnprof_bpmnpropertys() {
        return bpmnprof_bpmnpropertys;
    }

    public void addBpmnprof_bpmnproperty(Bpmnprof_bpmnproperty bpmnprof_bpmnproperty) {
        this.bpmnprof_bpmnpropertys.add(bpmnprof_bpmnproperty);
    }

}