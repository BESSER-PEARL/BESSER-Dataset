





import java.util.List;
import java.util.ArrayList;

public class UML2_Component extends Class {

    private boolean isIndirectlyInstantiated;





    private List<UML2_PackageableElement> uml2_packageableelements;




    private List<UML2_Interface> uml2_interfaces;




    private List<UML2_Interface> uml2_interfaces;


    public UML2_Component(
        boolean isIndirectlyInstantiated    ) {
        super(
        );
        this.isIndirectlyInstantiated = isIndirectlyInstantiated;
        this.uml2_packageableelements = new ArrayList<>();
        this.uml2_interfaces = new ArrayList<>();
        this.uml2_interfaces = new ArrayList<>();
    }

    public UML2_Component(
        boolean isIndirectlyInstantiated        ArrayList<UML2_PackageableElement> uml2_packageableelements,        ArrayList<UML2_Interface> uml2_interfaces,        ArrayList<UML2_Interface> uml2_interfaces    ) {
        this.isIndirectlyInstantiated = isIndirectlyInstantiated;
        this.uml2_packageableelements = uml2_packageableelements;
        this.uml2_interfaces = uml2_interfaces;
        this.uml2_interfaces = uml2_interfaces;
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
    public List<UML2_Interface> getUml2_interfaces() {
        return uml2_interfaces;
    }

    public void addUml2_interface(Uml2_interface uml2_interface) {
        this.uml2_interfaces.add(uml2_interface);
    }
    public List<UML2_Interface> getUml2_interfaces() {
        return uml2_interfaces;
    }

    public void addUml2_interface(Uml2_interface uml2_interface) {
        this.uml2_interfaces.add(uml2_interface);
    }

}