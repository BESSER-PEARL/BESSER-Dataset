





import java.util.List;
import java.util.ArrayList;

public class uml3_0_0_Component extends Class {

    private String isIndirectlyInstantiated;





    private List<uml3_0_0_Interface> uml3_0_0_interfaces;




    private List<uml3_0_0_ComponentRealization> uml3_0_0_componentrealizations;




    private List<uml3_0_0_PackageableElement> uml3_0_0_packageableelements;




    private List<uml3_0_0_Interface> uml3_0_0_interfaces;




    private uml3_0_0_ComponentRealization uml3_0_0_componentrealization;


    public uml3_0_0_Component(
        String isIndirectlyInstantiated    ) {
        super(
        );
        this.isIndirectlyInstantiated = isIndirectlyInstantiated;
        this.uml3_0_0_interfaces = new ArrayList<>();
        this.uml3_0_0_componentrealizations = new ArrayList<>();
        this.uml3_0_0_packageableelements = new ArrayList<>();
        this.uml3_0_0_interfaces = new ArrayList<>();
    }

    public uml3_0_0_Component(
        String isIndirectlyInstantiated        ArrayList<uml3_0_0_Interface> uml3_0_0_interfaces,        ArrayList<uml3_0_0_ComponentRealization> uml3_0_0_componentrealizations,        ArrayList<uml3_0_0_PackageableElement> uml3_0_0_packageableelements,        ArrayList<uml3_0_0_Interface> uml3_0_0_interfaces    ) {
        this.isIndirectlyInstantiated = isIndirectlyInstantiated;
        this.uml3_0_0_interfaces = uml3_0_0_interfaces;
        this.uml3_0_0_componentrealizations = uml3_0_0_componentrealizations;
        this.uml3_0_0_packageableelements = uml3_0_0_packageableelements;
        this.uml3_0_0_interfaces = uml3_0_0_interfaces;
    }

    public String getIsindirectlyinstantiated() {
        return isIndirectlyInstantiated;
    }

    public void setIsindirectlyinstantiated(String isIndirectlyInstantiated) {
        this.isIndirectlyInstantiated = isIndirectlyInstantiated;
    }

    public List<uml3_0_0_Interface> getUml3_0_0_interfaces() {
        return uml3_0_0_interfaces;
    }

    public void addUml3_0_0_interface(Uml3_0_0_interface uml3_0_0_interface) {
        this.uml3_0_0_interfaces.add(uml3_0_0_interface);
    }
    public List<uml3_0_0_ComponentRealization> getUml3_0_0_componentrealizations() {
        return uml3_0_0_componentrealizations;
    }

    public void addUml3_0_0_componentrealization(Uml3_0_0_componentrealization uml3_0_0_componentrealization) {
        this.uml3_0_0_componentrealizations.add(uml3_0_0_componentrealization);
    }
    public List<uml3_0_0_PackageableElement> getUml3_0_0_packageableelements() {
        return uml3_0_0_packageableelements;
    }

    public void addUml3_0_0_packageableelement(Uml3_0_0_packageableelement uml3_0_0_packageableelement) {
        this.uml3_0_0_packageableelements.add(uml3_0_0_packageableelement);
    }
    public List<uml3_0_0_Interface> getUml3_0_0_interfaces() {
        return uml3_0_0_interfaces;
    }

    public void addUml3_0_0_interface(Uml3_0_0_interface uml3_0_0_interface) {
        this.uml3_0_0_interfaces.add(uml3_0_0_interface);
    }
    public uml3_0_0_ComponentRealization getUml3_0_0_componentrealization() {
        return uml3_0_0_componentrealization;
    }

    public void setUml3_0_0_componentrealization(uml3_0_0_ComponentRealization uml3_0_0_componentrealization) {
        this.uml3_0_0_componentrealization = uml3_0_0_componentrealization;
    }

}