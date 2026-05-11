





import java.util.List;
import java.util.ArrayList;

public class componentModel_errorModes  {

    private String name;





    private componentModel_PortType componentmodel_porttype;


    public componentModel_errorModes(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public componentModel_PortType getComponentmodel_porttype() {
        return componentmodel_porttype;
    }

    public void setComponentmodel_porttype(componentModel_PortType componentmodel_porttype) {
        this.componentmodel_porttype = componentmodel_porttype;
    }

}