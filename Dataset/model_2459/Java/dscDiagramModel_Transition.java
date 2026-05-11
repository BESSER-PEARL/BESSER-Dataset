





import java.util.List;
import java.util.ArrayList;

public class dscDiagramModel_Transition extends Relationship {

    private boolean triggeredByEvent;
    private String guardID;
    private String transitionID;
    private boolean showTransitionID;
    private boolean showProperties;
    private String actionID;
    private String eventID;



    public dscDiagramModel_Transition(
        boolean triggeredByEvent,        String guardID,        String transitionID,        boolean showTransitionID,        boolean showProperties,        String actionID,        String eventID    ) {
        super(
        );
        this.triggeredByEvent = triggeredByEvent;
        this.guardID = guardID;
        this.transitionID = transitionID;
        this.showTransitionID = showTransitionID;
        this.showProperties = showProperties;
        this.actionID = actionID;
        this.eventID = eventID;
    }


    public boolean getTriggeredbyevent() {
        return triggeredByEvent;
    }

    public void setTriggeredbyevent(boolean triggeredByEvent) {
        this.triggeredByEvent = triggeredByEvent;
    }
    public String getGuardid() {
        return guardID;
    }

    public void setGuardid(String guardID) {
        this.guardID = guardID;
    }
    public String getTransitionid() {
        return transitionID;
    }

    public void setTransitionid(String transitionID) {
        this.transitionID = transitionID;
    }
    public boolean getShowtransitionid() {
        return showTransitionID;
    }

    public void setShowtransitionid(boolean showTransitionID) {
        this.showTransitionID = showTransitionID;
    }
    public boolean getShowproperties() {
        return showProperties;
    }

    public void setShowproperties(boolean showProperties) {
        this.showProperties = showProperties;
    }
    public String getActionid() {
        return actionID;
    }

    public void setActionid(String actionID) {
        this.actionID = actionID;
    }
    public String getEventid() {
        return eventID;
    }

    public void setEventid(String eventID) {
        this.eventID = eventID;
    }


}