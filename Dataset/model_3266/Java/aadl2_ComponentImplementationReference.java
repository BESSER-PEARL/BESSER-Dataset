





import java.util.List;
import java.util.ArrayList;

public class aadl2_ComponentImplementationReference extends Element {






    private List<aadl2_PrototypeBinding> aadl2_prototypebindings;




    private aadl2_Subcomponent aadl2_subcomponent;


    public aadl2_ComponentImplementationReference(
    ) {
        super(
        );
        this.aadl2_prototypebindings = new ArrayList<>();
    }

    public aadl2_ComponentImplementationReference(
        ArrayList<aadl2_PrototypeBinding> aadl2_prototypebindings    ) {
        this.aadl2_prototypebindings = aadl2_prototypebindings;
    }


    public List<aadl2_PrototypeBinding> getAadl2_prototypebindings() {
        return aadl2_prototypebindings;
    }

    public void addAadl2_prototypebinding(Aadl2_prototypebinding aadl2_prototypebinding) {
        this.aadl2_prototypebindings.add(aadl2_prototypebinding);
    }
    public aadl2_Subcomponent getAadl2_subcomponent() {
        return aadl2_subcomponent;
    }

    public void setAadl2_subcomponent(aadl2_Subcomponent aadl2_subcomponent) {
        this.aadl2_subcomponent = aadl2_subcomponent;
    }

}