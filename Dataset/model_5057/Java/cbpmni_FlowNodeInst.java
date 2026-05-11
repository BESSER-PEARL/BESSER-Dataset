





import java.util.List;
import java.util.ArrayList;

public class cbpmni_FlowNodeInst  {

    private String status;





    private cbpmni_ProcessInst cbpmni_processinst;




    private cbpmni_FlowNodeInst cbpmni_flownodeinst;




    private cbpmni_ProcessInst cbpmni_processinst;


    public cbpmni_FlowNodeInst(
        String status    ) {
        this.status = status;
    }


    public String getStatus() {
        return status;
    }

    public void setStatus(String status) {
        this.status = status;
    }

    public cbpmni_ProcessInst getCbpmni_processinst() {
        return cbpmni_processinst;
    }

    public void setCbpmni_processinst(cbpmni_ProcessInst cbpmni_processinst) {
        this.cbpmni_processinst = cbpmni_processinst;
    }
    public cbpmni_FlowNodeInst getCbpmni_flownodeinst() {
        return cbpmni_flownodeinst;
    }

    public void setCbpmni_flownodeinst(cbpmni_FlowNodeInst cbpmni_flownodeinst) {
        this.cbpmni_flownodeinst = cbpmni_flownodeinst;
    }
    public cbpmni_ProcessInst getCbpmni_processinst() {
        return cbpmni_processinst;
    }

    public void setCbpmni_processinst(cbpmni_ProcessInst cbpmni_processinst) {
        this.cbpmni_processinst = cbpmni_processinst;
    }

}