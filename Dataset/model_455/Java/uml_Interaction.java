





import java.util.List;
import java.util.ArrayList;

public class uml_Interaction extends InteractionFragment, Behavior {






    private uml_InteractionFragment uml_interactionfragment;




    private List<uml_InteractionFragment> uml_interactionfragments;




    private List<uml_Lifeline> uml_lifelines;




    private uml_Lifeline uml_lifeline;




    private uml_Message uml_message;




    private List<uml_Message> uml_messages;


    public uml_Interaction(
    ) {
        super(
        );
        this.uml_interactionfragments = new ArrayList<>();
        this.uml_lifelines = new ArrayList<>();
        this.uml_messages = new ArrayList<>();
    }

    public uml_Interaction(
        ArrayList<uml_InteractionFragment> uml_interactionfragments,        ArrayList<uml_Lifeline> uml_lifelines,        ArrayList<uml_Message> uml_messages    ) {
        this.uml_interactionfragments = uml_interactionfragments;
        this.uml_lifelines = uml_lifelines;
        this.uml_messages = uml_messages;
    }


    public uml_InteractionFragment getUml_interactionfragment() {
        return uml_interactionfragment;
    }

    public void setUml_interactionfragment(uml_InteractionFragment uml_interactionfragment) {
        this.uml_interactionfragment = uml_interactionfragment;
    }
    public List<uml_InteractionFragment> getUml_interactionfragments() {
        return uml_interactionfragments;
    }

    public void addUml_interactionfragment(Uml_interactionfragment uml_interactionfragment) {
        this.uml_interactionfragments.add(uml_interactionfragment);
    }
    public List<uml_Lifeline> getUml_lifelines() {
        return uml_lifelines;
    }

    public void addUml_lifeline(Uml_lifeline uml_lifeline) {
        this.uml_lifelines.add(uml_lifeline);
    }
    public uml_Lifeline getUml_lifeline() {
        return uml_lifeline;
    }

    public void setUml_lifeline(uml_Lifeline uml_lifeline) {
        this.uml_lifeline = uml_lifeline;
    }
    public uml_Message getUml_message() {
        return uml_message;
    }

    public void setUml_message(uml_Message uml_message) {
        this.uml_message = uml_message;
    }
    public List<uml_Message> getUml_messages() {
        return uml_messages;
    }

    public void addUml_message(Uml_message uml_message) {
        this.uml_messages.add(uml_message);
    }

}