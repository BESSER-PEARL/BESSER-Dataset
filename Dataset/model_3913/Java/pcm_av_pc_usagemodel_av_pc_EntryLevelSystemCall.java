





import java.util.List;
import java.util.ArrayList;

public class pcm_av_pc_usagemodel_av_pc_EntryLevelSystemCall extends AbstractUserAction {

    private int priority;





    private OperationProvidedRole operationprovidedrole;


    public pcm_av_pc_usagemodel_av_pc_EntryLevelSystemCall(
        int priority    ) {
        super(
        );
        this.priority = priority;
    }


    public int getPriority() {
        return priority;
    }

    public void setPriority(int priority) {
        this.priority = priority;
    }

    public OperationProvidedRole getOperationprovidedrole() {
        return operationprovidedrole;
    }

    public void setOperationprovidedrole(OperationProvidedRole operationprovidedrole) {
        this.operationprovidedrole = operationprovidedrole;
    }

}