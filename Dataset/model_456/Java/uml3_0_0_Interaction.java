





import java.util.List;
import java.util.ArrayList;

public class uml3_0_0_Interaction extends InteractionFragment, Behavior {






    private uml3_0_0_InteractionFragment uml3_0_0_interactionfragment;




    private List<uml3_0_0_InteractionFragment> uml3_0_0_interactionfragments;




    private List<uml3_0_0_Lifeline> uml3_0_0_lifelines;




    private List<uml3_0_0_Message> uml3_0_0_messages;




    private uml3_0_0_Message uml3_0_0_message;




    private uml3_0_0_Lifeline uml3_0_0_lifeline;


    public uml3_0_0_Interaction(
    ) {
        super(
        );
        this.uml3_0_0_interactionfragments = new ArrayList<>();
        this.uml3_0_0_lifelines = new ArrayList<>();
        this.uml3_0_0_messages = new ArrayList<>();
    }

    public uml3_0_0_Interaction(
        ArrayList<uml3_0_0_InteractionFragment> uml3_0_0_interactionfragments,        ArrayList<uml3_0_0_Lifeline> uml3_0_0_lifelines,        ArrayList<uml3_0_0_Message> uml3_0_0_messages    ) {
        this.uml3_0_0_interactionfragments = uml3_0_0_interactionfragments;
        this.uml3_0_0_lifelines = uml3_0_0_lifelines;
        this.uml3_0_0_messages = uml3_0_0_messages;
    }


    public uml3_0_0_InteractionFragment getUml3_0_0_interactionfragment() {
        return uml3_0_0_interactionfragment;
    }

    public void setUml3_0_0_interactionfragment(uml3_0_0_InteractionFragment uml3_0_0_interactionfragment) {
        this.uml3_0_0_interactionfragment = uml3_0_0_interactionfragment;
    }
    public List<uml3_0_0_InteractionFragment> getUml3_0_0_interactionfragments() {
        return uml3_0_0_interactionfragments;
    }

    public void addUml3_0_0_interactionfragment(Uml3_0_0_interactionfragment uml3_0_0_interactionfragment) {
        this.uml3_0_0_interactionfragments.add(uml3_0_0_interactionfragment);
    }
    public List<uml3_0_0_Lifeline> getUml3_0_0_lifelines() {
        return uml3_0_0_lifelines;
    }

    public void addUml3_0_0_lifeline(Uml3_0_0_lifeline uml3_0_0_lifeline) {
        this.uml3_0_0_lifelines.add(uml3_0_0_lifeline);
    }
    public List<uml3_0_0_Message> getUml3_0_0_messages() {
        return uml3_0_0_messages;
    }

    public void addUml3_0_0_message(Uml3_0_0_message uml3_0_0_message) {
        this.uml3_0_0_messages.add(uml3_0_0_message);
    }
    public uml3_0_0_Message getUml3_0_0_message() {
        return uml3_0_0_message;
    }

    public void setUml3_0_0_message(uml3_0_0_Message uml3_0_0_message) {
        this.uml3_0_0_message = uml3_0_0_message;
    }
    public uml3_0_0_Lifeline getUml3_0_0_lifeline() {
        return uml3_0_0_lifeline;
    }

    public void setUml3_0_0_lifeline(uml3_0_0_Lifeline uml3_0_0_lifeline) {
        this.uml3_0_0_lifeline = uml3_0_0_lifeline;
    }

}