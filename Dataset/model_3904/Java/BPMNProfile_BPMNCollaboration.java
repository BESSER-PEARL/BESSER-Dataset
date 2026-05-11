





import java.util.List;
import java.util.ArrayList;

public class BPMNProfile_BPMNCollaboration extends RootElement {

    private String isClosed;





    private BPMNProfile_BPMNProcess bpmnprofile_bpmnprocess;


    public BPMNProfile_BPMNCollaboration(
        String isClosed    ) {
        super(
        );
        this.isClosed = isClosed;
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