





import java.util.List;
import java.util.ArrayList;

public class BPMNProfile_Error extends ItemDefinition {

    private String errorCode;





    private BPMNProfile_BPMNOperation bpmnprofile_bpmnoperation;


    public BPMNProfile_Error(
        String errorCode    ) {
        super(
        );
        this.errorCode = errorCode;
    }


    public String getErrorcode() {
        return errorCode;
    }

    public void setErrorcode(String errorCode) {
        this.errorCode = errorCode;
    }

    public BPMNProfile_BPMNOperation getBpmnprofile_bpmnoperation() {
        return bpmnprofile_bpmnoperation;
    }

    public void setBpmnprofile_bpmnoperation(BPMNProfile_BPMNOperation bpmnprofile_bpmnoperation) {
        this.bpmnprofile_bpmnoperation = bpmnprofile_bpmnoperation;
    }

}