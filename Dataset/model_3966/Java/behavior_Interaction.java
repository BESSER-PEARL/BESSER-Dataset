





import java.util.List;
import java.util.ArrayList;

public class behavior_Interaction extends InteractionFragment, Behavior {






    private List<behavior_InteractionFragment> behavior_interactionfragments;




    private behavior_Message behavior_message;




    private List<behavior_Lifeline> behavior_lifelines;




    private List<behavior_DestructionEvent> behavior_destructionevents;




    private behavior_Lifeline behavior_lifeline;




    private behavior_DestructionEvent behavior_destructionevent;




    private List<behavior_BehavioredClassifier> behavior_behavioredclassifiers;




    private behavior_InteractionFragment behavior_interactionfragment;




    private List<behavior_Message> behavior_messages;


    public behavior_Interaction(
    ) {
        super(
        );
        this.behavior_interactionfragments = new ArrayList<>();
        this.behavior_lifelines = new ArrayList<>();
        this.behavior_destructionevents = new ArrayList<>();
        this.behavior_behavioredclassifiers = new ArrayList<>();
        this.behavior_messages = new ArrayList<>();
    }

    public behavior_Interaction(
        ArrayList<behavior_InteractionFragment> behavior_interactionfragments,        ArrayList<behavior_Lifeline> behavior_lifelines,        ArrayList<behavior_DestructionEvent> behavior_destructionevents,        ArrayList<behavior_BehavioredClassifier> behavior_behavioredclassifiers,        ArrayList<behavior_Message> behavior_messages    ) {
        this.behavior_interactionfragments = behavior_interactionfragments;
        this.behavior_lifelines = behavior_lifelines;
        this.behavior_destructionevents = behavior_destructionevents;
        this.behavior_behavioredclassifiers = behavior_behavioredclassifiers;
        this.behavior_messages = behavior_messages;
    }


    public List<behavior_InteractionFragment> getBehavior_interactionfragments() {
        return behavior_interactionfragments;
    }

    public void addBehavior_interactionfragment(Behavior_interactionfragment behavior_interactionfragment) {
        this.behavior_interactionfragments.add(behavior_interactionfragment);
    }
    public behavior_Message getBehavior_message() {
        return behavior_message;
    }

    public void setBehavior_message(behavior_Message behavior_message) {
        this.behavior_message = behavior_message;
    }
    public List<behavior_Lifeline> getBehavior_lifelines() {
        return behavior_lifelines;
    }

    public void addBehavior_lifeline(Behavior_lifeline behavior_lifeline) {
        this.behavior_lifelines.add(behavior_lifeline);
    }
    public List<behavior_DestructionEvent> getBehavior_destructionevents() {
        return behavior_destructionevents;
    }

    public void addBehavior_destructionevent(Behavior_destructionevent behavior_destructionevent) {
        this.behavior_destructionevents.add(behavior_destructionevent);
    }
    public behavior_Lifeline getBehavior_lifeline() {
        return behavior_lifeline;
    }

    public void setBehavior_lifeline(behavior_Lifeline behavior_lifeline) {
        this.behavior_lifeline = behavior_lifeline;
    }
    public behavior_DestructionEvent getBehavior_destructionevent() {
        return behavior_destructionevent;
    }

    public void setBehavior_destructionevent(behavior_DestructionEvent behavior_destructionevent) {
        this.behavior_destructionevent = behavior_destructionevent;
    }
    public List<behavior_BehavioredClassifier> getBehavior_behavioredclassifiers() {
        return behavior_behavioredclassifiers;
    }

    public void addBehavior_behavioredclassifier(Behavior_behavioredclassifier behavior_behavioredclassifier) {
        this.behavior_behavioredclassifiers.add(behavior_behavioredclassifier);
    }
    public behavior_InteractionFragment getBehavior_interactionfragment() {
        return behavior_interactionfragment;
    }

    public void setBehavior_interactionfragment(behavior_InteractionFragment behavior_interactionfragment) {
        this.behavior_interactionfragment = behavior_interactionfragment;
    }
    public List<behavior_Message> getBehavior_messages() {
        return behavior_messages;
    }

    public void addBehavior_message(Behavior_message behavior_message) {
        this.behavior_messages.add(behavior_message);
    }

}