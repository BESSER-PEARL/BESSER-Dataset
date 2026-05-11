





import java.util.List;
import java.util.ArrayList;

public class componentModel_Signature  {

    private String name;





    private componentModel_Interface componentmodel_interface;




    private componentModel_Service componentmodel_service;


    public componentModel_Signature(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public componentModel_Interface getComponentmodel_interface() {
        return componentmodel_interface;
    }

    public void setComponentmodel_interface(componentModel_Interface componentmodel_interface) {
        this.componentmodel_interface = componentmodel_interface;
    }
    public componentModel_Service getComponentmodel_service() {
        return componentmodel_service;
    }

    public void setComponentmodel_service(componentModel_Service componentmodel_service) {
        this.componentmodel_service = componentmodel_service;
    }

}