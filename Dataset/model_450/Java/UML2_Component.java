





import java.util.List;
import java.util.ArrayList;

public class UML2_Component extends Class {

    private boolean isIndirectlyInstantiated;





    private List<UML2_Interface> uml2_interfaces;




    private List<UML2_Interface> uml2_interfaces;


    public UML2_Component(
        boolean isIndirectlyInstantiated    ) {
        super(
        );
        this.isIndirectlyInstantiated = isIndirectlyInstantiated;
        this.uml2_interfaces = new ArrayList<>();
        this.uml2_interfaces = new ArrayList<>();
    }

    public UML2_Component(
        boolean isIndirectlyInstantiated        ArrayList<UML2_Interface> uml2_interfaces,        ArrayList<UML2_Interface> uml2_interfaces    ) {
        this.isIndirectlyInstantiated = isIndirectlyInstantiated;
        this.uml2_interfaces = uml2_interfaces;
        this.uml2_interfaces = uml2_interfaces;
    }

    public boolean getIsindirectlyinstantiated() {
        return isIndirectlyInstantiated;
    }

    public void setIsindirectlyinstantiated(boolean isIndirectlyInstantiated) {
        this.isIndirectlyInstantiated = isIndirectlyInstantiated;
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