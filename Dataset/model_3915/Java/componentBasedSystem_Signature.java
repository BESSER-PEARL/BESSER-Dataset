





import java.util.List;
import java.util.ArrayList;

public class componentBasedSystem_Signature  {

    private String name;





    private List<componentBasedSystem_Parameter> componentbasedsystem_parameters;




    private ReturnType returntype;




    private componentBasedSystem_Service componentbasedsystem_service;




    private componentBasedSystem_Interface componentbasedsystem_interface;


    public componentBasedSystem_Signature(
        String name    ) {
        this.name = name;
        this.componentbasedsystem_parameters = new ArrayList<>();
    }

    public componentBasedSystem_Signature(
        String name        ArrayList<componentBasedSystem_Parameter> componentbasedsystem_parameters    ) {
        this.name = name;
        this.componentbasedsystem_parameters = componentbasedsystem_parameters;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<componentBasedSystem_Parameter> getComponentbasedsystem_parameters() {
        return componentbasedsystem_parameters;
    }

    public void addComponentbasedsystem_parameter(Componentbasedsystem_parameter componentbasedsystem_parameter) {
        this.componentbasedsystem_parameters.add(componentbasedsystem_parameter);
    }
    public ReturnType getReturntype() {
        return returntype;
    }

    public void setReturntype(ReturnType returntype) {
        this.returntype = returntype;
    }
    public componentBasedSystem_Service getComponentbasedsystem_service() {
        return componentbasedsystem_service;
    }

    public void setComponentbasedsystem_service(componentBasedSystem_Service componentbasedsystem_service) {
        this.componentbasedsystem_service = componentbasedsystem_service;
    }
    public componentBasedSystem_Interface getComponentbasedsystem_interface() {
        return componentbasedsystem_interface;
    }

    public void setComponentbasedsystem_interface(componentBasedSystem_Interface componentbasedsystem_interface) {
        this.componentbasedsystem_interface = componentbasedsystem_interface;
    }

}