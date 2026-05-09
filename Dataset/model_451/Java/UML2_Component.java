





import java.util.List;
import java.util.ArrayList;

public class UML2_Component extends Class {

    private boolean isIndirectlyInstantiated;





    private List<UML2_PackageableElement> uml2_packageableelements;




    private List<UML2_Realization> uml2_realizations;




    private UML2_Realization uml2_realization;


    public UML2_Component(
        boolean isIndirectlyInstantiated    ) {
        super(
        );
        this.isIndirectlyInstantiated = isIndirectlyInstantiated;
        this.uml2_packageableelements = new ArrayList<>();
        this.uml2_realizations = new ArrayList<>();
    }

    public UML2_Component(
        boolean isIndirectlyInstantiated        ArrayList<UML2_PackageableElement> uml2_packageableelements,        ArrayList<UML2_Realization> uml2_realizations    ) {
        this.isIndirectlyInstantiated = isIndirectlyInstantiated;
        this.uml2_packageableelements = uml2_packageableelements;
        this.uml2_realizations = uml2_realizations;
    }

    public boolean getIsindirectlyinstantiated() {
        return isIndirectlyInstantiated;
    }

    public void setIsindirectlyinstantiated(boolean isIndirectlyInstantiated) {
        this.isIndirectlyInstantiated = isIndirectlyInstantiated;
    }

    public List<UML2_PackageableElement> getUml2_packageableelements() {
        return uml2_packageableelements;
    }

    public void addUml2_packageableelement(Uml2_packageableelement uml2_packageableelement) {
        this.uml2_packageableelements.add(uml2_packageableelement);
    }
    public List<UML2_Realization> getUml2_realizations() {
        return uml2_realizations;
    }

    public void addUml2_realization(Uml2_realization uml2_realization) {
        this.uml2_realizations.add(uml2_realization);
    }
    public UML2_Realization getUml2_realization() {
        return uml2_realization;
    }

    public void setUml2_realization(UML2_Realization uml2_realization) {
        this.uml2_realization = uml2_realization;
    }

}