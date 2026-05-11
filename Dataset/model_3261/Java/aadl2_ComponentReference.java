





import java.util.List;
import java.util.ArrayList;

public class aadl2_ComponentReference extends ComponentPrototypeActual {






    private List<aadl2_PrototypeBinding> aadl2_prototypebindings;


    public aadl2_ComponentReference(
    ) {
        super(
        );
        this.aadl2_prototypebindings = new ArrayList<>();
    }

    public aadl2_ComponentReference(
        ArrayList<aadl2_PrototypeBinding> aadl2_prototypebindings    ) {
        this.aadl2_prototypebindings = aadl2_prototypebindings;
    }


    public List<aadl2_PrototypeBinding> getAadl2_prototypebindings() {
        return aadl2_prototypebindings;
    }

    public void addAadl2_prototypebinding(Aadl2_prototypebinding aadl2_prototypebinding) {
        this.aadl2_prototypebindings.add(aadl2_prototypebinding);
    }

}