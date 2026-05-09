





import java.util.List;
import java.util.ArrayList;

public class UML2_Gate extends MessageEnd {






    private UML2_Interaction uml2_interaction;




    private UML2_InteractionOccurrence uml2_interactionoccurrence;




    private UML2_CombinedFragment uml2_combinedfragment;


    public UML2_Gate(
    ) {
        super(
        );
    }



    public UML2_Interaction getUml2_interaction() {
        return uml2_interaction;
    }

    public void setUml2_interaction(UML2_Interaction uml2_interaction) {
        this.uml2_interaction = uml2_interaction;
    }
    public UML2_InteractionOccurrence getUml2_interactionoccurrence() {
        return uml2_interactionoccurrence;
    }

    public void setUml2_interactionoccurrence(UML2_InteractionOccurrence uml2_interactionoccurrence) {
        this.uml2_interactionoccurrence = uml2_interactionoccurrence;
    }
    public UML2_CombinedFragment getUml2_combinedfragment() {
        return uml2_combinedfragment;
    }

    public void setUml2_combinedfragment(UML2_CombinedFragment uml2_combinedfragment) {
        this.uml2_combinedfragment = uml2_combinedfragment;
    }

}