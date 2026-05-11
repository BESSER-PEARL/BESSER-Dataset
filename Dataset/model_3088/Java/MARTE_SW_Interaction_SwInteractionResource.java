





import java.util.List;
import java.util.ArrayList;

public class MARTE_SW_Interaction_SwInteractionResource extends SwResource {

    private boolean isIntraMemoryPartitionInteraction;
    private String waitingQueuePolicy;
    private String waitingQueueCapacity;



    public MARTE_SW_Interaction_SwInteractionResource(
        boolean isIntraMemoryPartitionInteraction,        String waitingQueuePolicy,        String waitingQueueCapacity    ) {
        super(
        );
        this.isIntraMemoryPartitionInteraction = isIntraMemoryPartitionInteraction;
        this.waitingQueuePolicy = waitingQueuePolicy;
        this.waitingQueueCapacity = waitingQueueCapacity;
    }


    public boolean getIsintramemorypartitioninteraction() {
        return isIntraMemoryPartitionInteraction;
    }

    public void setIsintramemorypartitioninteraction(boolean isIntraMemoryPartitionInteraction) {
        this.isIntraMemoryPartitionInteraction = isIntraMemoryPartitionInteraction;
    }
    public String getWaitingqueuepolicy() {
        return waitingQueuePolicy;
    }

    public void setWaitingqueuepolicy(String waitingQueuePolicy) {
        this.waitingQueuePolicy = waitingQueuePolicy;
    }
    public String getWaitingqueuecapacity() {
        return waitingQueueCapacity;
    }

    public void setWaitingqueuecapacity(String waitingQueueCapacity) {
        this.waitingQueueCapacity = waitingQueueCapacity;
    }


}