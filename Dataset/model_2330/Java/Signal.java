





import java.util.List;
import java.util.ArrayList;

public class Signal  {






    private Actions_IntermediateActions_BroadcastSignalAction actions_intermediateactions_broadcastsignalaction;




    private Actions_BasicActions_SendSignalAction actions_basicactions_sendsignalaction;


    public Signal(
    ) {
    }



    public Actions_IntermediateActions_BroadcastSignalAction getActions_intermediateactions_broadcastsignalaction() {
        return actions_intermediateactions_broadcastsignalaction;
    }

    public void setActions_intermediateactions_broadcastsignalaction(Actions_IntermediateActions_BroadcastSignalAction actions_intermediateactions_broadcastsignalaction) {
        this.actions_intermediateactions_broadcastsignalaction = actions_intermediateactions_broadcastsignalaction;
    }
    public Actions_BasicActions_SendSignalAction getActions_basicactions_sendsignalaction() {
        return actions_basicactions_sendsignalaction;
    }

    public void setActions_basicactions_sendsignalaction(Actions_BasicActions_SendSignalAction actions_basicactions_sendsignalaction) {
        this.actions_basicactions_sendsignalaction = actions_basicactions_sendsignalaction;
    }

}