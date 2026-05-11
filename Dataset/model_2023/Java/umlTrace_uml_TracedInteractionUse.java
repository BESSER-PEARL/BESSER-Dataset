





import java.util.List;
import java.util.ArrayList;

public class umlTrace_uml_TracedInteractionUse extends TracedInteractionFragment {






    private uml_TracedInteraction uml_tracedinteraction;




    private List<uml_TracedValueSpecification> uml_tracedvaluespecifications;




    private List<uml_TracedGate> uml_tracedgates;




    private uml_TracedProperty uml_tracedproperty;




    private uml_TracedValueSpecification uml_tracedvaluespecification;


    public umlTrace_uml_TracedInteractionUse(
    ) {
        super(
        );
        this.uml_tracedvaluespecifications = new ArrayList<>();
        this.uml_tracedgates = new ArrayList<>();
    }

    public umlTrace_uml_TracedInteractionUse(
        ArrayList<uml_TracedValueSpecification> uml_tracedvaluespecifications,        ArrayList<uml_TracedGate> uml_tracedgates    ) {
        this.uml_tracedvaluespecifications = uml_tracedvaluespecifications;
        this.uml_tracedgates = uml_tracedgates;
    }


    public uml_TracedInteraction getUml_tracedinteraction() {
        return uml_tracedinteraction;
    }

    public void setUml_tracedinteraction(uml_TracedInteraction uml_tracedinteraction) {
        this.uml_tracedinteraction = uml_tracedinteraction;
    }
    public List<uml_TracedValueSpecification> getUml_tracedvaluespecifications() {
        return uml_tracedvaluespecifications;
    }

    public void addUml_tracedvaluespecification(Uml_tracedvaluespecification uml_tracedvaluespecification) {
        this.uml_tracedvaluespecifications.add(uml_tracedvaluespecification);
    }
    public List<uml_TracedGate> getUml_tracedgates() {
        return uml_tracedgates;
    }

    public void addUml_tracedgate(Uml_tracedgate uml_tracedgate) {
        this.uml_tracedgates.add(uml_tracedgate);
    }
    public uml_TracedProperty getUml_tracedproperty() {
        return uml_tracedproperty;
    }

    public void setUml_tracedproperty(uml_TracedProperty uml_tracedproperty) {
        this.uml_tracedproperty = uml_tracedproperty;
    }
    public uml_TracedValueSpecification getUml_tracedvaluespecification() {
        return uml_tracedvaluespecification;
    }

    public void setUml_tracedvaluespecification(uml_TracedValueSpecification uml_tracedvaluespecification) {
        this.uml_tracedvaluespecification = uml_tracedvaluespecification;
    }

}