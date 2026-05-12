





import java.util.List;
import java.util.ArrayList;

public class UML2_Interaction extends InteractionFragment, Behavior {






    private UML2_Lifeline uml2_lifeline;




    private List<UML2_InteractionFragment> uml2_interactionfragments;




    private List<UML2_Message> uml2_messages;




    private List<UML2_Lifeline> uml2_lifelines;




    private UML2_InteractionFragment uml2_interactionfragment;




    private UML2_Message uml2_message;


    public UML2_Interaction(
    ) {
        super(
        );
        this.uml2_interactionfragments = new ArrayList<>();
        this.uml2_messages = new ArrayList<>();
        this.uml2_lifelines = new ArrayList<>();
    }

    public UML2_Interaction(
        ArrayList<UML2_InteractionFragment> uml2_interactionfragments,        ArrayList<UML2_Message> uml2_messages,        ArrayList<UML2_Lifeline> uml2_lifelines    ) {
        this.uml2_interactionfragments = uml2_interactionfragments;
        this.uml2_messages = uml2_messages;
        this.uml2_lifelines = uml2_lifelines;
    }


    public UML2_Lifeline getUml2_lifeline() {
        return uml2_lifeline;
    }

    public void setUml2_lifeline(UML2_Lifeline uml2_lifeline) {
        this.uml2_lifeline = uml2_lifeline;
    }
    public List<UML2_InteractionFragment> getUml2_interactionfragments() {
        return uml2_interactionfragments;
    }

    public void addUml2_interactionfragment(Uml2_interactionfragment uml2_interactionfragment) {
        this.uml2_interactionfragments.add(uml2_interactionfragment);
    }
    public List<UML2_Message> getUml2_messages() {
        return uml2_messages;
    }

    public void addUml2_message(Uml2_message uml2_message) {
        this.uml2_messages.add(uml2_message);
    }
    public List<UML2_Lifeline> getUml2_lifelines() {
        return uml2_lifelines;
    }

    public void addUml2_lifeline(Uml2_lifeline uml2_lifeline) {
        this.uml2_lifelines.add(uml2_lifeline);
    }
    public UML2_InteractionFragment getUml2_interactionfragment() {
        return uml2_interactionfragment;
    }

    public void setUml2_interactionfragment(UML2_InteractionFragment uml2_interactionfragment) {
        this.uml2_interactionfragment = uml2_interactionfragment;
    }
    public UML2_Message getUml2_message() {
        return uml2_message;
    }

    public void setUml2_message(UML2_Message uml2_message) {
        this.uml2_message = uml2_message;
    }

}