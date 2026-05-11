





import java.util.List;
import java.util.ArrayList;

public class componentModel_ProvidedRole  {

    private String name;





    private componentModel_Interface componentmodel_interface;




    private componentModel_AssemblyContext componentmodel_assemblycontext;




    private componentModel_AssemblyContext componentmodel_assemblycontext;




    private componentModel_AssemblyConnector componentmodel_assemblyconnector;


    public componentModel_ProvidedRole(
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
    public componentModel_AssemblyContext getComponentmodel_assemblycontext() {
        return componentmodel_assemblycontext;
    }

    public void setComponentmodel_assemblycontext(componentModel_AssemblyContext componentmodel_assemblycontext) {
        this.componentmodel_assemblycontext = componentmodel_assemblycontext;
    }
    public componentModel_AssemblyContext getComponentmodel_assemblycontext() {
        return componentmodel_assemblycontext;
    }

    public void setComponentmodel_assemblycontext(componentModel_AssemblyContext componentmodel_assemblycontext) {
        this.componentmodel_assemblycontext = componentmodel_assemblycontext;
    }
    public componentModel_AssemblyConnector getComponentmodel_assemblyconnector() {
        return componentmodel_assemblyconnector;
    }

    public void setComponentmodel_assemblyconnector(componentModel_AssemblyConnector componentmodel_assemblyconnector) {
        this.componentmodel_assemblyconnector = componentmodel_assemblyconnector;
    }

}