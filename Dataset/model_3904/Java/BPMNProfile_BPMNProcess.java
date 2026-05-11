





import java.util.List;
import java.util.ArrayList;

public class BPMNProfile_BPMNProcess extends FlowElementsContainer, CallableElement {

    private String processType;
    private String isExecutable;
    private String isClosed;





    private BPMNProfile_BPMNProcess bpmnprofile_bpmnprocess;


    public BPMNProfile_BPMNProcess(
        String processType,        String isExecutable,        String isClosed    ) {
        super(
        );
        this.processType = processType;
        this.isExecutable = isExecutable;
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
    public String getIsclosed() {
        return isClosed;
    }

    public void setIsclosed(String isClosed) {
        this.isClosed = isClosed;
    }

    public BPMNProfile_BPMNProcess getBpmnprofile_bpmnprocess() {
        return bpmnprofile_bpmnprocess;
    }

    public void setBpmnprofile_bpmnprocess(BPMNProfile_BPMNProcess bpmnprofile_bpmnprocess) {
        this.bpmnprofile_bpmnprocess = bpmnprofile_bpmnprocess;
    }

}