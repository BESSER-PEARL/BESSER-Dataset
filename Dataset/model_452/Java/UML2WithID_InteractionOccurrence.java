





import java.util.List;
import java.util.ArrayList;

public class UML2WithID_InteractionOccurrence extends InteractionFragment {






    private List<UML2WithID_InputPin> uml2withid_inputpins;




    private UML2WithID_Interaction uml2withid_interaction;


    public UML2WithID_InteractionOccurrence(
    ) {
        super(
        );
        this.uml2withid_inputpins = new ArrayList<>();
    }

    public UML2WithID_InteractionOccurrence(
        ArrayList<UML2WithID_InputPin> uml2withid_inputpins    ) {
        this.uml2withid_inputpins = uml2withid_inputpins;
    }


    public List<UML2WithID_InputPin> getUml2withid_inputpins() {
        return uml2withid_inputpins;
    }

    public void addUml2withid_inputpin(Uml2withid_inputpin uml2withid_inputpin) {
        this.uml2withid_inputpins.add(uml2withid_inputpin);
    }
    public UML2WithID_Interaction getUml2withid_interaction() {
        return uml2withid_interaction;
    }

    public void setUml2withid_interaction(UML2WithID_Interaction uml2withid_interaction) {
        this.uml2withid_interaction = uml2withid_interaction;
    }

}