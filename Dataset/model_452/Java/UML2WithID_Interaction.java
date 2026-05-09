





import java.util.List;
import java.util.ArrayList;

public class UML2WithID_Interaction extends InteractionFragment, Behavior {






    private List<UML2WithID_InteractionFragment> uml2withid_interactionfragments;




    private List<UML2WithID_Lifeline> uml2withid_lifelines;




    private UML2WithID_Message uml2withid_message;




    private List<UML2WithID_Message> uml2withid_messages;




    private UML2WithID_InteractionFragment uml2withid_interactionfragment;




    private UML2WithID_Lifeline uml2withid_lifeline;


    public UML2WithID_Interaction(
    ) {
        super(
        );
        this.uml2withid_interactionfragments = new ArrayList<>();
        this.uml2withid_lifelines = new ArrayList<>();
        this.uml2withid_messages = new ArrayList<>();
    }

    public UML2WithID_Interaction(
        ArrayList<UML2WithID_InteractionFragment> uml2withid_interactionfragments,        ArrayList<UML2WithID_Lifeline> uml2withid_lifelines,        ArrayList<UML2WithID_Message> uml2withid_messages    ) {
        this.uml2withid_interactionfragments = uml2withid_interactionfragments;
        this.uml2withid_lifelines = uml2withid_lifelines;
        this.uml2withid_messages = uml2withid_messages;
    }


    public List<UML2WithID_InteractionFragment> getUml2withid_interactionfragments() {
        return uml2withid_interactionfragments;
    }

    public void addUml2withid_interactionfragment(Uml2withid_interactionfragment uml2withid_interactionfragment) {
        this.uml2withid_interactionfragments.add(uml2withid_interactionfragment);
    }
    public List<UML2WithID_Lifeline> getUml2withid_lifelines() {
        return uml2withid_lifelines;
    }

    public void addUml2withid_lifeline(Uml2withid_lifeline uml2withid_lifeline) {
        this.uml2withid_lifelines.add(uml2withid_lifeline);
    }
    public UML2WithID_Message getUml2withid_message() {
        return uml2withid_message;
    }

    public void setUml2withid_message(UML2WithID_Message uml2withid_message) {
        this.uml2withid_message = uml2withid_message;
    }
    public List<UML2WithID_Message> getUml2withid_messages() {
        return uml2withid_messages;
    }

    public void addUml2withid_message(Uml2withid_message uml2withid_message) {
        this.uml2withid_messages.add(uml2withid_message);
    }
    public UML2WithID_InteractionFragment getUml2withid_interactionfragment() {
        return uml2withid_interactionfragment;
    }

    public void setUml2withid_interactionfragment(UML2WithID_InteractionFragment uml2withid_interactionfragment) {
        this.uml2withid_interactionfragment = uml2withid_interactionfragment;
    }
    public UML2WithID_Lifeline getUml2withid_lifeline() {
        return uml2withid_lifeline;
    }

    public void setUml2withid_lifeline(UML2WithID_Lifeline uml2withid_lifeline) {
        this.uml2withid_lifeline = uml2withid_lifeline;
    }

}