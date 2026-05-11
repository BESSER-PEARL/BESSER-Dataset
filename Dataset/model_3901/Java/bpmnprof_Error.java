





import java.util.List;
import java.util.ArrayList;

public class bpmnprof_Error extends ItemDefinition {

    private String errorCode;





    private bpmnprof_BPMNOperation bpmnprof_bpmnoperation;


    public bpmnprof_Error(
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

    public bpmnprof_BPMNOperation getBpmnprof_bpmnoperation() {
        return bpmnprof_bpmnoperation;
    }

    public void setBpmnprof_bpmnoperation(bpmnprof_BPMNOperation bpmnprof_bpmnoperation) {
        this.bpmnprof_bpmnoperation = bpmnprof_bpmnoperation;
    }

}