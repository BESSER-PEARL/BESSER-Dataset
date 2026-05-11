





import java.util.List;
import java.util.ArrayList;

public class MARTE_SW_Interaction_SwInteractionResource extends SwResource {

    private String waitingQueuePolicy;
    private boolean isIntraMemoryPartitionInteraction;
    private String waitingQueueCapacity;



    public MARTE_SW_Interaction_SwInteractionResource(
        String waitingQueuePolicy,        boolean isIntraMemoryPartitionInteraction,        String waitingQueueCapacity    ) {
        super(
        );
        this.waitingQueuePolicy = waitingQueuePolicy;
        this.isIntraMemoryPartitionInteraction = isIntraMemoryPartitionInteraction;
        this.waitingQueueCapacity = waitingQueueCapacity;
    }


    public String getWaitingqueuepolicy() {
        return waitingQueuePolicy;
    }

    public void setWaitingqueuepolicy(String waitingQueuePolicy) {
        this.waitingQueuePolicy = waitingQueuePolicy;
    }
    public boolean getIsintramemorypartitioninteraction() {
        return isIntraMemoryPartitionInteraction;
    }

    public void setIsintramemorypartitioninteraction(boolean isIntraMemoryPartitionInteraction) {
        this.isIntraMemoryPartitionInteraction = isIntraMemoryPartitionInteraction;
    }
    public String getWaitingqueuecapacity() {
        return waitingQueueCapacity;
    }

    public void setWaitingqueuecapacity(String waitingQueueCapacity) {
        this.waitingQueueCapacity = waitingQueueCapacity;
    }


}