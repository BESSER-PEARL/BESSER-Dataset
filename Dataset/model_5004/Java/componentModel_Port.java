





import java.util.List;
import java.util.ArrayList;

public class componentModel_Port  {

    private String name;





    private componentModel_ComponentFeature componentmodel_componentfeature;




    private componentModel_PortType componentmodel_porttype;


    public componentModel_Port(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public componentModel_ComponentFeature getComponentmodel_componentfeature() {
        return componentmodel_componentfeature;
    }

    public void setComponentmodel_componentfeature(componentModel_ComponentFeature componentmodel_componentfeature) {
        this.componentmodel_componentfeature = componentmodel_componentfeature;
    }
    public componentModel_PortType getComponentmodel_porttype() {
        return componentmodel_porttype;
    }

    public void setComponentmodel_porttype(componentModel_PortType componentmodel_porttype) {
        this.componentmodel_porttype = componentmodel_porttype;
    }

}