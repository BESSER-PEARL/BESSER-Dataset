





import java.util.List;
import java.util.ArrayList;

public class UML2WithID_Component extends Class {

    private boolean isIndirectlyInstantiated;





    private List<UML2WithID_Interface> uml2withid_interfaces;




    private List<UML2WithID_Interface> uml2withid_interfaces;


    public UML2WithID_Component(
        boolean isIndirectlyInstantiated    ) {
        super(
        );
        this.isIndirectlyInstantiated = isIndirectlyInstantiated;
        this.uml2withid_interfaces = new ArrayList<>();
        this.uml2withid_interfaces = new ArrayList<>();
    }

    public UML2WithID_Component(
        boolean isIndirectlyInstantiated        ArrayList<UML2WithID_Interface> uml2withid_interfaces,        ArrayList<UML2WithID_Interface> uml2withid_interfaces    ) {
        this.isIndirectlyInstantiated = isIndirectlyInstantiated;
        this.uml2withid_interfaces = uml2withid_interfaces;
        this.uml2withid_interfaces = uml2withid_interfaces;
    }

    public boolean getIsindirectlyinstantiated() {
        return isIndirectlyInstantiated;
    }

    public void setIsindirectlyinstantiated(boolean isIndirectlyInstantiated) {
        this.isIndirectlyInstantiated = isIndirectlyInstantiated;
    }

    public List<UML2WithID_Interface> getUml2withid_interfaces() {
        return uml2withid_interfaces;
    }

    public void addUml2withid_interface(Uml2withid_interface uml2withid_interface) {
        this.uml2withid_interfaces.add(uml2withid_interface);
    }
    public List<UML2WithID_Interface> getUml2withid_interfaces() {
        return uml2withid_interfaces;
    }

    public void addUml2withid_interface(Uml2withid_interface uml2withid_interface) {
        this.uml2withid_interfaces.add(uml2withid_interface);
    }

}