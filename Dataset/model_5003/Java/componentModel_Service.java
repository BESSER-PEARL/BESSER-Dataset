





import java.util.List;
import java.util.ArrayList;

public class componentModel_Service  {






    private List<componentModel_Interface> componentmodel_interfaces;




    private componentModel_InterfaceServiceMapTuple componentmodel_interfaceservicemaptuple;


    public componentModel_Service(
    ) {
        this.componentmodel_interfaces = new ArrayList<>();
    }

    public componentModel_Service(
        ArrayList<componentModel_Interface> componentmodel_interfaces    ) {
        this.componentmodel_interfaces = componentmodel_interfaces;
    }


    public List<componentModel_Interface> getComponentmodel_interfaces() {
        return componentmodel_interfaces;
    }

    public void addComponentmodel_interface(Componentmodel_interface componentmodel_interface) {
        this.componentmodel_interfaces.add(componentmodel_interface);
    }
    public componentModel_InterfaceServiceMapTuple getComponentmodel_interfaceservicemaptuple() {
        return componentmodel_interfaceservicemaptuple;
    }

    public void setComponentmodel_interfaceservicemaptuple(componentModel_InterfaceServiceMapTuple componentmodel_interfaceservicemaptuple) {
        this.componentmodel_interfaceservicemaptuple = componentmodel_interfaceservicemaptuple;
    }

}