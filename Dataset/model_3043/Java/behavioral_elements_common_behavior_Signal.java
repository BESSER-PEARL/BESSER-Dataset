





import java.util.List;
import java.util.ArrayList;

public class behavioral_elements_common_behavior_Signal extends Classifier {






    private List<SignalEvent> signalevents;




    private List<SendAction> sendactions;


    public behavioral_elements_common_behavior_Signal(
    ) {
        super(
        );
        this.signalevents = new ArrayList<>();
        this.sendactions = new ArrayList<>();
    }

    public behavioral_elements_common_behavior_Signal(
        ArrayList<SignalEvent> signalevents,        ArrayList<SendAction> sendactions    ) {
        this.signalevents = signalevents;
        this.sendactions = sendactions;
    }


    public List<SignalEvent> getSignalevents() {
        return signalevents;
    }

    public void addSignalevent(Signalevent signalevent) {
        this.signalevents.add(signalevent);
    }
    public List<SendAction> getSendactions() {
        return sendactions;
    }

    public void addSendaction(Sendaction sendaction) {
        this.sendactions.add(sendaction);
    }

}