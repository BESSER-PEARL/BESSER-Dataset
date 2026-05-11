





import java.util.List;
import java.util.ArrayList;

public class BPMNProfile_BPMNProcess extends CallableElement, FlowElementsContainer {

    private String isClosed;
    private String processType;
    private String isExecutable;





    private BPMNProfile_Auditing bpmnprofile_auditing;




    private List<BPMNProfile_ResourceRole> bpmnprofile_resourceroles;




    private List<BPMNProfile_CorrelationSubscription> bpmnprofile_correlationsubscriptions;




    private BPMNProfile_BPMNProcess bpmnprofile_bpmnprocess;




    private BPMNProfile_Monitoring bpmnprofile_monitoring;




    private BPMNProfile_Participant bpmnprofile_participant;




    private BPMNProfile_ResourceRole bpmnprofile_resourcerole;


    public BPMNProfile_BPMNProcess(
        String isClosed,        String processType,        String isExecutable    ) {
        super(
        );
        this.isClosed = isClosed;
        this.processType = processType;
        this.isExecutable = isExecutable;
        this.bpmnprofile_resourceroles = new ArrayList<>();
        this.bpmnprofile_correlationsubscriptions = new ArrayList<>();
    }

    public BPMNProfile_BPMNProcess(
        String isClosed,        String processType,        String isExecutable        ArrayList<BPMNProfile_ResourceRole> bpmnprofile_resourceroles,        ArrayList<BPMNProfile_CorrelationSubscription> bpmnprofile_correlationsubscriptions    ) {
        this.isClosed = isClosed;
        this.processType = processType;
        this.isExecutable = isExecutable;
        this.bpmnprofile_resourceroles = bpmnprofile_resourceroles;
        this.bpmnprofile_correlationsubscriptions = bpmnprofile_correlationsubscriptions;
    }

    public String getIsclosed() {
        return isClosed;
    }

    public void setIsclosed(String isClosed) {
        this.isClosed = isClosed;
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

    public BPMNProfile_Auditing getBpmnprofile_auditing() {
        return bpmnprofile_auditing;
    }

    public void setBpmnprofile_auditing(BPMNProfile_Auditing bpmnprofile_auditing) {
        this.bpmnprofile_auditing = bpmnprofile_auditing;
    }
    public List<BPMNProfile_ResourceRole> getBpmnprofile_resourceroles() {
        return bpmnprofile_resourceroles;
    }

    public void addBpmnprofile_resourcerole(Bpmnprofile_resourcerole bpmnprofile_resourcerole) {
        this.bpmnprofile_resourceroles.add(bpmnprofile_resourcerole);
    }
    public List<BPMNProfile_CorrelationSubscription> getBpmnprofile_correlationsubscriptions() {
        return bpmnprofile_correlationsubscriptions;
    }

    public void addBpmnprofile_correlationsubscription(Bpmnprofile_correlationsubscription bpmnprofile_correlationsubscription) {
        this.bpmnprofile_correlationsubscriptions.add(bpmnprofile_correlationsubscription);
    }
    public BPMNProfile_BPMNProcess getBpmnprofile_bpmnprocess() {
        return bpmnprofile_bpmnprocess;
    }

    public void setBpmnprofile_bpmnprocess(BPMNProfile_BPMNProcess bpmnprofile_bpmnprocess) {
        this.bpmnprofile_bpmnprocess = bpmnprofile_bpmnprocess;
    }
    public BPMNProfile_Monitoring getBpmnprofile_monitoring() {
        return bpmnprofile_monitoring;
    }

    public void setBpmnprofile_monitoring(BPMNProfile_Monitoring bpmnprofile_monitoring) {
        this.bpmnprofile_monitoring = bpmnprofile_monitoring;
    }
    public BPMNProfile_Participant getBpmnprofile_participant() {
        return bpmnprofile_participant;
    }

    public void setBpmnprofile_participant(BPMNProfile_Participant bpmnprofile_participant) {
        this.bpmnprofile_participant = bpmnprofile_participant;
    }
    public BPMNProfile_ResourceRole getBpmnprofile_resourcerole() {
        return bpmnprofile_resourcerole;
    }

    public void setBpmnprofile_resourcerole(BPMNProfile_ResourceRole bpmnprofile_resourcerole) {
        this.bpmnprofile_resourcerole = bpmnprofile_resourcerole;
    }

}