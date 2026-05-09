





import java.util.List;
import java.util.ArrayList;

public class uml_Component extends Class {

    private String isIndirectlyInstantiated;





    private List<uml_PackageableElement> uml_packageableelements;




    private List<uml_Interface> uml_interfaces;




    private List<uml_Interface> uml_interfaces;




    private List<uml_ComponentRealization> uml_componentrealizations;




    private uml_ComponentRealization uml_componentrealization;


    public uml_Component(
        String isIndirectlyInstantiated    ) {
        super(
        );
        this.isIndirectlyInstantiated = isIndirectlyInstantiated;
        this.uml_packageableelements = new ArrayList<>();
        this.uml_interfaces = new ArrayList<>();
        this.uml_interfaces = new ArrayList<>();
        this.uml_componentrealizations = new ArrayList<>();
    }

    public uml_Component(
        String isIndirectlyInstantiated        ArrayList<uml_PackageableElement> uml_packageableelements,        ArrayList<uml_Interface> uml_interfaces,        ArrayList<uml_Interface> uml_interfaces,        ArrayList<uml_ComponentRealization> uml_componentrealizations    ) {
        this.isIndirectlyInstantiated = isIndirectlyInstantiated;
        this.uml_packageableelements = uml_packageableelements;
        this.uml_interfaces = uml_interfaces;
        this.uml_interfaces = uml_interfaces;
        this.uml_componentrealizations = uml_componentrealizations;
    }

    public String getIsindirectlyinstantiated() {
        return isIndirectlyInstantiated;
    }

    public void setIsindirectlyinstantiated(String isIndirectlyInstantiated) {
        this.isIndirectlyInstantiated = isIndirectlyInstantiated;
    }

    public List<uml_PackageableElement> getUml_packageableelements() {
        return uml_packageableelements;
    }

    public void addUml_packageableelement(Uml_packageableelement uml_packageableelement) {
        this.uml_packageableelements.add(uml_packageableelement);
    }
    public List<uml_Interface> getUml_interfaces() {
        return uml_interfaces;
    }

    public void addUml_interface(Uml_interface uml_interface) {
        this.uml_interfaces.add(uml_interface);
    }
    public List<uml_Interface> getUml_interfaces() {
        return uml_interfaces;
    }

    public void addUml_interface(Uml_interface uml_interface) {
        this.uml_interfaces.add(uml_interface);
    }
    public List<uml_ComponentRealization> getUml_componentrealizations() {
        return uml_componentrealizations;
    }

    public void addUml_componentrealization(Uml_componentrealization uml_componentrealization) {
        this.uml_componentrealizations.add(uml_componentrealization);
    }
    public uml_ComponentRealization getUml_componentrealization() {
        return uml_componentrealization;
    }

    public void setUml_componentrealization(uml_ComponentRealization uml_componentrealization) {
        this.uml_componentrealization = uml_componentrealization;
    }

}