





import java.util.List;
import java.util.ArrayList;

public class aadl2_Subcomponent extends ModalElement, Context, StructuralFeature, FlowElement, ArrayableElement {

    private String allModes;





    private List<aadl2_ModeBinding> aadl2_modebindings;




    private aadl2_SubcomponentType aadl2_subcomponenttype;




    private List<aadl2_ComponentImplementationReference> aadl2_componentimplementationreferences;




    private aadl2_Subcomponent aadl2_subcomponent;




    private List<aadl2_PrototypeBinding> aadl2_prototypebindings;


    public aadl2_Subcomponent(
        String allModes    ) {
        super(
        );
        this.allModes = allModes;
        this.aadl2_modebindings = new ArrayList<>();
        this.aadl2_componentimplementationreferences = new ArrayList<>();
        this.aadl2_prototypebindings = new ArrayList<>();
    }

    public aadl2_Subcomponent(
        String allModes        ArrayList<aadl2_ModeBinding> aadl2_modebindings,        ArrayList<aadl2_ComponentImplementationReference> aadl2_componentimplementationreferences,        ArrayList<aadl2_PrototypeBinding> aadl2_prototypebindings    ) {
        this.allModes = allModes;
        this.aadl2_modebindings = aadl2_modebindings;
        this.aadl2_componentimplementationreferences = aadl2_componentimplementationreferences;
        this.aadl2_prototypebindings = aadl2_prototypebindings;
    }

    public String getAllmodes() {
        return allModes;
    }

    public void setAllmodes(String allModes) {
        this.allModes = allModes;
    }

    public List<aadl2_ModeBinding> getAadl2_modebindings() {
        return aadl2_modebindings;
    }

    public void addAadl2_modebinding(Aadl2_modebinding aadl2_modebinding) {
        this.aadl2_modebindings.add(aadl2_modebinding);
    }
    public aadl2_SubcomponentType getAadl2_subcomponenttype() {
        return aadl2_subcomponenttype;
    }

    public void setAadl2_subcomponenttype(aadl2_SubcomponentType aadl2_subcomponenttype) {
        this.aadl2_subcomponenttype = aadl2_subcomponenttype;
    }
    public List<aadl2_ComponentImplementationReference> getAadl2_componentimplementationreferences() {
        return aadl2_componentimplementationreferences;
    }

    public void addAadl2_componentimplementationreference(Aadl2_componentimplementationreference aadl2_componentimplementationreference) {
        this.aadl2_componentimplementationreferences.add(aadl2_componentimplementationreference);
    }
    public aadl2_Subcomponent getAadl2_subcomponent() {
        return aadl2_subcomponent;
    }

    public void setAadl2_subcomponent(aadl2_Subcomponent aadl2_subcomponent) {
        this.aadl2_subcomponent = aadl2_subcomponent;
    }
    public List<aadl2_PrototypeBinding> getAadl2_prototypebindings() {
        return aadl2_prototypebindings;
    }

    public void addAadl2_prototypebinding(Aadl2_prototypebinding aadl2_prototypebinding) {
        this.aadl2_prototypebindings.add(aadl2_prototypebinding);
    }

}