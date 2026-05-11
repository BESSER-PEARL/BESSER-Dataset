





import java.util.List;
import java.util.ArrayList;

public class bpmn2_Process extends CallableElement, FlowElementsContainer {

    private boolean isClosed;
    private boolean isExecutable;
    private String processType;





    private List<bpmn2_Property> bpmn2_propertys;




    private bpmn2_Participant bpmn2_participant;




    private bpmn2_Collaboration bpmn2_collaboration;




    private List<bpmn2_ResourceRole> bpmn2_resourceroles;




    private List<bpmn2_Artifact> bpmn2_artifacts;




    private bpmn2_Monitoring bpmn2_monitoring;




    private List<bpmn2_Process> bpmn2_processs;




    private bpmn2_Auditing bpmn2_auditing;




    private List<bpmn2_CorrelationSubscription> bpmn2_correlationsubscriptions;


    public bpmn2_Process(
        boolean isClosed,        boolean isExecutable,        String processType    ) {
        super(
        );
        this.isClosed = isClosed;
        this.isExecutable = isExecutable;
        this.processType = processType;
        this.bpmn2_propertys = new ArrayList<>();
        this.bpmn2_resourceroles = new ArrayList<>();
        this.bpmn2_artifacts = new ArrayList<>();
        this.bpmn2_processs = new ArrayList<>();
        this.bpmn2_correlationsubscriptions = new ArrayList<>();
    }

    public bpmn2_Process(
        boolean isClosed,        boolean isExecutable,        String processType        ArrayList<bpmn2_Property> bpmn2_propertys,        ArrayList<bpmn2_ResourceRole> bpmn2_resourceroles,        ArrayList<bpmn2_Artifact> bpmn2_artifacts,        ArrayList<bpmn2_Process> bpmn2_processs,        ArrayList<bpmn2_CorrelationSubscription> bpmn2_correlationsubscriptions    ) {
        this.isClosed = isClosed;
        this.isExecutable = isExecutable;
        this.processType = processType;
        this.bpmn2_propertys = bpmn2_propertys;
        this.bpmn2_resourceroles = bpmn2_resourceroles;
        this.bpmn2_artifacts = bpmn2_artifacts;
        this.bpmn2_processs = bpmn2_processs;
        this.bpmn2_correlationsubscriptions = bpmn2_correlationsubscriptions;
    }

    public boolean getIsclosed() {
        return isClosed;
    }

    public void setIsclosed(boolean isClosed) {
        this.isClosed = isClosed;
    }
    public boolean getIsexecutable() {
        return isExecutable;
    }

    public void setIsexecutable(boolean isExecutable) {
        this.isExecutable = isExecutable;
    }
    public String getProcesstype() {
        return processType;
    }

    public void setProcesstype(String processType) {
        this.processType = processType;
    }

    public List<bpmn2_Property> getBpmn2_propertys() {
        return bpmn2_propertys;
    }

    public void addBpmn2_property(Bpmn2_property bpmn2_property) {
        this.bpmn2_propertys.add(bpmn2_property);
    }
    public bpmn2_Participant getBpmn2_participant() {
        return bpmn2_participant;
    }

    public void setBpmn2_participant(bpmn2_Participant bpmn2_participant) {
        this.bpmn2_participant = bpmn2_participant;
    }
    public bpmn2_Collaboration getBpmn2_collaboration() {
        return bpmn2_collaboration;
    }

    public void setBpmn2_collaboration(bpmn2_Collaboration bpmn2_collaboration) {
        this.bpmn2_collaboration = bpmn2_collaboration;
    }
    public List<bpmn2_ResourceRole> getBpmn2_resourceroles() {
        return bpmn2_resourceroles;
    }

    public void addBpmn2_resourcerole(Bpmn2_resourcerole bpmn2_resourcerole) {
        this.bpmn2_resourceroles.add(bpmn2_resourcerole);
    }
    public List<bpmn2_Artifact> getBpmn2_artifacts() {
        return bpmn2_artifacts;
    }

    public void addBpmn2_artifact(Bpmn2_artifact bpmn2_artifact) {
        this.bpmn2_artifacts.add(bpmn2_artifact);
    }
    public bpmn2_Monitoring getBpmn2_monitoring() {
        return bpmn2_monitoring;
    }

    public void setBpmn2_monitoring(bpmn2_Monitoring bpmn2_monitoring) {
        this.bpmn2_monitoring = bpmn2_monitoring;
    }
    public List<bpmn2_Process> getBpmn2_processs() {
        return bpmn2_processs;
    }

    public void addBpmn2_process(Bpmn2_process bpmn2_process) {
        this.bpmn2_processs.add(bpmn2_process);
    }
    public bpmn2_Auditing getBpmn2_auditing() {
        return bpmn2_auditing;
    }

    public void setBpmn2_auditing(bpmn2_Auditing bpmn2_auditing) {
        this.bpmn2_auditing = bpmn2_auditing;
    }
    public List<bpmn2_CorrelationSubscription> getBpmn2_correlationsubscriptions() {
        return bpmn2_correlationsubscriptions;
    }

    public void addBpmn2_correlationsubscription(Bpmn2_correlationsubscription bpmn2_correlationsubscription) {
        this.bpmn2_correlationsubscriptions.add(bpmn2_correlationsubscription);
    }

}