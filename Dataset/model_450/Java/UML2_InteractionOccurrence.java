





import java.util.List;
import java.util.ArrayList;

public class UML2_InteractionOccurrence extends InteractionFragment {






    private List<UML2_InputPin> uml2_inputpins;




    private UML2_Interaction uml2_interaction;


    public UML2_InteractionOccurrence(
    ) {
        super(
        );
        this.uml2_inputpins = new ArrayList<>();
    }

    public UML2_InteractionOccurrence(
        ArrayList<UML2_InputPin> uml2_inputpins    ) {
        this.uml2_inputpins = uml2_inputpins;
    }


    public List<UML2_InputPin> getUml2_inputpins() {
        return uml2_inputpins;
    }

    public void addUml2_inputpin(Uml2_inputpin uml2_inputpin) {
        this.uml2_inputpins.add(uml2_inputpin);
    }
    public UML2_Interaction getUml2_interaction() {
        return uml2_interaction;
    }

    public void setUml2_interaction(UML2_Interaction uml2_interaction) {
        this.uml2_interaction = uml2_interaction;
    }

}